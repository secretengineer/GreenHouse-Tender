from flask import Flask, jsonify
import os
import requests
from dotenv import load_dotenv
from format_weather import format_weather_data
import logging

# Configure logging for library usage
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file (only if available)
load_dotenv('API.env')

# Retrieve API key from environment variables if caller doesn't provide one
DEFAULT_API_KEY = os.getenv("API_KEY")


def get_weather(lat, lon, api_key=None, timeout=10):
    """Fetch weather from OpenWeatherMap and return parsed JSON or error dict.

    Args:
        lat (float): latitude
        lon (float): longitude
        api_key (str|None): OpenWeatherMap API key; if None, DEFAULT_API_KEY is used
        timeout (int): request timeout in seconds

    Returns:
        dict: parsed JSON on success or {'error': 'message'} on failure
    """
    key = api_key or DEFAULT_API_KEY
    if not key:
        logging.error('No API key provided for get_weather')
        return {"error": "API key not configured"}

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
    try:
        response = requests.get(url, timeout=timeout)
    except requests.RequestException as exc:
        logging.exception('HTTP request to weather API failed')
        return {"error": str(exc)}

    try:
        response_data = response.json()
    except ValueError:
        logging.error("Invalid JSON response from weather API")
        return {"error": "Invalid JSON response"}

    if response.status_code == 200 and 'main' in response_data:
        return response_data
    else:
        logging.error("Unable to fetch data, status=%s, body=%s", response.status_code, response_data)
        return {"error": response_data.get('message', 'Unable to fetch data')}


def get_formatted_weather(lat, lon, api_key=None):
    """Convenience wrapper: fetch and format weather text for display."""
    raw = get_weather(lat, lon, api_key)
    return format_weather_data(raw)


if __name__ == "__main__":
    # Simple CLI for manual runs; prints formatted weather to stdout.
    import argparse

    parser = argparse.ArgumentParser(description='Fetch and print formatted weather')
    parser.add_argument('--lat', type=float, default=39.73915)
    parser.add_argument('--lon', type=float, default=-104.9847)
    parser.add_argument('--api-key', type=str, default=None)
    args = parser.parse_args()

    print(get_formatted_weather(args.lat, args.lon, args.api_key))
