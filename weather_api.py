from flask import Flask, jsonify
import os
import requests
from dotenv import load_dotenv
from format_weather import format_weather_data
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv('API.env')

# Retrieve API key from environment variables
api_key = os.getenv("API_KEY")

def get_weather(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    
    try:
        response_data = response.json()
    except ValueError:
        logging.error("Invalid JSON response")
        return {"error": "Invalid JSON response"}
    
    if response.status_code == 200 and 'main' in response_data:
        return response_data
    else:
        logging.error("Unable to fetch data")
        return {"error": "Unable to fetch data"}

@app.route('/weather', methods=['GET'])
def weather():
    latitude = 39.7373324  # Mayfair Greenhouse latitude
    longitude = -104.9136498  # Mayfair Greenhouse longitude
    weather_data = get_weather(latitude, longitude, api_key)
    formatted_weather_data = format_weather_data(weather_data)
    return jsonify({"weather": formatted_weather_data})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
