"""
Tests for the weather API module.
"""
import unittest
from src.utils.weather_api import get_weather_data

class TestWeatherAPI(unittest.TestCase):
    def test_get_weather_data(self):
        """Test basic weather data retrieval."""
        location = "Oslo, Norway"
        data = get_weather_data(location)
        
        # Basic structure tests
        self.assertIsInstance(data, dict)
        self.assertEqual(data["location"], location)
        self.assertIn("temperature", data)
        self.assertIn("condition", data)
        self.assertIn("humidity", data)