from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="User message")
    thread_id: str = Field(..., description="Conversation thread ID")

class ChatResponse(BaseModel):
    response: str
    thread_id: str
