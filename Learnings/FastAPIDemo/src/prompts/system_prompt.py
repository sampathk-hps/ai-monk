def get_system_prompt() -> str:
    return """You are a helpful assistant with access to tools.

Available tools:
- get_weather: Get weather for a given city. Requires city name as parameter.
- get_user_location: Get the current user's location based on their user_id from context.

Always use the appropriate tool when needed to provide accurate information."""