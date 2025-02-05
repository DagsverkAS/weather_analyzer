"""
Weather API Module
Handles all interactions with the OpenWeatherMap API service.
"""
import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class WeatherAPIError(Exception):
    """Custom exception for weather API related errors."""
    pass

class WeatherAPI:
    """Handler for OpenWeatherMap API interactions."""
    
    def __init__(self):
        """Initialize the WeatherAPI with configuration."""
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.base_url = os.getenv('OPENWEATHER_BASE_URL', 
                                'https://api.openweathermap.org/data/2.5')
        
        if not self.api_key:
            raise WeatherAPIError("API key not found. Please set OPENWEATHER_API_KEY in .env file")

    def get_weather_data(self, location: str) -> Dict[str, Any]:
        """
        Fetch current weather data for a given location.
        
        Args:
            location (str): City name (e.g., "Oslo, NO")
            
        Returns:
            dict: Processed weather data
            
        Raises:
            WeatherAPIError: If API request fails or returns invalid data
        """
        try:
            # Construct the API URL for current weather
            url = f"{self.base_url}/weather"
            params = {
                'q': location,
                'appid': self.api_key,
                'units': 'metric'  # Use metric units
            }
            
            # Make the API request
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise exception for bad status codes
            
            # Parse the response
            data = response.json()
            
            # Extract and structure the relevant information
            weather_data = {
                'location': location,
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'weather_condition': data['weather'][0]['main'],
                'description': data['weather'][0]['description'],
                'wind_speed': data['wind']['speed']
            }
            
            return weather_data
            
        except requests.exceptions.RequestException as e:
            raise WeatherAPIError(f"Failed to fetch weather data: {str(e)}")
        except (KeyError, ValueError) as e:
            raise WeatherAPIError(f"Failed to parse weather data: {str(e)}")
    
    def get_forecast(self, location: str, days: int = 5) -> Dict[str, Any]:
        """
        Fetch weather forecast for a given location.
        
        Args:
            location (str): City name (e.g., "Oslo, NO")
            days (int): Number of days to forecast (max 5 for free tier)
            
        Returns:
            dict: Forecast data
            
        Raises:
            WeatherAPIError: If API request fails or returns invalid data
        """
        # This will be implemented in the next iteration
        raise NotImplementedError("Forecast functionality coming soon")