from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    """
    Get weather for indian city.
    
    :param city: Description
    :type city: str
    :return: Description
    :rtype: str
    """

    return f"It's always rainy in {city}!"