import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print("Get current Weather Conditions\n")

    city = input("Please enter a city name\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'

    print(request_url)
    weather_data = requests.get(request_url).json()
    print(f'Current Weather for {weather_data["name"]}')
    print(f'Current Temperature is {weather_data["main"]["temp"]:.1f}:°')


get_current_weather()