a = input()
f = a.find('h')
l = a.rfind('h')
print(f'{a[:f]}{a[l:f:-1]}{a[l:]}')