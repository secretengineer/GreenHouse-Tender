import os
import requests
import logging
from dotenv import load_dotenv

# --- Initialization ---

# Configure basic logging to capture errors and informational messages.
# This helps in debugging and monitoring the application's health.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from a .env file (e.g., API.env).
# This is a secure way to manage sensitive data like API keys without hardcoding them.
load_dotenv('API.env')

# Retrieve the OpenWeatherMap API key from environment variables.
# This serves as a default key if one isn't provided directly to the function.
DEFAULT_API_KEY = os.getenv("API_KEY")

# --- Core Function ---

def get_weather(lat, lon, api_key=None, timeout=10):
    """
    Fetch weather data from the OpenWeatherMap API.

    This function constructs a request, handles potential network errors,
    and returns the parsed JSON response or a structured error message.

    Args:
        lat (float): Latitude for the desired location.
        lon (float): Longitude for the desired location.
        api_key (str, optional): OpenWeatherMap API key.
                                 If None, uses the default key from environment variables.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.

    Returns:
        dict: A dictionary containing the weather data on success,
              or an error dictionary (e.g., {'error': 'message'}) on failure.
    """
    # Use the provided api_key or fall back to the default one.
    key = api_key or DEFAULT_API_KEY
    if not key:
        logging.error('API key is missing. Cannot fetch weather data.')
        return {"error": "API key not configured"}

    # Construct the API request URL with the provided coordinates and API key.
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"

    try:
        # Perform the GET request with a specified timeout to prevent indefinite hanging.
        response = requests.get(url, timeout=timeout)
        # Raise an exception for bad status codes (4xx or 5xx).
        response.raise_for_status()
    except requests.exceptions.RequestException as exc:
        # Catch any request-related errors (e.g., DNS failure, connection refused).
        logging.exception('HTTP request to OpenWeatherMap API failed.')
        return {"error": f"Network error: {exc}"}

    try:
        # Parse the JSON response from the API.
        response_data = response.json()
    except ValueError:
        # Handle cases where the response is not valid JSON.
        logging.error("Invalid JSON response received from weather API.")
        return {"error": "Invalid JSON response from server"}

    # Basic validation to ensure the response contains essential weather data.
    if 'main' in response_data:
        return response_data
    else:
        # Log and return an error if the response is valid JSON but lacks expected data.
        error_message = response_data.get('message', 'Unknown API error')
        logging.error(f"API returned an error: {error_message} (Status: {response.status_code})")
        return {"error": error_message}

# --- Command-Line Interface ---

if __name__ == "__main__":
    # This block allows the script to be run directly from the command line
    # for testing or manual weather checks.
    import argparse
    from format_weather import format_weather_data

    # Set up argument parser for command-line usage.
    parser = argparse.ArgumentParser(description='Fetch and print formatted weather data.')
    parser.add_argument('--lat', type=float, default=39.73915, help='Latitude')
    parser.add_argument('--lon', type=float, default=-104.9847, help='Longitude')
    parser.add_argument('--api-key', type=str, default=None, help='OpenWeatherMap API key')
    args = parser.parse_args()

    # Fetch and display the weather data.
    weather_info = get_weather(args.lat, args.lon, args.api_key)
    if 'error' in weather_info:
        print(f"Error: {weather_info['error']}")
    else:
        # Format the raw data for readable output.
        formatted_weather = format_weather_data(weather_info)
        print(formatted_weather)
