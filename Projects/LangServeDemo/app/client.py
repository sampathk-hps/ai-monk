
import argparse
import os
import logging
import time
from langserve import RemoteRunnable

from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Joke Generator Client')
    parser.add_argument('--topic', type=str, default='Artificial_Intelligence',
                       help='Topic to generate a joke about')
    args = parser.parse_args()
    
    # Connect to the remote server
    try:
        host = os.getenv("HOST", "localhost")
        port = int(os.getenv("PORT", "8000"))
    except ValueError as e:
        logger.error(f"Invalid PORT environment variable: {e}")
        return
    
    server_url = f"http://{host}:{port}/joke-generator/"
    logger.info(f"Connecting to server: {server_url}")
    
    remote_chain = RemoteRunnable(server_url)
    
    logger.info(f"Requesting joke for topic: {args.topic}")
    
    # Invoke the remote chain
    start_time = time.time()
    try:
        response = remote_chain.invoke({"topic": args.topic})
        duration = time.time() - start_time
        logger.info(f"Request completed successfully in {duration:.2f}s")
        
        print("\nJoke Response:")
        print("-" * 40)
        print(response)
        print("-" * 40)
        
    except Exception as e:
        duration = time.time() - start_time
        logger.error(f"Request failed after {duration:.2f}s: {e}")
        logger.error(f"Make sure server is running on {server_url}")

if __name__ == "__main__":
    main()
