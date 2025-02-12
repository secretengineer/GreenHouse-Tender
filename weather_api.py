import os
import requests
from dotenv import load_dotenv
from format_weather import format_weather_data
import time

# Load environment variables from .env file
load_dotenv('API.env')

# Retrieve API key from environment variables
api_key = os.getenv("API_KEY")

# Debugging line to check if API key is loaded correctly
if api_key is None:
    print("Error: API_KEY is not defined.")
else:
    print("API Key loaded successfully.")  # Removed actual API key from being printed

def get_weather(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    
    try:
        response_data = response.json()
    except ValueError:
        return {"error": "Invalid JSON response"}
    if response.status_code == 200 and 'main' in response_data:
        return response_data
    else:
        return {"error": "Unable to fetch data"}

if __name__ == "__main__":
    # Latitude and longitude for Mayfair Greenhouse
    latitude = 39.73915000  # Mayfair Greenhouse latitude
    longitude = -104.98470000  # Mayfair Greenhouse longitude

    weather_data = get_weather(latitude, longitude, api_key)
    print("Preparing to write formatted output to index.html")  # Debugging line
    print(f"Weather Data: {weather_data}")  # Debugging line

    formatted_weather_data = format_weather_data(weather_data)
    print(f"Formatted Weather Data: {formatted_weather_data}")  # Debugging line

    # Read the existing index.html file
    with open('index.html', 'r') as html_file:
        html_content = html_file.read()

    # Ensure the placeholder exists and replace it with the formatted weather data
    if '<div id="weather-data"></div>' in html_content:
        updated_html_content = html_content.replace(
            '<div id="weather-data"></div>',
            f'<div id="weather-data"><pre>{formatted_weather_data}</pre></div>'
        )
    else:
        print("Placeholder not found in index.html")

    # Write the updated content back to the index.html file
    with open('index.html', 'w') as html_file:
        html_file.write(updated_html_content)

    print("Formatted output written to index.html")  # Debugging line
