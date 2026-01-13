from fastapi import APIRouter
from .models import ChatRequest, ChatResponse
from agents import weather_agent

from langchain_core.runnables.config import RunnableConfig
from models.context import Context

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_router(
    request: ChatRequest,
):
    """
    Chat with the weather agent.
    """

    config: RunnableConfig = {
        "configurable": {
            "thread_id": request.thread_id
        }
    }

    result = weather_agent.invoke(
        {"messages":[{"role":"user","content":request.message}]},
        config=config,
        context=Context(user_id=request.user_id)
    )
    # final_message = result["messages"][-1]
    
    # Handle Gemini's list-style content

    content = result['structured_response']
    if isinstance(content, list) and content:
        content = "".join(
            c.get("text", "") if isinstance(c, dict) else str(c) 
            for c in content
        )
    
    return ChatResponse(
        response=str(content),
        thread_id=request.thread_id
    )
