from core.llm import get_llm
from state.agent_state import AgentState
from schema.validation import ValidationResult
from core.csv_loader import get_expected_data
from prompts.validation import VALIDATION_PROMPT

import logging

_llm = get_llm()
_expected_db = get_expected_data()

def validation_node(state: AgentState):
    item = state["current_item"]
    gen_cls = state["classification"]
    gen_ana = state["analysis"]
    
    source_id = item.source_id
    
    # Fetch expected data
    expected_row = _expected_db.get(source_id)
    
    if not expected_row:
        # If no ground truth exists for this ID, skip validation or give neutral score
        return {"validation": {"accuracy_score": -1.0, "match_reasoning": "No ground truth found"}}

    # Construct Prompt
    prompt = VALIDATION_PROMPT.format(
        source_id=source_id,
        gen_category=gen_cls.get("category"),
        gen_priority=gen_ana.get("priority"),
        exp_category=expected_row.get("category"),
        exp_priority=expected_row.get("priority")
    )
    
    structured_llm = _llm.with_structured_output(ValidationResult)
    result = structured_llm.invoke(prompt)

    logging.info(f"Validation Result for source_id {source_id}: {result}")

    return {"validation": result if isinstance(result, dict) else result.model_dump()}
