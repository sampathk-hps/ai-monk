from core.llm import get_llm
from state.agent_state import AgentState
from schema.ticket import TicketClassification
from prompts.classifier import CLASSIFIER_PROMPT

import logging

_llm = get_llm()

def classifier_node(state: AgentState):
    """Classifies the feedback item."""
    item = state["current_item"]
    
    # Structured output enforcement
    structured_llm = _llm.with_structured_output(TicketClassification)
    
    response = structured_llm.invoke(
        CLASSIFIER_PROMPT.format(text=item.text_content)
    )
    
    logging.info(f"Classification: {response}")
    
    return {"classification": response if isinstance(response, dict) else response.model_dump()}
