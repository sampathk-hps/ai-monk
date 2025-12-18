from core.llm import get_llm
from constants.constants import PROMPT_DIR

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from fastapi import FastAPI
from langserve import add_routes
import logging
import re
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

with open(PROMPT_DIR, 'r') as f:
    template_content = f.read()
system_prompt = template_content

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "Topic: {topic}")
])

parser = StrOutputParser()

def validate_topic(inputs):
    topic = inputs.get("topic", "").strip()
    if not topic:
        raise ValueError("Topic cannot be empty")
    if len(topic) > 100:
        raise ValueError("Topic must be 100 characters or less")
    if not re.match(r'^[a-zA-Z0-9\s\-_.,!?]+$', topic):
        raise ValueError("Topic contains invalid characters")
    return inputs

try:
    llm = get_llm()
    chain = RunnableLambda(validate_topic) | prompt_template | llm | parser
    logger.info("LLM chain initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize LLM: {str(e)}")
    raise RuntimeError(f"LLM initialization failed: {str(e)}")

app = FastAPI(
    title="Joke Generator API",
    version="1.0",
    description="A simple demo API using LangChain and LangServe to generate the jokes about a given topic",
)

add_routes(
    app,
    chain,
    path="/joke-generator",
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Joke Generator API",
        "endpoints": {
            "joke_generator": "/joke-generator",
        }
    }

if __name__ == "__main__":
    import uvicorn

    host = os.getenv("HOST", "localhost")
    port = int(os.getenv("PORT", "8000"))
    print(f"Starting the Joke Generator API server on {host}:{port}...")

    uvicorn.run(app, host=host, port=port)
