import pandas as pd
import requests

cities = pd.read_json('city.list.json')

cities_names = cities['name']
data = []

for city in cities_names:
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=560e60fe74d03c226f8d38330c255062')
    weather_data = res.json()

    data.append([city, weather_data['main']['temp'], weather_data['main']['humidity']])

weather_df = pd.DataFrame(data=data, columns=['City', 'Temperature', 'Humidity'])

print(weather_df)

