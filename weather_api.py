import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
api_key = os.getenv("API_KEY")

def get_weather(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch data"}

if __name__ == "__main__":
    # Latitude and longitude for Mayfair Greenhouse
    latitude = 39.7373324  # Mayfair Greenhouse latitude
    longitude = -104.9136498  # Mayfair Greenhouse longitude

    weather_data = get_weather(latitude, longitude, api_key)
    print(weather_data)
