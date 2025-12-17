from pathlib import Path

MODEL = "meta/llama-3.1-405b-instruct"
EMBED_MODEL = "nvidia/llama-3.2-nemoretriever-1b-vlm-embed-v1"

root_dir = Path(__file__).resolve().parents[1]
DATA_DIR = root_dir / "data"
FAISS_DIR = root_dir / "vector_stores"

PROMPT_DIR = root_dir / "prompts" / "generate.md"