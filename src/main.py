"""
Weather Data Analyzer - Main Module
This module serves as the entry point for the weather data analyzer application.
"""
from utils.weather_api import WeatherAPI, WeatherAPIError

def display_current_weather(weather_data: dict):
    """Display current weather information."""
    print("\nCURRENT WEATHER:")
    print("=" * 50)
    print(f"Location: {weather_data['location']}")
    print(f"Temperature: {weather_data['temperature']}°C")
    print(f"Feels like: {weather_data['feels_like']}°C")
    print(f"Condition: {weather_data['weather_condition']}")
    print(f"Description: {weather_data['description']}")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Wind Speed: {weather_data['wind_speed']} m/s")
    print(f"Pressure: {weather_data['pressure']} hPa")

def display_forecast(forecast_data: list):
    """Display weather forecast information."""
    print("\nWEATHER FORECAST:")
    print("=" * 50)
    
    for day in forecast_data:
        print(f"\nDate: {day['date']}")
        print("-" * 30)
        print(f"Temperature range: {day['temp_min']:.1f}°C to {day['temp_max']:.1f}°C")
        print(f"Average temperature: {day['temp_avg']:.1f}°C")
        print(f"Average humidity: {day['humidity_avg']:.1f}%")
        print(f"Average wind speed: {day['wind_speed_avg']:.1f} m/s")
        print(f"Max precipitation probability: {day['precipitation_prob_max']:.1f}%")
        print(f"Most common condition: {day['most_common_condition']}")
        
        print("\nDetailed forecast:")
        for detail in day['detailed_forecasts']:
            print(f"  {detail['time']}: {detail['temp']:.1f}°C, "
                  f"{detail['description']}, "
                  f"Rain: {detail['rain_prob']:.0f}%")

def main():
    """Main function to run the weather analyzer."""
    try:
        # Initialize the Weather API
        weather_api = WeatherAPI()
        
        # Example location (will be configurable later)
        location = "Oslo, NO"
        
        # Get current weather
        weather_data = weather_api.get_weather_data(location)
        display_current_weather(weather_data)
        
        # Get 5-day forecast
        forecast_data = weather_api.get_forecast(location, days=5)
        display_forecast(forecast_data)
        
    except WeatherAPIError as e:
        print(f"Weather API Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()