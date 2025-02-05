# Weather Data Analyzer

A Python application for analyzing weather data from various locations.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
pip install -e .
```

## Usage

Run the main application:
```bash
python src/main.py
```

Run tests:
```bash
python -m pytest tests/
```

## Project Structure

- `src/`: Source code
  - `main.py`: Entry point
  - `utils/`: Utility modules
    - `weather_api.py`: Weather API interactions
- `tests/`: Test files
- `docs/`: Documentation
