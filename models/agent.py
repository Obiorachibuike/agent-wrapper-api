from pydantic import BaseModel
from typing import Optional

class AgentRequest(BaseModel):
    name: str
    description: Optional[str] = None
    voice: Optional[str] = None
    provider: str  # "vapi" or "retell"
