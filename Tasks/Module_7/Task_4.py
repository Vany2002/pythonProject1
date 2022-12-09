N = int(input())
l = []
max_N = N
count = 0

while N != 0:
    key = input()
    words = key.split(' ')
    for word in words:
        l.append(word)
    N -= 1

detour = 0
d = {}

while detour < len(l):
    key = l[detour]
    if key not in d:
        d[key] = 1
    else:
        d[key] += 1
    detour += 1

max_value = max(d.values())
d2 = {}
desired_value = 0
new_detour = 0

while new_detour < len(l):
    key = l[new_detour]
    if key not in d2:
        d2[key] = 1
    else:
        d2[key] += 1
        if d2[key] == max_value:
            desired_value = key
            break
    new_detour += 1

print(desired_value)