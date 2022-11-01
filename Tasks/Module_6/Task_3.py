a = [int(s) for s in input().split()]
for i in range(len(a) - 1):
    a[i], a[i + 1] = a[i + 1], a[i]
print(a)