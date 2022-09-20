a = input()
b = a.find(' ')
print(a[b + 1:] + a[b] + a[:b])