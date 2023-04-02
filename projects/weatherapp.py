import requests
import json

city = input("Enter name of any city: ");

url = f'http://api.weatherapi.com/v1/current.json?key=362ebbf301d74aeabb364836230104&q={city}'

r = requests.get(url)

dict = json.loads(r.text)

temp = dict["current"]["temp_c"]
humidity = dict["current"]["humidity"]

print(f'''
    temperature : {temp}
    humidity : {humidity}
''')