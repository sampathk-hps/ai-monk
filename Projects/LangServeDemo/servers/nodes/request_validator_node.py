from servers.state.joke_state import JokeState

from langchain_core.runnables import RunnableLambda

import re

from fastapi import HTTPException

# Request validator
def _validate_topic(input: JokeState):
    topic = input.get("topic", "").strip()
    if not topic:
        raise HTTPException(status_code=400, detail="Topic cannot be empty")
    if len(topic) > 100:
        raise HTTPException(status_code=400, detail="Topic must be 100 characters or less")
    if not re.match(r'^[a-zA-Z0-9\s\-_.,!?]+$', topic):
        raise HTTPException(status_code=400, detail="Topic contains invalid characters")
    return input

def request_validator(req: JokeState):
    validator_node = RunnableLambda(_validate_topic)
    result = validator_node.invoke(req)
    return result

if __name__ == "__main__":
    from pprint import pprint
    pprint(request_validator({"topic": "dogs"}))