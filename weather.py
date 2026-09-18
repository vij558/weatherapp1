import os

import requests
import streamlit as st
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",
    }

    try:
        response = requests.get(
            WEATHER_URL,
            params=params,
            timeout=10,
        )

        if response.status_code == 404:
            return None, "City not found. Please try again."

        if response.status_code != 200:
            return None, "Unable to fetch weather data. Please try again later."

        data = response.json()

        weather = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "condition": data["weather"][0]["main"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind_speed": data["wind"]["speed"],
        }

        return weather, None

    except requests.exceptions.Timeout:
        return None, "The request timed out. Please try again."

    except requests.exceptions.ConnectionError:
        return None, "Unable to connect. Please check your internet connection."


st.set_page_config(
    page_title="Weather Dashboard",
    layout="centered",
)

st.title("Weather Dashboard")
st.write("Check the current weather for any city.")

city_name = st.text_input(
    "City",
    placeholder="Enter a city name",
)

if st.button("Get Weather", type="primary"):
    city_name = city_name.strip()

    if not city_name:
        st.warning("Please enter a city name.")

    elif not API_KEY:
        st.error("API key is missing. Please check your .env file.")

    else:
        weather, error = get_weather(city_name)

        if error:
            st.error(error)

        else:
            st.subheader(
                f"{weather['city']}, {weather['country']}"
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Temperature",
                    f"{weather['temperature']:.1f} °C",
                )

            with col2:
                st.metric(
                    "Humidity",
                    f"{weather['humidity']}%",
                )

            with col3:
                st.metric(
                    "Wind Speed",
                    f"{weather['wind_speed']} m/s",
                )

            col4, col5 = st.columns(2)

            with col4:
                st.metric(
                    "Feels Like",
                    f"{weather['feels_like']:.1f} °C",
                )

            with col5:
                st.metric(
                    "Pressure",
                    f"{weather['pressure']} hPa",
                )

            st.write(
                f"**Weather Condition:** {weather['condition']}"
            )