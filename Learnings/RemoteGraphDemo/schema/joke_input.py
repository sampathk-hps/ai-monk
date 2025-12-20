from pydantic import BaseModel, Field

# Define input schema with validation
class JokeInput(BaseModel):
    topic: str = Field(..., description="Topic for the joke (required)", max_length=100)
