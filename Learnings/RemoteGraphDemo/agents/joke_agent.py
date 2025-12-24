from state.joke_state import JokeState
from nodes.process_joke_node import process_joke

from langgraph.graph import StateGraph, START, END

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Build the graph
builder = StateGraph(JokeState)
builder.add_node("generate_joke", process_joke)
builder.add_edge(START, "generate_joke")
builder.add_edge("generate_joke", END)
graph = builder.compile()