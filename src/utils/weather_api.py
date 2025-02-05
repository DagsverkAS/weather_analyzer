"""
Weather API Module
Handles all interactions with the OpenWeatherMap API service.
"""
import os
import requests
from datetime import datetime
from typing import Dict, Any, List
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
            url = f"{self.base_url}/weather"
            params = {
                'q': location,
                'appid': self.api_key,
                'units': 'metric'
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
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
    
    def get_forecast(self, location: str, days: int = 5) -> List[Dict[str, Any]]:
        """
        Fetch weather forecast for a given location.
        
        Args:
            location (str): City name (e.g., "Oslo, NO")
            days (int): Number of days to forecast (max 5 for free tier)
            
        Returns:
            list: List of daily forecast data
            
        Raises:
            WeatherAPIError: If API request fails or returns invalid data
            ValueError: If days parameter is invalid
        """
        if not 1 <= days <= 5:
            raise ValueError("Days parameter must be between 1 and 5")
            
        try:
            # Get forecast data
            url = f"{self.base_url}/forecast"
            params = {
                'q': location,
                'appid': self.api_key,
                'units': 'metric'
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Process the forecast data
            forecasts = []
            current_day = None
            day_data = None
            
            for item in data['list']:
                # Convert timestamp to datetime
                timestamp = datetime.fromtimestamp(item['dt'])
                date = timestamp.date()
                
                # If we're starting a new day
                if date != current_day:
                    # Save the previous day's data if it exists
                    if day_data:
                        forecasts.append(self._process_day_data(day_data))
                        
                    # Start new day
                    current_day = date
                    day_data = {
                        'date': date.strftime('%Y-%m-%d'),
                        'temps': [],
                        'humidity': [],
                        'weather_conditions': [],
                        'wind_speeds': [],
                        'precipitation_prob': [],
                        'detailed_forecasts': []
                    }
                
                # Add the 3-hour forecast data
                temps = item['main']
                weather = item['weather'][0]
                
                day_data['temps'].append(temps['temp'])
                day_data['humidity'].append(temps['humidity'])
                day_data['weather_conditions'].append(weather['main'])
                day_data['wind_speeds'].append(item['wind']['speed'])
                
                # Add rain probability if available
                rain_prob = item.get('pop', 0) * 100  # Convert to percentage
                day_data['precipitation_prob'].append(rain_prob)
                
                # Store detailed forecast for this time
                detailed = {
                    'time': timestamp.strftime('%H:%M'),
                    'temp': temps['temp'],
                    'feels_like': temps['feels_like'],
                    'humidity': temps['humidity'],
                    'weather': weather['main'],
                    'description': weather['description'],
                    'wind_speed': item['wind']['speed'],
                    'rain_prob': rain_prob
                }
                day_data['detailed_forecasts'].append(detailed)
            
            # Add the last day's data
            if day_data:
                forecasts.append(self._process_day_data(day_data))
            
            # Return only the requested number of days
            return forecasts[:days]
            
        except requests.exceptions.RequestException as e:
            raise WeatherAPIError(f"Failed to fetch forecast data: {str(e)}")
        except (KeyError, ValueError) as e:
            raise WeatherAPIError(f"Failed to parse forecast data: {str(e)}")

    def _process_day_data(self, day_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process raw day data into a summary format.
        
        Args:
            day_data (dict): Raw data for one day
            
        Returns:
            dict: Processed day data with summary statistics
        """
        temps = day_data['temps']
        
        return {
            'date': day_data['date'],
            'temp_min': min(temps),
            'temp_max': max(temps),
            'temp_avg': sum(temps) / len(temps),
            'humidity_avg': sum(day_data['humidity']) / len(day_data['humidity']),
            'wind_speed_avg': sum(day_data['wind_speeds']) / len(day_data['wind_speeds']),
            'precipitation_prob_max': max(day_data['precipitation_prob']),
            'most_common_condition': max(set(day_data['weather_conditions']), 
                                      key=day_data['weather_conditions'].count),
            'detailed_forecasts': day_data['detailed_forecasts']
        }