import urllib.request
from datetime import datetime
import re

url = 'https://api.openweathermap.org/data/2.5/weather?q=Moscow&units=metric&lang=ru&appid=c341e34f9b7c327502cde34aa7817c5f'
resp = urllib.request.urlopen(url)
resp = resp.read().decode('utf-8')
resp = resp[1:-1]

info = []

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
info.append(f'Time: {current_time}\n')

temp = re.findall(r'(?:temp":)([^,]+)', resp)
info.append(f'Temperature: {temp[0]}\n')

humidity = re.findall(r'(?:humidity":)([^,]+)', resp)
info.append(f'Air humidity: {humidity[0]}\n')

speed = re.findall(r'(?:speed":)([^,]+)', resp)
info.append(f'Wind speed: {speed[0]}\n')

pressure = re.findall(r'(?:pressure":)([^,]+)', resp)
info.append(f'Atmosphere pressure: {pressure[0]}\n')

name = re.findall(r'(?:name":")([^,]+)(?:")', resp)
info.append(f'City: {name[0]}\n')

for i in info:
    print(i)

f = open('text.txt', 'r+', encoding='utf-8')
f.write(f'Time: {current_time}\n')
f.write(f'City: {name[0]}\n')
f.write(f'Temperature: {temp[0]}\n')
f.write(f'Air humidity: {humidity[0]}\n')
f.write(f'Wind speed: {speed[0]}\n')
f.write(f'Atmosphere pressure: {pressure[0]}\n')