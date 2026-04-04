import asyncio
import logging
from threading import Lock

from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain.tools import BaseTool
from langgraph.checkpoint.memory import InMemorySaver

from core.llm import get_llm_model
from core.mcp.client import get_mcp_tools
from models.response_format import ResponseFormat
from prompts import get_system_prompt
from tools import get_weather, get_user_location
from .utils import extract_structured_response

logger = logging.getLogger(__name__)

_weather_agent = None
_lock = Lock()

async def get_weather_agent():
    """Get or create the weather agent with all tools loaded."""
    global _weather_agent
    
    if _weather_agent is None:
        with _lock:
            if _weather_agent is None:
                logger.info("Initializing weather agent with tools")
                mcp_tools = await get_mcp_tools()
                custom_tools = [get_weather, get_user_location]
                all_tools = custom_tools + mcp_tools
                
                _weather_agent = create_agent(
                    model=get_llm_model(),
                    tools=all_tools,
                    system_prompt=get_system_prompt(),
                    response_format=ToolStrategy(ResponseFormat),
                    checkpointer=InMemorySaver()
                )
                logger.info(f"Weather agent initialized with {len(all_tools)} tools")
    
    return _weather_agent

async def _run_async():
    from langchain_core.runnables.config import RunnableConfig
    from models.context import Context

    agent = await get_weather_agent()

    config: RunnableConfig = {
        "configurable": {
            "thread_id": "3"
        }
    }
    result = await agent.ainvoke({
        "messages": [
            {
                "role": "user",
                "content": "What is the weather in my location?"
            }
        ]
    },
    config=config,
    context=Context(user_id="2"))

    print("\n=== Structured Response ===")
    print(extract_structured_response(result))
    print("\n======")

    print("\n=== All Messages ===")
    for msg in result["messages"]:
        print(f"\n{msg}")
        print("\n======")
    
    print("\n=== Tool Calls Only ===")
    for msg in result["messages"]:
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            print(f"\n{msg.tool_calls}")

def _run():
    asyncio.run(_run_async())

if __name__ == "__main__":
    _run()
    
    