from constants.constants import VECTOR_STORE_DIR, CHROMA_COLLECTION_NAME
from core.embeddings import get_embeddings

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
import logging

logging.basicConfig(level=logging.INFO)

_vector_store = Chroma(
    collection_name=CHROMA_COLLECTION_NAME,
    persist_directory=str(VECTOR_STORE_DIR),
    embedding_function=get_embeddings()
)

def get_vector_store() -> Chroma:
    """
    Retrieve the Chroma vector store instance.
    Returns:
        Chroma: The Chroma vector store instance.
    """
    return _vector_store

# Text splitting
def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.create_documents([text])

# Store resume analysis in vector store
def store_content(content, doc_id):
    documents = split_text(content)
    _vector_store.add_documents(documents, ids=[f"{doc_id}_chunk_{i}" for i in range(len(documents))])

def query_analysis(query, k=3):
    return _vector_store.similarity_search(query, k=k)


if __name__ == "__main__":
    vs = get_vector_store()
    print(f"Vectore Store ID: {id(vs)}")