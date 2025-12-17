from constants.constants import EMBED_MODEL

from dotenv import load_dotenv

from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings

load_dotenv()

_embeddings = NVIDIAEmbeddings(model=EMBED_MODEL)

def get_embeddings():
    return _embeddings

if __name__ == "__main__":
        embed_list = _embeddings.embed_documents(["Hello", "World"])
        print(f"Sample Embedding: {embed_list[0][:10]}...")