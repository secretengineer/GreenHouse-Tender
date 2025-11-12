import os
import time
from flask import Flask, jsonify, send_from_directory
from dotenv import load_dotenv

# Import the existing get_weather function and the formatter
from weather_api import get_weather
from format_weather import format_weather_data

# Load API key
load_dotenv('API.env')
API_KEY = os.getenv('API_KEY')

app = Flask(__name__, static_folder='.', template_folder='.')

LATITUDE = 39.73915
LONGITUDE = -104.9847


@app.route('/')
def home():
    return send_from_directory('.', 'index.html')


@app.route('/weather')
def weather():
    if not API_KEY:
        return jsonify({'error': 'API_KEY not configured on server'}), 500

    data = get_weather(LATITUDE, LONGITUDE, API_KEY)
    if isinstance(data, dict) and data.get('error'):
        return jsonify({'error': data.get('error')}), 502

    formatted = format_weather_data(data)
    timestamp = time.time()
    return jsonify({'formatted': formatted, 'raw': data, 'timestamp': timestamp})


if __name__ == '__main__':
    # Run on local network; change host/port as needed
    app.run(host='0.0.0.0', port=5000)
