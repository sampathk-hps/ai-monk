# Use LangServe with LangGraph
# LangGraph introduced with Type-Safety

from servers.state.joke_state import JokeState
from servers.schema.joke_input import JokeInput
from servers.nodes.process_joke_node import process_joke

from langgraph.graph import StateGraph, START, END

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from langserve import add_routes
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create LangGraph graph
def _create_joke_graph():
    try:

        # Create the workflow graph
        graph = StateGraph(JokeState)

        graph.add_node("generate_joke", process_joke)
        
        graph.add_edge(START, "generate_joke")
        graph.add_edge("generate_joke", END)
        
        compiled_graph = graph.compile()
        logger.info("LangGraph compiled successfully")
        return compiled_graph
    
    except Exception as e:
        logger.error(f"Failed to create graph: {str(e)}")
        raise RuntimeError(f"Graph initialization failed: {str(e)}")

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
            "joke_generator/invoke": "/joke-generator",
        }
    }

# Initialize and register the graph
_joke_graph = _create_joke_graph()

# register the routes on langserve
add_routes(
    app = app,
    runnable = _joke_graph,
    path="/joke-generator",
    input_type=JokeInput,
)

if __name__ == "__main__":
    import uvicorn

    host = os.getenv("HOST", "localhost")
    port = int(os.getenv("PORT", "8000"))
    print(f"Starting the Joke Generator API server on {host}:{port}...")

    uvicorn.run(app, host=host, port=port)
