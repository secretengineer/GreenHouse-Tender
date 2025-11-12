import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('API.env')

API_KEY = os.getenv("API_KEY")
LATITUDE = 39.73915000  # Mayfair Greenhouse latitude
LONGITUDE = -104.98470000  # Mayfair Greenhouse longitude
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
