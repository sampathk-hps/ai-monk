import os
import logging
import time
from dotenv import load_dotenv
from langgraph.pregel.remote import RemoteGraph

load_dotenv()

host = os.getenv("HOST", "127.0.0.1")
port = int(os.getenv("PORT", "2024"))


def call_joke_endpoint(topic: str) -> (str | None):
    # RemoteGraph connects to the deployment server, NOT a specific graph endpoint
    server_url = f"http://{host}:{port}"
    logging.info(f"Connecting to server: {server_url}")

    # Initialize RemoteGraph with the graph name from your langgraph.json
    remote_graph = RemoteGraph("joke_generator", url=server_url)
    
    logging.info(f"Requesting joke for topic: {topic}")

    # Invoke the remote graph
    start_time = time.time()
    try:
        response = remote_graph.invoke({"topic": topic})
        duration = time.time() - start_time
        logging.info(f"Request completed successfully in {duration:.2f}s")
        
        return response.get('result')
    
    except Exception as e:
        duration = time.time() - start_time
        logging.error(f"Request failed after {duration:.2f}s")
        logging.error(f"Error: {e}")
        return None
    
if __name__ == "__main__":
    print("This cannot be called directly")
    print("Use: uv run python -m app.cli.cli_remote_graph_call")
