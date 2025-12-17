from constants.constants import MODEL

from dotenv import load_dotenv

from langchain_nvidia_ai_endpoints import ChatNVIDIA
import logging

load_dotenv()

_llm = ChatNVIDIA(model=MODEL, temperature=0.2, verbose=True)

def get_llm():
    return _llm

if __name__ == "__main__":
    try:
        response = _llm.invoke("Who are you?")
        print(response.content)
    except Exception as e:
        logging.error(f"Error invoking LLM: {e}")
