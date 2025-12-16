from langchain_community.document_loaders import PyPDFDirectoryLoader
from pathlib import Path
from constants.constants import DATA_DIR

_loader = PyPDFDirectoryLoader(path=DATA_DIR)

def get_docs():
    try:
        docs = _loader.load()
        print(f"Loaded {len(docs)} documents from {DATA_DIR}")
        return docs
    except Exception as e:
        print(f"Error loading PDFs: {e}")
        print(f"Looking for PDFs in: {DATA_DIR}")
        print(f"Directory exists: {DATA_DIR.exists()}")

if __name__ == "__main__":
    print(f"Total pages: {len(_loader.load())}")
