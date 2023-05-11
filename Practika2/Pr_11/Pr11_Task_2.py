import urllib.request
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
input = urllib.request.urlopen("https://quke.ru/shop/smartfony/apple?page-size=72").read().decode()

price_pattern = r'(?:<span class="b-card2-v2__price-val">)([^<]+)'
price = re.findall(price_pattern, input)
print(price)

phone_pattern = r'(?:<a class="b-card2-v2__name" href=")(?:[^\"]+)(?:" title=")([^\"]+)'
phone = re.findall(phone_pattern, input)
print(phone)

phone_price = dict(map(lambda x, y: (x, int(y.replace(" ", ""))), phone, price))
phone_count = 72

minimum = min(phone_price.values())
maximum = max(phone_price.values())
average = round(sum(phone_price.values()) / phone_count)

print(minimum)
print(maximum)
print(average)

f = open("catalog.csv", 'w')
for n, p in phone_price.items():
    f.write(f'{n}: {p}\n')

f.write(f'\nmin: {str(minimum)} \n')
f.write(f'max: {str(maximum)} \n')
f.write(f'average: {str(average)} \n')