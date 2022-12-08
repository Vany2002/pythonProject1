import math
a = input()
a_1 = list(a)
k = float(len(a_1)) / 2
max = math.ceil(k)
a_2 = a_1[max: len(a_1)] + a_1[0: max]
print("".join(map(str, a_2)))