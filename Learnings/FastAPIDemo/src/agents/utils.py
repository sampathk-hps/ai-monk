from typing import Any


def extract_structured_response(result: dict[str, Any]) -> str:
    """
    Extract structured response from agent result.
    Handles different formats from various LLM providers.
    """
    structured_response = result.get('structured_response')
    
    if structured_response is None:
        return ""
    
    # If it's already a ResponseFormat object (Pydantic model)
    if hasattr(structured_response, 'punny_response'):
        return structured_response.punny_response
    
    # If it's a dict with punny_response
    if isinstance(structured_response, dict):
        return str(structured_response.get('punny_response', ''))
    
    # If it's a list (Gemini format)
    if isinstance(structured_response, list) and structured_response:
        content = "".join(
            c.get("text", "") if isinstance(c, dict) else str(c)
            for c in structured_response
        )
        return content
    
    # Fallback: convert to string
    return str(structured_response)
