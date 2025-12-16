def format_weather_data(weather_data):
    """
    Formats raw weather data from OpenWeatherMap into a readable string.

    This function takes a dictionary of weather data, extracts key information,
    converts temperatures from Kelvin to Fahrenheit, and returns a formatted,
    multi-line string suitable for display.

    Args:
        weather_data (dict): A dictionary containing the raw weather data,
                             typically from the OpenWeatherMap API.

    Returns:
        str: A user-friendly, formatted string with the most relevant
             weather details. Returns an error message string if the
             input data is invalid or missing keys.
    """
    # Check if the input dictionary contains an error message.
    if "error" in weather_data:
        return f"API Error: {weather_data['error']}"
    
    try:
        # Safely extract location name; default if not available.
        city = weather_data.get('name', 'Unknown Location')

        # --- Temperature Extraction and Conversion ---
        # Extract temperatures in Kelvin from the 'main' data block.
        temp_k = weather_data['main']['temp']
        feels_like_k = weather_data['main']['feels_like']
        temp_min_k = weather_data['main']['temp_min']
        temp_max_k = weather_data['main']['temp_max']
        
        # Convert temperatures from Kelvin to Fahrenheit for readability.
        # Formula: (K - 273.15) * 9/5 + 32
        temp_f = (temp_k - 273.15) * 9/5 + 32
        feels_like_f = (feels_like_k - 273.15) * 9/5 + 32
        temp_min_f = (temp_min_k - 273.15) * 9/5 + 32
        temp_max_f = (temp_max_k - 273.15) * 9/5 + 32

        # --- Other Weather Details ---
        # Extract weather condition, humidity, and wind speed.
        weather_description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        
        # --- String Formatting ---
        # Assemble the extracted and converted data into a multi-line string.
        # The .capitalize() method is used for a clean 'Title Case' description.
        formatted_output = (
            f"Location: {city}\n"
            f"Temperature: {temp_f:.1f}°F\n"
            f"Feels Like: {feels_like_f:.1f}°F\n"
            f"Daily Low: {temp_min_f:.1f}°F\n"
            f"Daily High: {temp_max_f:.1f}°F\n"
            f"Condition: {weather_description.capitalize()}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed:.1f} m/s"
        )
        
        return formatted_output
    except (KeyError, IndexError) as e:
        # Handle cases where expected data keys are missing from the API response.
        # This prevents the application from crashing due to malformed data.
        return f"Error: Malformed weather data received. Missing key: {e}"

# --- Command-Line Test ---
if __name__ == "__main__":
    # This block allows for direct testing of the formatting function.
    # To use, run `python format_weather.py` in the terminal.

    # Example of a valid weather data dictionary.
    sample_data = {
        "name": "Denver",
        "main": {
            "temp": 290.15, "feels_like": 289.15,
            "temp_min": 288.15, "temp_max": 292.15,
            "humidity": 45
        },
        "weather": [{"description": "clear sky"}],
        "wind": {"speed": 3.5}
    }
    
    # Example of an error dictionary.
    error_data = {"error": "Invalid API key"}

    print("--- Testing with valid data ---")
    print(format_weather_data(sample_data))
    print("\n" + "="*30 + "\n")
    print("--- Testing with error data ---")
    print(format_weather_data(error_data))
