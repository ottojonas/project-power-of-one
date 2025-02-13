import requests
from icecream import ic
import pandas as pd
from bs4 import BeautifulSoup

df = pd.read_csv("csv/food_data.csv", delimiter="\t", encoding="ISO-8859-1")

API_KEY = ''

def scrape_data(trading_name):
    search_url = f"https://www.google.com/search?q={trading_name.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    phone = (
        soup.find("span", class_="BNeawe tAd8D AP7Wnd").text
        if soup.find("span", class_="BNeawe tAd8D AP7Wnd")
        else "N/A"
    )
    return phone


def get_company_data(trading_name):
    search_url = f"https://api.company-information.service.gov.uk/search/companies?q={trading_name}"
    headers = {"Authorization": f"Basic {API_KEY}"}
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data["items"]:
            company_number = data["items"][0]["company_number"]
            company_url = f"https://api.company-information.service.gov.uk/company/{company_number}"
            company_response = requests.get(company_url, headers=headers)
            if company_response.status_code == 200:
                company_data = company_response.json()
                address = company_data.get("registered_office_address", {}).get(
                    "address_line_1", "N/A"
                )
                return address
    return "N/A"


def fill_missing_info(row):
    if (
        pd.isna(row["Address"])
        or pd.isna(row["Phone"])
        or pd.isna(row["Email"])
        or pd.isna(row["Website"])
    ):
        address, phone, email, website = get_company_data(row["TradingName"])
        if pd.isna(row["Address"]):
            row["Address"] = address
        if pd.isna(row["Phone"]):
            row["Phone"] = phone
        if pd.isna(row["Email"]):
            row["Email"] = email
        if pd.isna(row["Website"]):
            row["Website"] = website
    return row


df = df.apply(fill_missing_info, axis=1)

df.to_csv("csv/food_data_updated.csv", index=False, sep="\t")
