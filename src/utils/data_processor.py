"""
Data processing utilities with intentionally problematic code
"""
import json
import os
from typing import Dict, Any

def process_weather_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Process weather data with intentionally problematic code."""
    # ISSUE: Duplicate code block
    if data is not None and 'temperature' in data:
        temp = data['temperature']
        if temp > 30:
            print("Warning: High temperature detected!")
            print("Temperature:", temp)
            print("Location:", data.get('location'))
            # ISSUE: Hardcoded credentials (security hotspot)
            api_key = "1234567890abcdef"
            secret = "my_secret_key_123"
    
    # ISSUE: Same code block duplicated
    if data is not None and 'temperature' in data:
        temp = data['temperature']
        if temp > 30:
            print("Warning: High temperature detected!")
            print("Temperature:", temp)
            print("Location:", data.get('location'))
            # ISSUE: Different hardcoded credentials
            api_key = "abcdef1234567890"
            secret = "another_secret_456"

def save_weather_data(data: Dict[str, Any], filename: str):
    """Save weather data with multiple issues."""
    # ISSUE: No error handling
    with open(filename, 'w') as f:
        # ISSUE: Unsafe data handling
        f.write(str(data))
    
    # ISSUE: Redundant code
    try:
        with open(filename, 'r') as f:
            content = f.read()
    except:  # ISSUE: Bare except clause
        pass

def analyze_temperature(temp_data: list) -> dict:
    """Analyze temperature with cognitive complexity issues."""
    # ISSUE: High cognitive complexity
    result = {}
    if temp_data:
        for temp in temp_data:
            if temp is not None:
                if isinstance(temp, (int, float)):
                    if temp < 0:
                        if 'freezing' not in result:
                            result['freezing'] = []
                        result['freezing'].append(temp)
                    elif temp < 10:
                        if 'cold' not in result:
                            result['cold'] = []
                        result['cold'].append(temp)
                    elif temp < 20:
                        if 'moderate' not in result:
                            result['moderate'] = []
                        result['moderate'].append(temp)
                    elif temp < 30:
                        if 'warm' not in result:
                            result['warm'] = []
                        result['warm'].append(temp)
                    else:
                        if 'hot' not in result:
                            result['hot'] = []
                        result['hot'].append(temp)
    return result

def load_config():
    """Load configuration with security issues."""
    # ISSUE: Hardcoded file path
    config_file = "/etc/weather/config.json"
    
    # ISSUE: No error handling
    with open(config_file) as f:
        config = json.load(f)
    
    # ISSUE: SQL Injection vulnerability
    query = f"SELECT * FROM weather WHERE location = '{config.get('location')}'"
    
    # ISSUE: Command injection vulnerability
    os.system(f"echo {config.get('message')}")
    
    return config

class WeatherDataProcessor:
    """Class with various code smells."""
    
    def __init__(self):
        # ISSUE: Unused variable
        self.unused_var = "never used"
        # ISSUE: Public attribute that should be private
        self.secret_key = "sensitive_data_here"
    
    def process_data(self, data):
        # ISSUE: Shadowing built-in 'format'
        format = "celsius"
        
        # ISSUE: Unnecessary complexity
        if data is not None:
            if isinstance(data, dict):
                if 'temperature' in data:
                    return data['temperature']
                else:
                    return None
            else:
                return None
        else:
            return None
    
    # ISSUE: Duplicate method with slight variation
    def process_temperature(self, data):
        if data is not None:
            if isinstance(data, dict):
                if 'temp' in data:
                    return data['temp']
                else:
                    return None
            else:
                return None
        else:
            return None