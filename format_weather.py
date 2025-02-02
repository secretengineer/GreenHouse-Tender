import json

def format_weather_data(weather_data):
    """
    Format the weather data into a user-friendly format.
    
    Args:
        weather_data (dict): The raw weather data from the API.
        
    Returns:
        str: A formatted string with relevant weather information.
    """
    try:
        # Extract relevant information
        city = weather_data.get('name', 'Unknown Location')
        temperature_k = weather_data['main']['temp']
        temperature_f = (temperature_k - 273.15) * 9/5 + 32  # Convert from Kelvin to Fahrenheit
        feels_like_k = weather_data['main']['feels_like']
        feels_like_f = (feels_like_k - 273.15) * 9/5 + 32  # Convert from Kelvin to Fahrenheit
        temp_min_k = weather_data['main']['temp_min']
        temp_min_f = (temp_min_k - 273.15) * 9/5 + 32  # Convert from Kelvin to Fahrenheit
        temp_max_k = weather_data['main']['temp_max']
        temp_max_f = (temp_max_k - 273.15) * 9/5 + 32  # Convert from Kelvin to Fahrenheit
        weather_description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        
        # Create a formatted string
        formatted_output = (
            f"Weather in {city}:\n"
            f"Temperature: {temperature_f:.2f}&deg;F\n"
            f"Feels Like: {feels_like_f:.2f}&deg;F\n"
            f"Minimum Temperature: {temp_min_f:.2f}&deg;F\n"
            f"Maximum Temperature: {temp_max_f:.2f}&deg;F\n"
            f"Condition: {weather_description.capitalize()}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s\n"
        )
        
        return formatted_output
    except KeyError as e:
        return f"Error: Missing data in the response - {e}"

if __name__ == "__main__":
    # Example usage
    sample_weather_data = {
        "name": "Glendale",
        "main": {
            "temp": 292.49,
            "humidity": 19
        },
        "weather": [
            {
                "description": "broken clouds"
            }
        ],
        "wind": {
            "speed": 1.54
        }
    }
    
    print(format_weather_data(sample_weather_data))
