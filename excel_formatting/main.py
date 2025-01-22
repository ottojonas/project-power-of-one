import pandas as pd
from icecream import ic
from dotenv import load_dotenv
import os
import googlemaps

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

# load the excel file
file_path = "excel_formatting/excel-sheets/modified_storelist_test.xlsx"
df = pd.read_excel(file_path)

ic(df.columns)

# initialize Google Maps client
gmaps = googlemaps.Client(key=google_api_key)


def clean_location_name(location):
    return " ".join(location.split()).title()


def get_country_google(location):
    location = clean_location_name(location) + ", UK"
    geocode_result = gmaps.geocode(location)
    ic(geocode_result)
    if geocode_result:
        address_components = geocode_result[0].get("address_components", [])
        for component in address_components:
            if "country" in component.get("types", []):
                country = component.get("long_name", "")
                if country == "United Kingdom":
                    # Check for specific locations within the UK
                    for comp in address_components:
                        if "administrative_area_level_1" in comp.get("types", []):
                            if comp.get("long_name") in [
                                "England",
                                "Scotland",
                                "Wales",
                                "Ireland",
                            ]:
                                return comp.get("long_name")
                return country
    return None


# add a new column to store the country
df["country"] = None

# iterate over the rows and assign the country to the new column
for index, row in df.iterrows():
    location = row["location"]
    try:
        country = get_country_google(location)
        if country:
            df.at[index, "country"] = country
        else:
            ic(f"Country not found for location: {location}")
    except Exception as e:
        ic(f"Failed to get country for location: {location}: {e}")

# save the updated dataframe back to the existing Excel file
output_file_path = "excel_formatting/excel-sheets/modified_storelist_test.xlsx"
df.to_excel(output_file_path, index=False)
