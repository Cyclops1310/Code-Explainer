# explainer_pipeline.py
from fast_api import get_modal_response

def multiline_input(prompt="Enter code (type 'END' on a new line to finish):\n") -> str:
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

if __name__ == "__main__":
    user_code = multiline_input()
    print("\n🧠 Sending to Modal Labs model...")
    modal_output = get_modal_response(user_code)
    print("\n✅ Explanation:\n", modal_output)
