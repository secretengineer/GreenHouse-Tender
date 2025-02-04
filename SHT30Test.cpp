#include <Wire.h>
#include <Adafruit_SHT30.h>

#define SHT30_ADDRESS 0x44
#define RELAY_PIN 2 // Replace with actual pin number

Adafruit_SHT30 sht30;

void setup() {
  Serial.begin(9600);
  
  // Initialize I2C
  Wire.begin();
  
  // Initialize SHT30 sensor
  sht30.begin(Wire);
  
  // Set up relay pin as output
  pinMode(RELAY_PIN, OUTPUT);
}

void loop() {
  float temperature, humidity;
  
  // Read temperature and humidity
  sht30.measure();
  temperature = sht30.temperature;
  humidity = sht30.relativeHumidity;
  
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println("°C");
  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.println("%");
  
  // Control relay based on temperature
  if (temperature > 77.0) {
    digitalWrite(RELAY_PIN, HIGH);
    Serial.println("Relay is ON");
  } else {
    digitalWrite(RELAY_PIN, LOW);
    Serial.println("Relay is OFF");
  }
  
  delay(2000); // Wait 2 seconds before next reading
}