"""
Weather Data Analyzer - Main Module
This module serves as the entry point for the weather data analyzer application.
"""
from utils.weather_api import WeatherAPI, WeatherAPIError

def main():
    """Main function to run the weather analyzer."""
    try:
        # Initialize the Weather API
        weather_api = WeatherAPI()
        
        # Example location (will be configurable later)
        location = "Oslo, NO"
        
        # Get current weather
        weather_data = weather_api.get_weather_data(location)
        
        # Display the weather information
        print(f"\nCurrent weather in {location}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Feels like: {weather_data['feels_like']}°C")
        print(f"Condition: {weather_data['weather_condition']}")
        print(f"Description: {weather_data['description']}")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")
        print(f"Pressure: {weather_data['pressure']} hPa")
        
    except WeatherAPIError as e:
        print(f"Weather API Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()