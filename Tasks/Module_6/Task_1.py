s = input()
a = [int(s) for s in s.split()]
for i in a:
    if int(i) % 2 == 1:
       print(i, end=' ')