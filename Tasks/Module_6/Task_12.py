a = input()
f = a.find('h')
l = a.rfind('h')
print(f'{a[:f+1]}{a[f+1:l].replace("h", "H")}{a[l:]}')