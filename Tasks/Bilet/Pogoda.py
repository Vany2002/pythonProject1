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
info.append(current_time)

temp = re.findall(r'(?:temp":)([^,]+)', resp)
info.append(temp)

humidity = re.findall(r'(?:humidity":)([^,]+)', resp)
info.append(humidity)

speed = re.findall(r'(?:speed":)([^,]+)', resp)
info.append(speed)

pressure = re.findall(r'(?:pressure":)([^,]+)', resp)
info.append(pressure)

name = re.findall(r'((?:name":)([^,]+))', resp)
info.append(name)

for i in info:
    print(i)

f = open('text.txt', 'r+', encoding='utf-8')
for i in info:
    f.write(i)