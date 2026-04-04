import os
from dotenv import load_dotenv
from .factory import LLMFactory
from .base import BaseLLMProvider
import logging
from constants.constants import DEFAULT_LLM_PROVIDER, DEFAULT_LLM_MODEL, DEFAULT_LLM_TEMPERATURE, DEFAULT_OLLAMA_BASE_URL

load_dotenv()

# Configuration from environment
LLM_PROVIDER = os.getenv("LLM_PROVIDER", DEFAULT_LLM_PROVIDER)
LLM_MODEL = os.getenv("LLM_MODEL", DEFAULT_LLM_MODEL)
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", DEFAULT_LLM_TEMPERATURE))
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", DEFAULT_OLLAMA_BASE_URL)

_llm: BaseLLMProvider | None = None

def get_llm() -> BaseLLMProvider:
    """Get or create LLM instance"""
    global _llm
    if _llm is None:
        kwargs = {}
        if LLM_PROVIDER == "ollama":
            kwargs["base_url"] = OLLAMA_BASE_URL
        
        _llm = LLMFactory.create(
            provider=LLM_PROVIDER,
            model=LLM_MODEL,
            temperature=LLM_TEMPERATURE,
            **kwargs
        )
    return _llm

def get_llm_model():
    """Get LLM model"""
    return get_llm().get_model()

def _run():
    try:
        llm = get_llm()
        for chunk in llm.stream_generate("Who are you?"):
            print(chunk, end="", flush=True)
        print()
        
        # response = llm.generate("Who are you?")
        # print(response)
    except Exception as e:
        logging.error(f"Error invoking LLM: {e}")

if __name__ == "__main__":
    _run()
