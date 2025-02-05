"""
Tests for the weather API module.
"""
import os
import pytest
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
        assert data['temperature'] == pytest.approx(20.5, rel=1e-3)
        assert data['weather_condition'] == 'Clear'
        assert data['humidity'] == 65

def test_get_weather_data_api_error(weather_api):
    """Test weather data retrieval with API error."""
    with patch('requests.get', side_effect=Exception('API Error')):
        with pytest.raises(WeatherAPIError):
            weather_api.get_weather_data('Invalid Location')
