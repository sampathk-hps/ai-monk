from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from constants.constants import MODEL

load_dotenv()

_llm = ChatNVIDIA(model=MODEL, verbose=True)

def get_llm():
    return _llm

if __name__ == "__main__":
    response = _llm.invoke("Who are you?")
    print(response.content)
