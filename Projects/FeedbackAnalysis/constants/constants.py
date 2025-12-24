from pathlib import Path

MODEL = "meta/llama-3.1-405b-instruct"
EMBED_MODEL = "nvidia/llama-3.2-nemoretriever-1b-vlm-embed-v1"

ROOT_DIR = Path(__file__).resolve().parents[1]

PROMPT_DIR = ROOT_DIR / "prompts" / "system.md"
PROMPT_QUERY_DIR = ROOT_DIR / "prompts" / "query.md"

INPUT_REVIEWS_PATH = ROOT_DIR / "data" / "app_store_reviews.csv"
INPUT_EMAILS_PATH = ROOT_DIR / "data" / "support_emails.csv"
EXPECTED_CLASSIFICATIONS_PATH = ROOT_DIR / "data" / "expected_classifications.csv"

OUTPUT_TICKETS_PATH = ROOT_DIR / "results" / "generated_tickets.csv"
OUTPUT_LOGS_PATH = ROOT_DIR / "results" / "processing_log.csv"

# Classification Thresholds
CONFIDENCE_THRESHOLD = 0.7
