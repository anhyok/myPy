# weather.py

import requests

def get_weather(api_url, city):
    response = requests.get(f"{api_url}/{city}")
    return response.json()
