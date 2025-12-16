# 🌱 GreenHouse Tender

> A comprehensive real-time climate monitoring and control system for backyard greenhouse management

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Hardware Integration](#hardware-integration)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## 🌟 Overview

**GreenHouse Tender** is an intelligent climate monitoring and control system designed to maintain optimal growing conditions in backyard greenhouses. By integrating real-time external weather data from OpenWeatherMap with internal sensor readings, the system automatically adjusts environmental controls to optimize plant growth while maximizing resource efficiency.

The application features a responsive web dashboard that displays:
- Real-time local weather conditions
- Internal greenhouse temperature and humidity
- Soil temperature and pH levels
- Ventilation and fan status
- Water system controls
- System notifications and alerts

---

## ✨ Features

### Current Features
- **Real-Time Weather Monitoring**: Integration with OpenWeatherMap API for location-specific weather data.
- **Redesigned Responsive Dashboard**: Features a modern, minimalist, and mobile-first dark theme for an improved user experience.
- **Accurate Timestamps**: Displays both the current time and a reliable "last updated" timestamp for weather data, provided by the server.
- **Manual Weather Refresh**: On-demand weather data updates via a refresh button.
- **Automatic Updates**: Weather data automatically refreshes every 5 minutes.
- **RESTful API**: A clean, Flask-based backend for data management and frontend communication.
- **Modular Codebase**: Refactored frontend (HTML/CSS/JS) and backend (Python) code for enhanced maintainability and readability.

### Planned Features
- **Automated Climate Control**: Integration with actuators for heating, cooling, and ventilation
- **Sensor Integration**: Real-time data from DHT22, soil moisture, and light sensors
- **Historical Data Analytics**: Track trends and optimize growing conditions
- **Alert System**: Notifications for out-of-range conditions
- **Mobile App**: Native iOS/Android applications

---

## 🏗️ System Architecture

### Data Flow
```
External Weather (OpenWeatherMap API)
          ↓
    Flask Backend
          ↓
    Data Processing & Formatting
          ↓
    RESTful API Endpoint
          ↓
    Web Dashboard (JavaScript)
          ↓
    User Interface Display
```

### Components

#### **Data Acquisition**
- OpenWeatherMap API for external weather conditions
- Internal sensor readings (temperature, humidity, soil metrics)
- Periodic data collection at configurable intervals

#### **Data Processing**
- Real-time analysis of environmental conditions
- Comparison against optimal climate parameters
- Decision algorithms for automated control

#### **User Interface**
- Web-based dashboard built with HTML5, CSS3, and JavaScript
- Real-time data visualization
- Manual control interface for greenhouse systems

#### **Hardware Control** (In Development)
- Microcontroller integration (Raspberry Pi/Arduino)
- Actuator control for heating, cooling, ventilation, and irrigation

---

## 🛠️ Technology Stack

### Backend
- **Python 3.8+**: Core programming language
- **Flask 2.0+**: Web framework for API and server
- **Requests**: HTTP library for API integration
- **python-dotenv**: Environment variable management

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with responsive design
- **JavaScript (ES6+)**: Dynamic functionality and AJAX requests
- **Font Awesome**: Icon library

### APIs & Services
- **OpenWeatherMap API**: Real-time weather data

### Hardware (Optional)
- **Raspberry Pi / Arduino**: Microcontroller for sensor/actuator control
- **DHT22**: Temperature and humidity sensors
- **Soil Moisture Sensors**: Soil condition monitoring
- **Relay Modules**: Actuator control

---

## 📦 Prerequisites

Before installing GreenHouse Tender, ensure you have the following:

- **Python 3.8 or higher** ([Download Python](https://www.python.org/downloads/))
- **pip** (Python package manager, included with Python)
- **OpenWeatherMap API Key** ([Get Free API Key](https://openweathermap.org/api))
- **Git** (optional, for cloning the repository)

---

## 🚀 Installation

### Method 1: Clone from GitHub

1. **Clone the repository**
   ```bash
   git clone https://github.com/secretengineer/GreenHouse-Tender.git
   cd GreenHouse-Tender
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Method 2: Download ZIP

1. Download the repository as a ZIP file from GitHub
2. Extract the ZIP file to your desired location
3. Open a terminal/command prompt in the extracted folder
4. Follow steps 2-3 from Method 1 above

---

## ⚙️ Configuration

### 1. Set Up API Key

Create a file named `API.env` in the root directory of the project:

```bash
# Windows PowerShell
New-Item -Path . -Name "API.env" -ItemType "file"

# macOS/Linux
touch API.env
```

### 2. Add Your API Key

Open `API.env` in a text editor and add your OpenWeatherMap API key:

```env
API_KEY=your_openweathermap_api_key_here
```

**Important**: Never commit your `API.env` file to version control. It should already be listed in `.gitignore`.

### 3. Configure Location (Optional)

To change the default greenhouse location, edit `app.py`:

```python
# Default: Denver, CO area
LATITUDE = 39.73915
LONGITUDE = -104.9847
```

Replace with your greenhouse's coordinates.

---

## 🎯 Running the Application

### Start the Flask Server

1. **Ensure your virtual environment is activated** (if using one)
   ```bash
   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

2. **Run the application**
   ```bash
   python app.py
   ```

3. **Expected output**
   ```
   * Serving Flask app 'app'
   * Debug mode: off
   * Running on http://0.0.0.0:5000
   ```

### Access the Dashboard

Open your web browser and navigate to:
```
http://localhost:5000
```

Or from another device on your local network:
```
http://[your-computer-ip]:5000
```

### Stopping the Server

Press `Ctrl+C` in the terminal to stop the Flask server.

---

## 🔌 Hardware Integration

### Microcontroller Setup

The `hardware/` directory contains code for integrating physical sensors and actuators:

- **`sht30_relay_control.py`**: Python script for SHT30 temperature/humidity sensor with relay control
- **`SHT30Test.cpp`**: Arduino/C++ test code for SHT30 sensor
- **`MicrocontrollerREADME.md`**: Detailed hardware setup instructions

### Sensor Requirements
- DHT22 or SHT30 Temperature/Humidity Sensor
- Soil Moisture Sensor
- Soil pH Sensor
- Light Level Sensor (optional)

### Actuator Requirements
- Relay modules for switching 120V/240V devices
- Fans for ventilation
- Heating elements
- Water valve/pump for irrigation

For detailed hardware setup instructions, see [`hardware/MicrocontrollerREADME.md`](hardware/MicrocontrollerREADME.md).

---

## 📁 Project Structure

```
GreenHouse-Tender/
├── app.py                      # Main Flask application
├── weather_api.py              # Handles OpenWeatherMap API requests
├── format_weather.py           # Utilities for formatting weather data
├── index.html                  # Main dashboard HTML file
├── requirements.txt            # Python dependencies for the project
├── static/                     # Contains all static assets
│   ├── style.css               # Main stylesheet for the dashboard
│   └── script.js               # JavaScript for dashboard interactivity
├── API.env                     # Environment variables (Git-ignored)
├── README.md                   # This file
└── hardware/                   # Code for hardware integration (e.g., Raspberry Pi)
    ├── ...
```

---

## 📡 API Documentation

### Endpoints

#### `GET /`
Returns the main dashboard HTML page.

**Response**: HTML document

---

#### `GET /weather`
Fetches current weather data for the configured location.

**Response**:
```json
{
  "formatted": "Location: Denver\nTemperature: 68.5°F\n...",
  "raw": {
    "main": {
      "temp": 293.45,
      ...
    },
    ...
  },
  "timestamp": 1699824000
}
```

**Error Response** (500):
```json
{
  "error": "API_KEY not configured on server"
}
```

**Error Response** (502):
```json
{
  "error": "Unable to fetch weather data"
}
```

---

## 🔮 Future Enhancements

### Short-Term Goals
- [ ] Live sensor data integration from hardware
- [ ] Historical data logging and visualization
- [ ] Automated control system implementation
- [ ] Email/SMS alert system
- [ ] User authentication and multi-user support

### Long-Term Goals
- [ ] Machine learning for predictive climate control
- [ ] Mobile application (iOS/Android)
- [ ] Voice assistant integration (Alexa/Google Home)
- [ ] Multi-greenhouse management
- [ ] Cloud-based data storage and analytics
- [ ] Solar panel and battery monitoring
- [ ] Camera integration for plant monitoring

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Pat Ryan**
- GitHub: [@secretengineer](https://github.com/secretengineer)

---

## 🙏 Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing weather data API
- [Flask](https://flask.palletsprojects.com/) for the excellent web framework
- [Font Awesome](https://fontawesome.com/) for the icon library

---

<div align="center">
  <p>Made with ❤️ for sustainable agriculture</p>
  <p>⭐ Star this repository if you find it helpful!</p>
</div>
