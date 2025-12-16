import os
import time
from flask import Flask, jsonify, send_from_directory
from dotenv import load_dotenv

# Import the existing get_weather function and the formatter
from weather_api import get_weather
from format_weather import format_weather_data

# Load API key from .env file for security
load_dotenv('API.env')
API_KEY = os.getenv('API_KEY')

# Initialize Flask app
# By default, Flask serves files from a 'static' folder at the '/static' URL prefix.
app = Flask(__name__, template_folder='.')

# --- Configuration ---
# Default location for weather data (Denver, CO)
LATITUDE = 39.73915
LONGITUDE = -104.9847

# --- Helper Functions ---
def get_weather_data():
    """
    Fetches, formats, and timestamps weather data.

    Returns:
        dict: A dictionary containing formatted and raw weather data,
              plus a Unix timestamp. Returns an error dictionary on failure.
    """
    if not API_KEY:
        return {'error': 'API_KEY not configured on server', 'status': 500}

    raw_data = get_weather(LATITUDE, LONGITUDE, API_KEY)
    if isinstance(raw_data, dict) and 'error' in raw_data:
        return {'error': raw_data['error'], 'status': 502}

    formatted_data = format_weather_data(raw_data)
    timestamp = int(time.time())

    return {
        'formatted': formatted_data,
        'raw': raw_data,
        'timestamp': timestamp
    }

# --- Routes ---
@app.route('/')
def home():
    """Serves the main HTML page."""
    return send_from_directory(app.template_folder, 'index.html')


@app.route('/weather')
def weather_route():
    """Provides weather data via a JSON API endpoint."""
    weather_data = get_weather_data()
    status_code = weather_data.pop('status', 200)
    return jsonify(weather_data), status_code


if __name__ == '__main__':
    # Run the app on the local network
    # Note: In a production environment, use a proper WSGI server like Gunicorn
    app.run(host='0.0.0.0', port=5000)
