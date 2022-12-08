a = [int(s) for s in input().split()]
i = 1
while i < len(a):
    a[i - 1], a[i] = a[i], a[i - 1]
    i += 2
print(" ".join(map(str, a)))