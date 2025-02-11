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
            <title>Mayfair Greenhouse Weather</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background: #1a1a1a;
                    color: #fff;
                }}
                .container {{
                    background-color: #333;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    text-align: center;
                    border: 2px solid #4CAF50;
                }}
                h1 {{
                    margin-bottom: 20px;
                    font-size: 2.5em;
                }}
                pre {{
                    text-align: left;
                    white-space: pre-wrap;
                    word-wrap: break-word;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Mayfair Greenhouse Weather</h1>
                <div id="weather-data">
                    <pre>{format_weather_data(weather_data)}</pre>
                </div>
            </div>
        </body>
        </html>
        """)
