import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('API.env')

# Retrieve API key from environment variables
api_key = os.getenv("API_KEY")

# Debugging line to check if API key is loaded correctly
if api_key is None:
    print("Error: API_KEY is not defined.")
else:
    print(f"Loaded API Key: {api_key}")

def get_weather(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    
    try:
        response_data = response.json()
    except ValueError:
        return {"error": "Invalid JSON response"}
    if response.status_code == 200 and 'main' in response_data:
        return response.json()
    else:
        return {"error": "Unable to fetch data"}

if __name__ == "__main__":
    # Latitude and longitude for Mayfair Greenhouse
    latitude = 39.7373324  # Mayfair Greenhouse latitude
    longitude = -104.9136498  # Mayfair Greenhouse longitude

    weather_data = get_weather(latitude, longitude, api_key)
    print("Preparing to write formatted output to index.html")  # Debugging line
    print(f"Weather Data: {weather_data}")  # Debugging line

    from format_weather import format_weather_data

    print("Writing formatted output to index.html")  # Debugging line
    with open('index.html', 'w') as html_file:
        html_file.write(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Weather Information</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                    padding: 20px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    background-color: #f9f9f9;
                }}
                h1 {{
                    color: #333;
                }}
            </style>
        </head>
        <body>
            <h1>Weather Information</h1>
            <div id="weather-data">
                <pre>{format_weather_data(weather_data)}</pre>
            </div>
        </body>
        </html>
        """)
    weather_data = get_weather(latitude, longitude, api_key)
    print(weather_data)
