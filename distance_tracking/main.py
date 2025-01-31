import pandas as pd 
from icecream import ic 
import requests
import googlemaps 
from dotenv import load_dotenv
import os 
load_dotenv()

# sales_data_modified file path
file_path = '/distance_tracking/excel/sales_data_modified.xlsx'
hmrc_api_url = 'https://api.service.hmrc.gov.uk/customs/goods-movement-system/movements'
google_api_key = os.getenv('GOOGLE_API_KEY')

def calculate_distance(google_api_key, origin, destination): 
    gmaps = googlemaps.Client(key = google_api_key)
    result = gmaps.distance_matrix(origins = [origin], destinations = [destination], mode = 'driving')
    distance = result['rows'][0]['elements'][0]['distance']['value']
    return distance / 1000 

def main(): 
    origin_postcode = 'KA8 8AE' 
    destination_postcode = 'PA3 4JA' 
    distance = calculate_distance(google_api_key, origin_postcode, destination_postcode)
    ic(f'total distance travelled: {distance} km')
    
if __name__ == '__main__': 
    main()