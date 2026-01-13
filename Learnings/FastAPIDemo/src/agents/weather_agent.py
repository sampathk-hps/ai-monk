from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langgraph.checkpoint.memory import InMemorySaver

from core.llm import get_llm_model
from prompts import get_system_prompt
from tools import get_weather, get_user_location
from models.response_format import ResponseFormat


llm = get_llm_model()

checkpointer = InMemorySaver()

weather_agent = create_agent(
    model=llm,
    tools=[get_weather, get_user_location],
    system_prompt=get_system_prompt(),
    response_format=ToolStrategy(ResponseFormat),
    checkpointer=checkpointer
)

def _run():
    from langchain_core.runnables.config import RunnableConfig
    from models.context import Context

    config: RunnableConfig = {
        "configurable": {
            "thread_id": "3"
        }
    }
    result = weather_agent.invoke({
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
    print(result['structured_response'])
    print("\n======")

    print("\n=== All Messages ===")
    for msg in result["messages"]:
        print(f"\n{msg}")
        print("\n======")
    
    print("\n=== Tool Calls Only ===")
    for msg in result["messages"]:
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            print(f"\n{msg.tool_calls}")

if __name__ == "__main__":
    result = _run()
    
    