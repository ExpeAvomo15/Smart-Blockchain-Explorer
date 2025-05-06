import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEBULA_API_KEY")
BASE_URL = "https://nebula-api.thirdweb.com"

HEADERS = {
    "x-secret-key": API_KEY,
    "Content-Type": "application/json"
}

def ask_question(message, chain_id=None, contract_address=None, modo_corto=False):
    if modo_corto:
        message += " Responde en menos de 200 caracteres. No hagas preguntas."

    body = {
        "message": message,
        "user_id": "default-user",
        "stream": False
    }

    if chain_id and contract_address:
        body["context"] = {
            "chain_ids": [chain_id],
            "contract_addresses": [contract_address]
        }

    res = requests.post(f"{BASE_URL}/chat", json=body, headers=HEADERS)

    try:
        data = res.json()
    except Exception:
        raise ValueError(f"No se pudo interpretar la respuesta JSON: {res.text}")

    if res.status_code == 200:
        if "response" in data:
            return data["response"]
        elif "message" in data:
            return data["message"]
        else:
            return f"Respuesta inesperada: {data}"
    else:
        raise ValueError(f"Error en la respuesta de la API: {data}")
