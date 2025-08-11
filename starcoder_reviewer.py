# starcoder_reviewer.py
import modal
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_NAME = "bigcode/starcoder2-15b"

app = modal.App("code-explainer-starcoder")

# Modal image with required packages
image = (
    modal.Image.debian_slim()
    .pip_install("torch", "transformers", "accelerate", "fastapi[standard]")
)

@app.cls(gpu="A100", image=image, timeout=1800, scaledown_window=600)
class StarCoderExplainer:
    @modal.enter()
    def load_model(self):
        print(" Loading model...")
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            trust_remote_code=True,
            torch_dtype=torch.float16,
            device_map="auto",
        )
        print(" Model loaded!")

    @modal.method()
    def explain(self, code: str) -> str:
        prompt = f"### Explain what this code does:\n{code.strip()}\n\n### Explanation:\n"
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        
        with torch.no_grad():
            output = self.model.generate(
                **inputs,
                max_new_tokens=256,
                do_sample=True,
                temperature=0.7,
                top_k=50,
                top_p=0.95,
                pad_token_id=self.tokenizer.eos_token_id,
            )

        decoded = self.tokenizer.decode(output[0], skip_special_tokens=True)
        explanation = decoded[len(prompt):].strip()
        return explanation

# Web API endpoint
@app.function(gpu="A100", image=image, timeout=1800, scaledown_window=600)
@modal.fastapi_endpoint(method="POST")
def explain_code_api(item: dict):
    if "code" not in item:
        return {"error": "Missing 'code' field in request"}
    
    code = item["code"]
    print(" Loading model for API request...")
    
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True,
        torch_dtype=torch.float16,
        device_map="auto",
    )
    print(" Model loaded!")

    prompt = f"### Explain what this code does:\n{code.strip()}\n\n### Explanation:\n"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=256,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            pad_token_id=tokenizer.eos_token_id,
        )

    decoded = tokenizer.decode(output[0], skip_special_tokens=True)
    explanation = decoded[len(prompt):].strip()

    return {"explanation": explanation}

@app.local_entrypoint()
def main():
    test_code = """
def square(x):
    return x * x
"""
    explainer = StarCoderExplainer()
    result = explainer.explain.remote(test_code)
    print("\n🧠 Explanation:\n", result)
