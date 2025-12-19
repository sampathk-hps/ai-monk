from langchain_community.document_loaders import PyPDFLoader
import logging
from pathlib import Path

def get_pdf_content(filePath: str) -> str:
    try:
        loader = PyPDFLoader(filePath)
        docs = loader.load()
        logging.info(f"Loaded {len(docs)} documents from {filePath}")
        text = " ".join([doc.page_content for doc in docs])
        return text
    except Exception as e:
        logging.error(f"Error loading PDF: {e}")
        return ""

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sample_pdf_path = str(Path(__file__).parent.parent / "data" / "Resume1.pdf")
    content = get_pdf_content(sample_pdf_path)
    print(f"Extracted Content: {content[:500]}")
