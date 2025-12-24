from pydantic import BaseModel, Field
from typing import Literal, Optional

class TicketClassification(BaseModel):
    """Output from the Classifier Agent."""
    category: Literal["Bug", "Feature Request", "Praise", "Complaint", "Spam"]
    confidence_score: float

class TicketAnalysis(BaseModel):
    """Output from Analysis Agents (Bug/Feature)."""
    priority: Literal["Critical", "High", "Medium", "Low"]
    technical_details: Optional[str] = Field(description="Steps to reproduce or technical context")
    suggested_title: str
    user_impact_score: int = Field(description="1-10 scale of impact")

class ProcessedTicket(BaseModel):
    """Final Structure for generated_tickets.csv"""
    ticket_id: str
    source_id: str
    source_type: str
    category: str
    priority: str
    title: str
    description: str
    technical_details: str
    status: str = "Open"
    accuracy_score: Optional[float] = 0.0
    accuracy_reasoning: Optional[str] = ""
