a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]

for i in range(len(a)):
    if (b.count(a[i]) > 0):
        print(a[i])