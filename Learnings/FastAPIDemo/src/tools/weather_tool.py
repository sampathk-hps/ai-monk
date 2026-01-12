from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    """
    Get weather for a given city.
    
    :param city: Description
    :type city: str
    :return: Description
    :rtype: str
    """

    return f"It's always rainy in {city}!"