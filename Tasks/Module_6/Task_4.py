a = [int(s) for s in input().split()]
for i in range(len(a) - 1):
    print(max(a), min(a))