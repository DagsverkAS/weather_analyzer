"""
Weather API Module
Handles all interactions with the weather API service.
"""

def get_weather_data(location: str) -> dict:
    """
    Fetch weather data for a given location.
    
    Args:
        location (str): Name of the location (e.g., "Oslo, Norway")
        
    Returns:
        dict: Weather data for the specified location
        
    Raises:
        ValueError: If location is invalid
        ConnectionError: If API cannot be reached
    """
    # This is a placeholder - we'll implement actual API calls later
    # For now, return dummy data
    return {
        "location": location,
        "temperature": 20,
        "condition": "sunny",
        "humidity": 65
    }