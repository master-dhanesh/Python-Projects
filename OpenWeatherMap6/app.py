import requests
from pprint import pprint

city = input('Enter City Name: ')
AIP_Key = 'f9fcf8993853a9dae975c63fb57e7242'

base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={AIP_Key}'
weather_data = requests.get(base_url).json()

pprint(weather_data)
# print(weather_data)