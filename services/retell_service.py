import httpx
import os

RETELL_API_KEY = os.getenv("RETELL_API_KEY")
RETELL_URL = "https://api.retellai.com/agents"

async def create_retell_agent(data: dict):
    payload = {
        "agent_name": data["name"],
        "description": data.get("description", ""),
        "voice_id": data.get("voice", "11")  # default voice ID
    }
    headers = {
        "Authorization": f"Bearer {RETELL_API_KEY}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(RETELL_URL, json=payload, headers=headers)
        return response.json()
