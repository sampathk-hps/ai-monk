from constants.constants import FAISS_DIR
from core.embeddings import get_embeddings

from typing import List
import logging

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

def get_results(query: str, k: int = 2) -> List[Document]:
    try:
        embeddings = get_embeddings()
        
        # Check if FAISS directory exists
        if not FAISS_DIR.exists():
            logging.error(f"FAISS directory not found: {FAISS_DIR}")
            return []
        
        db = FAISS.load_local(str(FAISS_DIR), embeddings, allow_dangerous_deserialization=True)
        docs = db.similarity_search(query, k=k)
        
        logging.info(f"Found {len(docs)} results for vector search.")
        return docs
        
    except FileNotFoundError:
        logging.error(f"FAISS index files not found in {FAISS_DIR}")
        return []
    except Exception as e:
        logging.error(f"Error during vector search: {e}")
        return []

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    results = get_results("What is the purpose of the contract?")
    print("Found results from below file:")
    for result in results:
        print(result.metadata.get("file_name"))
