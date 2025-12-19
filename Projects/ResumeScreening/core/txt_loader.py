from langchain_community.document_loaders import TextLoader
import logging
from pathlib import Path

def get_txt_content(filePath: str) -> str:
    try:
        loader = TextLoader(filePath)
        docs = loader.load()
        logging.info(f"Loaded {len(docs)} documents from {filePath}")
        text = " ".join([doc.page_content for doc in docs])
        return text
    except Exception as e:
        logging.error(f"Error loading TXT: {e}")
        return ""

if __name__ == "__main__":
    print("Testing TXT Loader...")