from setuptools import setup, find_packages

setup(
    name="weather_analyzer",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
    ],
    python_requires=">=3.7",
    author="Uno Vaaland",
    description="A weather data analysis tool",
    keywords="weather, analysis, api",
)