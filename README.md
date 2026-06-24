# Code Explainer

##  Overview
Code Explainer is an AI-powered tool that takes source code as input and generates human-readable explanations.  
It helps beginners and developers understand unfamiliar code quickly.  
The backend is powered by **StarCoder2-15B** deployed on **Modal Labs**.

---

## Tech Stack
- **Python** – Core application
- **Modal Labs** – Model hosting & API
- **Transformers (Hugging Face)** – Model loading
- **Torch** – Deep learning framework

---
## Execution Steps

To run the **Code Explainer** project:

1. **Deploy Model on Modal Labs** – Use `starcoder_reviewer.py` to host the **StarCoder2-15B** model. This will:  
   - Create a Modal application.  
   - Load the `bigcode/starcoder2-15b` model from Hugging Face.  
   - Set up an API endpoint for sending code and receiving explanations.  

2. **Set Up Backend API** – Once deployed, Modal will provide an API endpoint (e.g., `https://<app-name>--<username>.modal.run`) that:  
   - Accepts **POST** requests containing source code.  
   - Returns AI-generated explanations.  

3. **Run Explainer Pipeline** – Use `explainer_pipeline.py` (client-side) to:  
   - Send code to the API endpoint.  
   - Receive and display explanations in a human-readable format. 
