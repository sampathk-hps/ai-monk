from pathlib import Path

MODEL = "meta/llama-3.1-405b-instruct"
EMBED_MODEL = "nvidia/llama-3.2-nemoretriever-1b-vlm-embed-v1"

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
FAISS_DIR = ROOT_DIR / "vector_stores"

PROMPT_DIR = ROOT_DIR / "prompts" / "generate.md"