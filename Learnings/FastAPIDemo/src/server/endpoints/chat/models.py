from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="User message")
    thread_id: str = Field(..., description="Conversation thread ID")
    user_id: str = Field(..., description="User ID")

class ChatResponse(BaseModel):
    response: str
    thread_id: str
