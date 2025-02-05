"""
Tests for the weather API module.
"""
import os
import pytest
from datetime import datetime, timedelta
from unittest.mock import patch, Mock
from src.utils.weather_api import WeatherAPI, WeatherAPIError

@pytest.fixture
def weather_api():
    """Fixture to create a WeatherAPI instance with a mock API key."""
    with patch.dict(os.environ, {'OPENWEATHER_API_KEY': 'mock_api_key'}):
        return WeatherAPI()

def test_weather_api_initialization_without_key():
    """Test WeatherAPI initialization without API key."""
    with patch.dict(os.environ, {'OPENWEATHER_API_KEY': ''}, clear=True):
        with pytest.raises(WeatherAPIError):
            WeatherAPI()

def test_get_weather_data_success(weather_api):
    """Test successful weather data retrieval."""
    mock_response = Mock()
    mock_response.json.return_value = {
        'main': {
            'temp': 20.5,
            'feels_like': 19.8,
            'humidity': 65,
            'pressure': 1013
        },
        'weather': [{'main': 'Clear', 'description': 'clear sky'}],
        'wind': {'speed': 3.6}
    }
    
    with patch('requests.get', return_value=mock_response):
        data = weather_api.get_weather_data('Oslo, NO')
        
        assert isinstance(data, dict)
        assert data['temperature'] == 20.5
        assert data['weather_condition'] == 'Clear'
        assert data['humidity'] == 65

def test_get_weather_data_api_error(weather_api):
    """Test weather data retrieval with API error."""
    with patch('requests.get', side_effect=Exception('API Error')):
        with pytest.raises(WeatherAPIError):
            weather_api.get_weather_data('Invalid Location')

def test_get_forecast_success(weather_api):
    """Test successful forecast data retrieval."""
    # Create mock forecast data
    mock_response = Mock()
    base_time = datetime.now()
    mock_response.json.return_value = {
        'list': [
            {
                'dt': int((base_time + timedelta(hours=i*3)).timestamp()),
                'main': {
                    'temp': 20.0 + i,
                    'feels_like': 19.0 + i,
                    'humidity': 65
                },
                'weather': [{'main': 'Clear', 'description': 'clear sky'}],
                'wind': {'speed': 3.6},
                'pop': 0.2
            }
            for i in range(8)  # 24 hours of 3-hour forecasts
        ]
    }
    
    with patch('requests.get', return_value=mock_response):
        forecast = weather_api.get_forecast('Oslo, NO', days=1)
        
        assert isinstance(forecast, list)
        assert len(forecast) == 1  # One day requested
        
        day_forecast = forecast[0]
        assert 'date' in day_forecast
        assert 'temp_min' in day_forecast
        assert 'temp_max' in day_forecast
        assert 'temp_avg' in day_forecast
        assert 'detailed_forecasts' in day_forecast
        
        # Check temperature calculations
        assert day_forecast['temp_min'] == 20.0  # First temperature
        assert day_forecast['temp_max'] == 27.0  # Last temperature
        
def test_get_forecast_invalid_days(weather_api):
    """Test forecast retrieval with invalid days parameter."""
    with pytest.raises(ValueError):
        weather_api.get_forecast('Oslo, NO', days=6)
    
    with pytest.raises(ValueError):
        weather_api.get_forecast('Oslo, NO', days=0)