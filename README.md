# Code Explainer

##  Overview
Code Explainer is an AI-powered tool that takes source code as input and generates human-readable explanations.  
It helps beginners and developers understand unfamiliar code quickly.  
The backend is powered by **StarCoder2-15B** deployed on **Modal Labs**.

---

## 🛠 Tech Stack
- **Python** – Core application
- **Modal Labs** – Model hosting & API
- **Transformers (Hugging Face)** – Model loading
- **Torch** – Deep learning framework

---
Execution :

Deploy the Model on Modal Labs

First, we need to host our StarCoder2 model on Modal Labs using the starcoder_reviewer.py script.

This script:

Creates a Modal app.

Loads the bigcode/starcoder2-15b model from Hugging Face.

Sets up an API endpoint so we can send code and get explanations back.

Set Up the Backend API

Once deployed, Modal gives us an endpoint URL like:

php-template
Copy
Edit
https://<your-app-name>--<function-name>.modal.run
This API will accept POST requests with code and return AI-generated explanations.

Run the Explainer Pipeline

The explainer_pipeline.py file is our client-side script.

It:

Reads code from a file or user input.

Sends the code to our Modal API endpoint.

Receives and displays the AI-generated explanation.

Testing with Example Code

We can test the pipeline by:

Providing a small C, C++, Python, or Java snippet.

Example:

c
Copy
Edit
#include <stdio.h>
int main() {
    printf("Hello, World!\n");
    return 0;
}
The API should return an explanation of what the code does.

End-to-End Flow

Step 1: Start Modal app → Model loads → API is ready.

Step 2: Client script sends code → Model processes it.

Step 3: Response (explanation) is shown to the user.
