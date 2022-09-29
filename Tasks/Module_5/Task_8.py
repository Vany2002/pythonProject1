prev = -1
x = 0
y = 0
a = int(input())
while a != 0:
    if prev == a:
        y += 1
    else:
        prev = a
        x = max(x, y)
        y = 1
    a = int(input())
x = max(x, y)
print(x)