import requests
import os

from dotenv import load_dotenv
load_dotenv()
api = os.getenv("OPENWEATHERMAP_API_KEY")


def get_weather(city, api_key):
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    forecast_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}"
    response = requests.get(current_weather_url.format(city, api_key)).json()

    # lon, lat = response['coord']['lon'], response['coord']['lat']
    # print(lon, lat)
    weather_data = {
        "city" : city,
        "temperature" : round(response['main']['temp'] - 273.15, 2),
        "description" : response['weather'][0]['description'],
        'icon' : response['weather']
    }

    return weather_data




weather = get_weather("mumbai", api)
# print(weather)
for i in weather:
	print(i, weather[i])