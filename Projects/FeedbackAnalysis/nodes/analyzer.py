from core.llm import get_llm
from state.agent_state import AgentState
from schema.ticket import TicketAnalysis
from prompts.bug_analysis import BUG_ANALYSIS_PROMPT
from prompts.feature_analysis import FEATURE_ANALYSIS_PROMPT

import logging

_llm = get_llm()

def analyzer_node(state: AgentState):
    """Routes to specific analysis based on classification."""
    category = state["classification"]["category"]
    item = state["current_item"]
    
    structured_llm = _llm.with_structured_output(TicketAnalysis)
    
    if category == "Bug":
        prompt = BUG_ANALYSIS_PROMPT.format(
            text=item.text_content, metadata=item.metadata
        )
    elif category == "Feature Request":
        prompt = FEATURE_ANALYSIS_PROMPT.format(text=item.text_content)
    else:
        # Default handling for Spam/Praise (Lower priority, no deep analysis)
        return {"analysis": {
            "priority": "Low", 
            "technical_details": "N/A", 
            "suggested_title": f"{category}: {item.source_id}", 
            "user_impact_score": 0
        }}

    response = structured_llm.invoke(prompt)

    if response is None:
        response = {
            "priority": "Low", 
            "technical_details": "Analysis failed", 
            "suggested_title": f"{category}: {item.source_id}", 
            "user_impact_score": 1
        }

    logging.info(f"Analysis for category {category}: {response}")
    
    return {"analysis": response if isinstance(response, dict) else response.model_dump()}

