import requests


def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org")
        response.raise_for_status()
        return response.text
    except Exception:
        return None
