
import argparse
import logging

from core.service import call_joke_endpoint

from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def _parse_topic() -> str:
    parser = argparse.ArgumentParser(description='Joke Generator Client')
    parser.add_argument('--topic', type=str, default='Artificial_Intelligence',
                        help='Topic to generate a joke about')
    args = parser.parse_args()
    return args.topic

def main():
    topic = _parse_topic()

    try:
        response = call_joke_endpoint(topic=topic)
        if response is None:
            print("Sorry, I couldn't generate a joke for that topic.")
            return
        
        print("\nJoke Response:")
        print("-" * 40)
        print(response)
        print("-" * 40)
        
    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()
