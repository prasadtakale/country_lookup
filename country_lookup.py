import os
import requests
import json
import argparse


# Define a function to fetch data from the API for a specific country code
def fetch_country_data(country_code):
    url = f"https://www.travel-advisory.info/api?countrycode={country_code}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Load data from the local file if it exists
def load_data_from_file():
    if os.path.isfile("data.json"):
        with open("data.json", "r") as file:
            return json.load(file)
    else:
        return None

# Updated lookup function to use local data and update if needed
def lookup_country(country_code):
    data = load_data_from_file()

    if data is not None:
        # Check if the country code exists in the data
        if country_code in data['data']:
            # Extract and return the country name
            return data['data'][country_code]['name']

    # If not found or data file doesn't exist, fetch data from API and create/update data.json
    country_data = fetch_country_data(country_code)
    
    if country_data is not None:
        data = data or {}  # Initialize data if it's None
        data['data'] = data.get('data', {})
        data['data'][country_code] = country_data['data'][country_code]
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
        
        return data['data'][country_code]['name']
    else:
        return "Country code not found even after updating data."

if __name__ == "__main__":
     # Parse command-line arguments
     parser = argparse.ArgumentParser(description="Country Code Lookup Tool")
     parser.add_argument("--countryCodes", nargs="+", help="List of country codes to look up", required=True)
     args = parser.parse_args()

     # Lookup and display country names for provided country codes
     for country_code in args.countryCodes:
         country_name = lookup_country(country_code)
         print(f"Country Code: {country_code} => Country Name: {country_name}")
