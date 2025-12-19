from langchain_community.document_loaders import Docx2txtLoader
import logging
from pathlib import Path

def get_docx_content(filePath: str) -> str:
    try:
        loader = Docx2txtLoader(filePath)
        docs = loader.load()
        logging.info(f"Loaded {len(docs)} documents from {filePath}")
        text = " ".join([doc.page_content for doc in docs])
        return text
    except Exception as e:
        logging.error(f"Error loading DOCX: {e}")
        return ""

if __name__ == "__main__":
    print("Testing DOCX Loader...")