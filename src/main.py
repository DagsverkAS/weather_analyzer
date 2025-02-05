"""
Weather Data Analyzer - Main Module
This module serves as the entry point for the weather data analyzer application.
"""
from utils.weather_api import get_weather_data

def main():
    """Main function to run the weather analyzer."""
    try:
        # Example location (will be configurable later)
        location = "Oslo, Norway"
        weather_data = get_weather_data(location)
        print(f"Weather data for {location}:")
        print(weather_data)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()