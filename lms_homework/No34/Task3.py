import datetime

import requests
weather_lof_data = 'weather_lof_data.txt'
api_key = '30d4741c779ba94c470ca1f63045390a'

user_input = input("You city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No city found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {round(((temp - 32) * 5) / 9, 2)} ºC")
    print(f"Save full data of weather in text-file: '{weather_lof_data}'")

    with open(weather_lof_data, 'a') as f:
        f.write(f'Query of Weather in {user_input} at ({datetime.datetime.now()}) :\n')
        f.write(str(weather_data.json()))
        f.write('\n')
