from core.llm import get_llm
from constants.constants import PROMPT_DIR

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from langserve import add_routes
import logging
import re
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load prompt
with open(PROMPT_DIR, 'r') as f:
    template_content = f.read()
system_prompt = template_content

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "Topic: {topic}")
])

parser = StrOutputParser()

# Request validator
def validate_topic(inputs):
    topic = inputs.get("topic", "").strip()
    if not topic:
        raise HTTPException(status_code=400, detail="Topic cannot be empty")
    if len(topic) > 100:
        raise HTTPException(status_code=400, detail="Topic must be 100 characters or less")
    if not re.match(r'^[a-zA-Z0-9\s\-_.,!?]+$', topic):
        raise HTTPException(status_code=400, detail="Topic contains invalid characters")
    return inputs

# Create Chain
try:
    llm = get_llm()
    chain = RunnableLambda(validate_topic) | prompt_template | llm | parser
    logger.info("LLM chain initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize LLM: {str(e)}")
    raise RuntimeError(f"LLM initialization failed: {str(e)}")

# Create FastAPI app
app = FastAPI(
    title="Joke Generator API",
    version="1.0",
    description="A simple demo API using LangChain and LangServe to generate the jokes about a given topic",
)

# Add exception handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

# Add endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to the Joke Generator API",
        "endpoints": {
            "joke_generator": "/joke-generator",
        }
    }

# register the routes on langserve
add_routes(
    app,
    chain,
    path="/joke-generator",
)

if __name__ == "__main__":
    import uvicorn

    host = os.getenv("HOST", "localhost")
    port = int(os.getenv("PORT", "8000"))
    print(f"Starting the Joke Generator API server on {host}:{port}...")

    uvicorn.run(app, host=host, port=port)
