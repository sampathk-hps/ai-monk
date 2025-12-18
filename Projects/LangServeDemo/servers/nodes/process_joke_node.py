from servers.state.joke_state import JokeState
from core.llm import get_llm
from constants.constants import PROMPT_DIR

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load prompt
with open(PROMPT_DIR, 'r') as f:
    template_content = f.read()
_system_prompt = template_content

_prompt_template = ChatPromptTemplate.from_messages([
    ("system", _system_prompt),
    ("user", "Topic: {topic}")
])

_parser = StrOutputParser()

# Add a single node that does all the work
def process_joke(state: JokeState,) -> JokeState:
    chain = _prompt_template | get_llm() | _parser
    result = chain.invoke({"topic": state["topic"]})
    return {"result": result}

if __name__ == "__main__":
    from pprint import pprint
    pprint(process_joke({"topic": "dogs"}))