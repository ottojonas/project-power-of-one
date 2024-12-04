import os
import time

import requests
from dotenv import load_dotenv
from icecream import ic


def load_environment():
    load_dotenv()
    return os.getenv("WEATHERBIT_API_KEY")


def get_user_input():
    city = input("Enter city: ")
    country = input("Enter country code (e.g., GB for Great Britain): ")
    return city, country


def build_urls(city, country, api_key):
    base_url = "https://api.weatherbit.io/v2.0"
    current_weather_url = f"{base_url}/current?city={city},{country}&key={api_key}"
    weather_alert_url = f"{base_url}/alerts?city={city},{country}&key={api_key}"
    return current_weather_url, weather_alert_url


def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        ic(f"Error fetching data from {url}: {e}")
        return None


def main():
    api_key = load_environment()
    city, country = get_user_input()
    ic(city)
    ic(country)

    current_weather_url, weather_alert_url = build_urls(city, country, api_key)
    ic(current_weather_url)
    ic(weather_alert_url)

    while True:
        weather_data = fetch_data(current_weather_url)
        if weather_data:
            ic(weather_data)

        alert_data = fetch_data(weather_alert_url)
        if alert_data:
            ic(alert_data)

        time.sleep(5)


if __name__ == "__main__":
    main()
