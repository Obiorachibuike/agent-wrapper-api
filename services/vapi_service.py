import httpx
import os

VAPI_API_TOKEN = os.getenv("VAPI_API_TOKEN")  # Make sure to rename in .env
VAPI_URL = "https://api.vapi.ai/v1/assistants"

async def create_vapi_agent(data: dict):
    payload = {
        "name": data["name"],
        "description": data.get("description", ""),
        "voice": data.get("voice", "echo")
    }
    headers = {
        "Authorization": f"Token {VAPI_API_TOKEN}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(VAPI_URL, json=payload, headers=headers)
        return response.json()
