from dotenv import load_dotenv
import os
import requests
from icecream import ic

load_dotenv()

weatherbit_api_key = os.getenv("WEATHERBIT_API_KEY")

class WeatherBitData: 
    def fetch_weatherbit_data(self, city, country, api_key):
        url = f"https://api.weatherbit.io/v2.0/current?city={city},{country}&key={api_key}"
        response = requests.get(url)
        return response.json()

    weatherbit_data = fetch_weatherbit_data("City", "Country", weatherbit_api_key)
    ic(f"weatherbit api data: {weatherbit_data}")
