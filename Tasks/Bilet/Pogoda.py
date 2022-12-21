import urllib.request
import re

url = 'https://api.openweathermap.org/data/2.5/weather?q=Moscow&units=metric&lang=ru&appid=c341e34f9b7c327502cde34aa7817c5f'
resp = urllib.request.urlopen(url)
print(resp.read().decode('utf-8'))
resp = resp[1:-1]
pattern = r'(?:"\w+":+)'
info = re.findall(pattern, resp)
print(info)