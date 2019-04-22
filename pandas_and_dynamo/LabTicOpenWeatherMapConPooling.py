import pandas as pd
import requests
from multiprocessing import Pool

cities = pd.read_json('city.list.json')

cities_names = cities['name']


def get_weather(city):
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?q='
                       + city
                       + '&APPID=560e60fe74d03c226f8d38330c255062')
    res = res.json()
    return [city, res['main']['temp'], res['main']['humidity']]


p = Pool()
result = p.map(get_weather, cities_names)

weather_df = pd.DataFrame(data=result, columns=['City', 'Temperature', 'Humidity'])

print(weather_df)
