from langchain.agents import create_agent

from core.llm import get_llm_model
from prompts import get_system_prompt
from tools import get_weather

llm = get_llm_model()

weather_agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt=get_system_prompt(),
)

def _run():
    return weather_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": "What is the weather in Mangalore?"
            }
        ]
    })

if __name__ == "__main__":
    print(_run())