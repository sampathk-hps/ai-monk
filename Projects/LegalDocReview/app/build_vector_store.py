from core.pdf_loader import get_docs
from core.embeddings import get_embeddings
from constants.constants import FAISS_DIR

from typing import List
from pathlib import Path
import logging

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

# Create splitter with chunk size and overlap
_text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

_embeddings = get_embeddings()

def _load_documents() -> List[Document]:
    updated_docs: list[Document] = []
    
    docs = get_docs()

    # Handle the case where no documents are found
    if not docs:
        logging.error("No documents found.")
        return []
    
    split_docs = _text_splitter.split_documents(docs)
    logging.info(f"Split into {len(split_docs)} chunks of text.")

    for i, doc in enumerate(split_docs):
        doc.metadata["chunk_id"] = i
        file_name = Path(doc.metadata.get("source", "Unknown")).name
        doc.metadata["file_name"] = file_name
        updated_docs.append(doc)
    
    return updated_docs

def build_faiss(docs: List[Document]):
    logging.basicConfig(level=logging.INFO)
    FAISS_DIR.mkdir(parents=True, exist_ok=True)
    vector_store = FAISS.from_documents(docs, _embeddings)
    vector_store.save_local(str(FAISS_DIR))
    logging.info(f"Saved FAISS index at: {FAISS_DIR.resolve()}")

if __name__ == "__main__":
    docs = _load_documents()
    if not docs:
        logging.error("No docs found in data directory.")
        raise SystemExit(1)
    build_faiss(docs)
