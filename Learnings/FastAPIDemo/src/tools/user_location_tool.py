from langchain.tools import tool, ToolRuntime

from models.context import Context

@tool
def get_user_location(runtime: ToolRuntime[Context] ) -> str:
    """
    A context-aware tool.
    It reads the user_id from runtime.context and returns the user's location. You can replace this with a real database or user profile lookup.

    :param runtime: The tool runtime context.
    :return: The user's location.
    :rtype: str
    """

    user_id = runtime.context.user_id
    # Simple rule: user_id "1" lives in Bangalore, others in Delhi.
    return "Bangalore" if user_id == "1" else "Delhi"