s = input()
a = [int(s) for s in s.split()]
for i in a:
    if [i] < [i + 1]:
        t = [i + 1]
        print(t, end=' ')
