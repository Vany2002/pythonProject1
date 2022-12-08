a = [int(s) for s in input().split()]
max = -10000000
min = 10000000
for i in range(0, len(a)):
    if a[i] > max:
        max = a[i]
    elif a[i] < min:
        min = a[i]
index_of_max_num = a.index(max)
index_of_min_num = a.index(min)
a[index_of_min_num], a[index_of_max_num] = a[index_of_max_num], a[index_of_min_num]
print(" ".join(map(str, a)))