from dotenv import load_dotenv
import os
import requests
from icecream import ic

class WeatherBitData:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("WEATHERBIT_API_KEY")

    def fetch_weatherbit_data(self, city, country):
        url = f"https://api.weatherbit.io/v2.0/current?city={city},{country}&key={self.api_key}"
        response = requests.get(url)
        return response.json()

    def display_weatherbit_data(self, city, country):
        weatherbit_data = self.fetch_weatherbit_data(city, country)
        ic(f"weatherbit api data: {weatherbit_data}")

if __name__ == "__main__":
    weather_data = WeatherBitData()
    weather_data.display_weatherbit_data("City", "Country")
