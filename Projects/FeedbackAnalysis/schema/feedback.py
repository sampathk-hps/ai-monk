from pydantic import BaseModel
from typing import Literal

class FeedbackItem(BaseModel):
    """Normalized input format for both emails and reviews."""
    source_id: str
    source_type: Literal["app_store", "support_email"]
    text_content: str
    metadata: dict  # Stores sender, platform, versions, etc.
