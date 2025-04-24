from fastapi import FastAPI, HTTPException
from models.agent import AgentRequest
from services.vapi_service import create_vapi_agent
from services.retell_service import create_retell_agent

app = FastAPI(title="AI Agent Wrapper API")

@app.post("/create-agent")
async def create_agent(agent: AgentRequest):
    if agent.provider.lower() == "vapi":
        result = await create_vapi_agent(agent.dict())
    elif agent.provider.lower() == "retell":
        result = await create_retell_agent(agent.dict())
    else:
        raise HTTPException(status_code=400, detail="Invalid provider. Choose either 'vapi' or 'retell'.")
    
    return result
