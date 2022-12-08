a = [int(s) for s in input().split()]
b = [int(p) for p in input().split()]
counter = 0
for i in range(0, len(a)):
    for j in range(0, len(b)):
        if a[i] == b[j]:
            counter += 1
print(counter)