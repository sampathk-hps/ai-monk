from fastapi import APIRouter
from .models import ChatRequest, ChatResponse
from agents import get_weather_agent
from agents.utils import extract_structured_response

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
    agent = await get_weather_agent()

    config: RunnableConfig = {
        "configurable": {
            "thread_id": request.thread_id
        }
    }

    result = await agent.ainvoke(
        {"messages":[{"role":"user","content":request.message}]},
        config=config,
        context=Context(user_id=request.user_id)
    )
    
    content = extract_structured_response(result)
    
    return ChatResponse(
        response=content,
        thread_id=request.thread_id
    )
