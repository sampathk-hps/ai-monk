from state.agent_state import AgentState
from schema.ticket import ProcessedTicket

def ticket_creator_node(state: AgentState):
    """Combines data into final ticket format."""
    item = state["current_item"]
    cls = state["classification"]
    ana = state["analysis"]
    val = state.get("validation", {}) # Get validation with default fallback
    
    ticket = ProcessedTicket(
        ticket_id=f"TKT-{item.source_id}",
        source_id=item.source_id,
        source_type=item.source_type,
        category=cls["category"],
        priority=ana["priority"],
        title=ana["suggested_title"],
        description=item.text_content,
        technical_details=ana.get("technical_details", ""),
        accuracy_score=val.get("accuracy_score", 0.0),
        accuracy_reasoning=val.get("match_reasoning", "N/A")
    )
    
    return {"final_ticket": ticket}
