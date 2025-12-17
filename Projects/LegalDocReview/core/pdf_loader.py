from langchain_community.document_loaders import PyPDFDirectoryLoader
from constants.constants import DATA_DIR
import logging

_loader = PyPDFDirectoryLoader(path=DATA_DIR)

def get_docs():
    try:
        docs = _loader.load()
        logging.info(f"Loaded {len(docs)} documents from {DATA_DIR}")
        return docs
    except Exception as e:
        logging.error(f"Error loading PDFs: {e}")
        logging.error(f"Looking for PDFs in: {DATA_DIR}")
        logging.error(f"Directory exists: {DATA_DIR.exists()}")
        return []

if __name__ == "__main__":
    try:
        docs = get_docs()
        print(f"Total pages: {len(docs)}")
    except Exception as e:
        logging.error(f"Error in main: {e}")
