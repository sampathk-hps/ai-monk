from core.pdf_loader import get_docs
from core.embeddings import get_embeddings
from constants.constants import FAISS_DIR

from typing import List

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

# Create splitter with chunk size and overlap
_text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

_embeddings = get_embeddings()

# vector_store = FAISS.from_documents(split_docs, embeddings)
# vector_store.save_local(FAISS_DIR)
# print(f"Vector store saved to {FAISS_DIR}")

# if __name__ == "__main__":
#     vector_store = FAISS.from_documents(split_docs, embeddings)
#     vector_store.save_local(FAISS_DIR)
#     print(f"Vector store saved to {FAISS_DIR}")


def _load_documents() -> List[Document]:
    updated_docs: list[Document] = []
    
    docs = get_docs()

    # Handle the case where no documents are found
    if not docs:
        print("No documents found.")
        return []
    
    split_docs = _text_splitter.split_documents(docs)
    print(f"Split into {len(split_docs)} chunks of text.")

    for i, doc in enumerate(split_docs):
        doc.metadata["chunk_id"] = i
        file_name = doc.metadata.get("source", "unknown").split("/")[-1]
        doc.metadata["file_name"] = file_name
        updated_docs.append(doc)
    
    return updated_docs

def build_faiss(docs: List[Document]):
    FAISS_DIR.mkdir(parents=True, exist_ok=True)
    vector_store = FAISS.from_documents(docs, _embeddings)
    vector_store.save_local(str(FAISS_DIR))
    print(f"Saved FAISS index at: {FAISS_DIR.resolve()}")

if __name__ == "__main__":
    docs = _load_documents()
    if len(docs) == 0 or not any(docs):
        raise SystemExit(f"No docs found in data directory.")
    build_faiss(docs)