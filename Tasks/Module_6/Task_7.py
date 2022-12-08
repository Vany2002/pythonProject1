a = [int(s) for s in input().split()]

for i in range(len(a)):
    if (a.index(a[i]) < i):
        print("Да")
    else:
        print("Нет")