from pydantic import BaseModel, Field

class ValidationResult(BaseModel):
    """Output from the Quality Assurance Node."""
    accuracy_score: float = Field(description="0.0 to 1.0 score based on match with expected results")
    match_reasoning: str = Field(description="Explanation of why the score was given")
