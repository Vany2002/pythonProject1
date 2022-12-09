l = {}
N = int(input())

while N != 0:
    place = input()
    key_1 = place.split(" ", 1)
    key_2 = str(key_1[:1])[2:-2]
    value_1 = place.split(" ", 1)
    value_2 = str(key_1[1:])[2:-2]

    l[key_2] = value_2
    N -= 1

l_Check = []
N = int(input())

while N != 0:
    place = input()
    key_1 = place.split(" ", 1)
    key_2 = str(key_1[:1])[2:-2]

    for key_1, value_1 in l.items():
        if key_2 in value_1:
            l_Check.append(key_1)

    N -= 1

for i in l_Check:
    print(i)