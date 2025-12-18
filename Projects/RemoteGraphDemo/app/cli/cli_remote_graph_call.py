import logging
from app.cli.service_remote_graph import call_joke_endpoint

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def _get_joke(topic: str):
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
        logging.error(f"Error: {e}")

if __name__ == '__main__':
    while True:
        try:
            topic = input("Enter Topic > ").strip()
            if not topic or topic.lower() in {"exit", "quit", "bye"}:
                break
            _get_joke(topic=topic)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            print("Sorry, an error occurred. Please try again.")