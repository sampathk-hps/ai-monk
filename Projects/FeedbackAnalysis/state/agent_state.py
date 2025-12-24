from typing import TypedDict, List, Dict, Any
from schema.feedback import FeedbackItem
from schema.ticket import ProcessedTicket

class AgentState(TypedDict):
    """The state of the graph execution."""
    raw_data: List[FeedbackItem]      # Normalized inputs
    current_item: FeedbackItem        # The item currently being processed in the loop
    classification: Dict[str, Any]    # Result from Classifier
    analysis: Dict[str, Any]          # Result from Bug/Feature agents
    validation: Dict[str, Any]        # Result from QA agent
    final_ticket: ProcessedTicket     # The generated ticket
    logs: List[str]                   # For processing_log.csv
