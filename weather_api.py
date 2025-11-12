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

    # Try to update only the weather section so we don't overwrite CSS/visual design.
    # 1) If there's a <div id="weather-data">...</div>, replace only its inner HTML.
    # 2) Otherwise, look for a heading that contains 'Mayfair Greenhouse Weather' and insert
    #    the weather block right after that heading.
    # 3) Fallback: insert before </body> or append.
    import re

    weather_block = f'<div id="weather-data"><pre>{formatted_weather_data}</pre></div>'

    # 1) Replace inner HTML of existing #weather-data (preserve attributes)
    pattern = re.compile(r'(<div[^>]+id=["\']weather-data["\'][^>]*>)(.*?)(</div>)', re.IGNORECASE | re.DOTALL)
    m = pattern.search(html_content)
    if m:
        print('Found existing #weather-data element — replacing its inner content')
        updated_html_content = html_content[:m.start(2)] + f'<pre>{formatted_weather_data}</pre>' + html_content[m.end(2):]
    else:
        # 2) Look for a heading mentioning Mayfair Greenhouse Weather (h1-h3)
        heading_pattern = re.compile(r'(<h[1-3][^>]*>\s*(?:Mayfair\s+Greenhouse\s+Weather)\s*</h[1-3]>)', re.IGNORECASE)
        hm = heading_pattern.search(html_content)
        if hm:
            print('Found heading "Mayfair Greenhouse Weather" — inserting weather block after it')
            insert_point = hm.end(1)
            updated_html_content = html_content[:insert_point] + '\n    ' + weather_block + html_content[insert_point:]
        else:
            # 3) Fallback: try to insert before </body>, otherwise append to the end
            print("Placeholder/heading not found in index.html, using fallback insertion")
            insert_point = html_content.rfind('</body>')
            if insert_point != -1:
                updated_html_content = (
                    html_content[:insert_point]
                    + f'\n    {weather_block}\n'
                    + html_content[insert_point:]
                )
            else:
                # As a last resort append to the file (preserves existing content)
                updated_html_content = html_content + f'\n{weather_block}\n'

    # Write the updated content back to the index.html file
    with open('index.html', 'w') as html_file:
        html_file.write(updated_html_content)

    print("Formatted output written to index.html")  # Debugging line
