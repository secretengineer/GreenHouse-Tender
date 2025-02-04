import smbus2
import time
import RPi.GPIO as GPIO

# Constants
SHT30_ADDRESS = 0x44  # I2C address of the SHT30 sensor
RELAY_PIN = 17  # GPIO pin for the relay
TEMP_THRESHOLD = 77.0  # Temperature threshold in Fahrenheit

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Initialize I2C bus
bus = smbus2.SMBus(1)

def read_sht30():
    """
    Read temperature and humidity from the SHT30 sensor.
    
    Returns:
        tuple: A tuple containing the temperature in Fahrenheit and the humidity in percentage.
    """
    # Send measurement command to SHT30 sensor
    bus.write_i2c_block_data(SHT30_ADDRESS, 0x24, [0x00])
    time.sleep(0.5)  # Wait for the measurement to complete
    
    # Read 6 bytes of data from the sensor
    data = bus.read_i2c_block_data(SHT30_ADDRESS, 0x00, 6)
    
    # Convert the data to temperature and humidity
    temp_c = -45 + 175 * (data[0] * 256 + data[1]) / 65535.0  # Temperature in Celsius
    temp_f = (temp_c * 9/5) + 32  # Convert to Fahrenheit
    humidity = 100 * (data[3] * 256 + data[4]) / 65535.0  # Humidity in percentage
    
    return temp_f, humidity

def control_relay(temperature):
    """
    Control the relay based on the temperature.
    
    Args:
        temperature (float): The temperature in Fahrenheit.
    """
    if temperature > TEMP_THRESHOLD:
        GPIO.output(RELAY_PIN, GPIO.HIGH)  # Turn on relay
        print("Relay is ON")
    else:
        GPIO.output(RELAY_PIN, GPIO.LOW)  # Turn off relay
        print("Relay is OFF")

def main():
    """
    Main function to read sensor data and control the relay.
    """
    try:
        while True:
            # Read temperature and humidity from the sensor
            temperature, humidity = read_sht30()
            print(f"Temperature: {temperature:.2f} °F, Humidity: {humidity:.2f} %")
            
            # Control the relay based on the temperature
            control_relay(temperature)
            
            time.sleep(2)  # Wait before the next reading
    
    except KeyboardInterrupt:
        print("Program stopped by user.")
    finally:
        GPIO.cleanup()  # Clean up GPIO settings

if __name__ == "__main__":
    main()
