# fast_api.py
import requests

MODAL_ENDPOINT = "https://saraswatshivansh78--code-explainer-starcoder-explain-code-api.modal.run"

def get_modal_response(user_code: str) -> str:
    payload = {"code": user_code}
    try:
        response = requests.post(MODAL_ENDPOINT, json=payload)
        response.raise_for_status()
        return response.json().get("explanation", "[No explanation found]")
    except requests.exceptions.RequestException as e:
        return f"[Modal API Error] {str(e)}"
