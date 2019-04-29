import pandas as pd
import requests
from multiprocessing import Pool
import boto3


def save_in_dynamo(aws_table, df):
    for index, row in df.iterrows():
        aws_table.put_item(
            Item={
                'city': row['City'],
                'temperature': row['Temperature'],
                'humidity': row['Humidity']
            }
        )


def get_weather(city):
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?q='
                       + city
                       + '&APPID=560e60fe74d03c226f8d38330c255062')
    res = res.json()
    return [city, res['main']['temp'], res['main']['humidity']]


client = boto3.client('dynamodb',
                      aws_access_key_id='ASIAXZSO4Z2CXC645BSX',
                      aws_secret_access_key='3eaPyOFD4a6VfGDceq7crQsZoXlofUp0K/zjxFtV',
                      aws_session_token='FQoGZXIvYXdzEOj//////////wEaDA+Y8g5Z2xqRNXvclCKHA8cwQ4NChDTWadztOxq02zcQAcLnD6I0yyJZX0OxSr+NDeOqxA1uBpbjg9HZoUEa5qkwsxmwryRP00CB8d1QOOx60CrgqxsCv6KNMO+oubinWtRxVVPqByuZ6JBK41J5XGqo+c6nNnYvxwQnqbFHSCnlmiBLi81BdL6/mLOQdMNqaIrMZ00Yi3YG4Zuc9V98dWwtM/CdU+Q93a+dtblSwidEKsCBvZlhxvoE9ySgiDDLbjKjTKl4YVMoyo+jPU/lbQp9oXBbW/wG+ivEBX58dUqomROGZ0+NDQyoLPaGB4tRp6QJ/3Z8cCFuHfb0pLrM40Ulako7/gNi1IyvF1IbiD0j9HwgYb1kUgoOFr/2S7725e7HRsTUfsccr3M3ijrVuzOBMyinNEKj/BXLzK4cln8ee2aW1XPvwUNWNHPgeAYkdcBRdpvcKD/TJSdhAn0dOeMCUV9/HMM7BEis4WSJfOOy/guQx8tqNhLxkYOXH6Nayh7Gfp3WjPRtrXupI74FoPKIium65mAo0of55QU='
                      )

table = client.create_table(
    TableName='weather',
    KeySchema=[
        {
            'AttributeName': 'city',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinition=[
        {
            'AttributeName': 'city',
            'AttributeType': 'S'
        },
{
            'AttributeName': 'temperature',
            'AttributeType': 'S'
        },
{
            'AttributeName': 'humidity',
            'AttributeType': 'S'
        }
    ]
)

table.meta.client.get_waiter('table_exists').wait(TableName='weather')

cities = pd.read_json('city.list.json')

cities_names = cities['name']

p = Pool()
result = p.map(get_weather, cities_names)

weather_df = pd.DataFrame(data=result, columns=['City', 'Temperature', 'Humidity'])

print(weather_df)

save_in_dynamo(table, weather_df)



