from constants.constants import FAISS_DIR
from core.embeddings import get_embeddings

from typing import List

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

def get_results(query, k=2) -> List[Document]:
    embeddings = get_embeddings()
    db = FAISS.load_local(str(FAISS_DIR), embeddings, allow_dangerous_deserialization=True)
    docs = db.similarity_search(query, k=k)
    print(f"Found {len(docs)} results for vector search.")
    return docs

if __name__ == "__main__":
    results = get_results("What is the purpose of the contract?")
    print("Found results from below file:")
    for result in results:
        print(result.metadata.get("file_name"))