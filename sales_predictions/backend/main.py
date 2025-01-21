import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import requests
from icecream import ic
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("WEATHERBIT_API_KEY")

# data processing

# load sales data
sales_data = pd.read_csv("")


# fetch weather data
def fetch_weather_data(city, country, api_key):
    url = f"https://api.weatherbit.io/v2.0/history/daily?city={city},{country}&key={api_key}"
    response = requests.get(url)
    return response.json()


weather_data = fetch_weather_data("City", "Country", api_key)

# process weather data
weather_df = pd.DataFrame(weather_data["data"])


# feature engineering

# merge sales and weather data
data = pd.merge(sales_data, weather_df, left_on="date", right_on="datetime")

# select relevant featurues
features = data[["temperature", "precipitation", "humidity"]]
target = data["sales"]


# model training

# split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    features, target, test_size=0.1, random_state=42
)

# train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)


# prediction

# prediction sales
predictions = model.predict(X_test)

# evaluate from model
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, predictions)
ic(f"mean squared error: {mse}")
