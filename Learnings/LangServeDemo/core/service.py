import os
import logging
import time
from langserve import RemoteRunnable
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("HOST", "localhost")
port = int(os.getenv("PORT", "8000"))


def call_joke_endpoint(topic: str) -> (str | None):
    server_url = f"http://{host}:{port}/joke-generator/"
    logging.info(f"Connecting to server: {server_url}")

    remote_chain = RemoteRunnable(server_url)
    
    logging.info(f"Requesting joke for topic: {topic}")

    # Invoke the remote chain
    start_time = time.time()
    try:
        response = remote_chain.invoke({"topic": topic})
        duration = time.time() - start_time
        logging.info(f"Request completed successfully in {duration:.2f}s")
        
        return response
    
    except Exception as e:
        duration = time.time() - start_time
        logging.error(f"Request failed after {duration:.2f}s")
        logging.error(f"Error: {e}")
        return None