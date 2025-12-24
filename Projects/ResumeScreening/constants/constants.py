from pathlib import Path

MODEL = "meta/llama-3.1-405b-instruct"
EMBED_MODEL = "nvidia/llama-3.2-nemoretriever-1b-vlm-embed-v1"

CHROMA_COLLECTION_NAME = "resume_screening"

ROOT_DIR = Path(__file__).resolve().parents[1]

PROMPT_DIR = ROOT_DIR / "prompts" / "system.md"
PROMPT_QUERY_DIR = ROOT_DIR / "prompts" / "query.md"
VECTOR_STORE_DIR = ROOT_DIR / "vector_store"
