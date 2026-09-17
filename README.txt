Weather App

A simple Python weather application built with Streamlit that fetches
current weather data from the OpenWeather API.

Features

-   Search for the current weather by city name
-   Displays city and country
-   Displays temperature in Celsius
-   Displays the current weather condition
-   Displays humidity
-   Displays wind speed
-   Handles invalid city names with a friendly message
-   Handles network connection errors and request timeouts
-   Keeps the OpenWeather API key outside the source code using
    environment variables

Requirements

-   Python 3
-   An OpenWeather API key

Installation

1. Clone or download the project

Open a terminal in the project folder.

2. Create a virtual environment

Windows:

    python -m venv .venv

3. Activate the virtual environment

PowerShell:

    .\.venv\Scripts\Activate.ps1

4. Install the dependencies

    python -m pip install -r requirements.txt

The project uses:

-   requests
-   python-dotenv
-   streamlit

OpenWeather API Setup

1.  Create an account on OpenWeather.

2.  Generate an API key.

3.  In the project root, create a file named .env.

4.  Add your API key using the following format:

    OPENWEATHER_API_KEY=your_api_key_here

Do not commit the .env file to GitHub.

Run the Application

Make sure the virtual environment is activated, then run:

    python -m streamlit run weather.py

Streamlit will start the application and provide a local URL. Open that
URL in your browser if it does not open automatically.

Using the App

1.  Enter a city name, such as Chennai, London, or New York.
2.  Click Get Weather.
3.  The application displays the current temperature, weather condition,
    humidity, and wind speed.

If the city cannot be found, the application displays a friendly error
message instead of crashing.

Project Structure

    weatherapp/
    ├── weather.py
    ├── requirements.txt
    ├── README.md
    ├── .gitignore
    ├── .env          # local only; do not commit
    └── .venv/        # local only; do not commit

.gitignore

Make sure .gitignore contains:

    .venv/
    .env
    __pycache__/
    *.pyc

This prevents the API key, virtual environment, and generated Python
files from being committed.

Dependencies

Install all required packages with:

    python -m pip install -r requirements.txt

Notes

The application uses the OpenWeather Current Weather Data API and sends
the selected city as a query parameter. API responses are parsed from
JSON and only the weather information required by the interface is
displayed.
