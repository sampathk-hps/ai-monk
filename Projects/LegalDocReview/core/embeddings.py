from constants.constants import EMBED_MODEL

from dotenv import load_dotenv
import logging

from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings

load_dotenv()

_embeddings = NVIDIAEmbeddings(model=EMBED_MODEL)

def get_embeddings():
    return _embeddings

if __name__ == "__main__":
        logging.basicConfig(level=logging.INFO)
        embed_list = get_embeddings().embed_documents(["Hello", "World"])
        logging.info(f"Sample Embedding: {embed_list[0][:10]}...")
