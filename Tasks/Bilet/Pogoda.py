import urllib.request
from datetime import datetime
import re

url = 'https://api.openweathermap.org/data/2.5/weather?q=Moscow&units=metric&lang=ru&appid=c341e34f9b7c327502cde34aa7817c5f'
resp = urllib.request.urlopen(url)
resp = resp.read().decode('utf-8')
resp = resp[1:-1]

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

town = re.findall(r'(?:name":)([^,]+)', resp)

temp = re.findall(r'(?:temp":)([^,]+)', resp)

humidity = re.findall(r'(?:humidity":)([^,]+)', resp)

speed = re.findall(r'(?:speed":)([^,]+)', resp)

pressure = re.findall(r'(?:pressure":)([^,]+)', resp)


print(f'�����: {now} \n'
    '�����: {town} \n'
    '�����������: {temp} \n'
    '���������: {humidity} \n'
    '�������� �����: {speed} \n'
    '��������: {pressure}')


f = open('text.txt', 'r+', encoding='utf-8')
f.write(f'[{now}] ������ ������ � ������: {town}')
f.write(f'�����������: {temp}')
f.write(f'��������� �������: {humidity}')
f.write(f'�������� �����: {speed}')
f.write(f'����������� ��������: {pressure}')
