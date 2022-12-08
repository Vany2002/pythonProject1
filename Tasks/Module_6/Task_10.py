a = input()
a_1 = list(a)
a_2 = a_1[0: a_1.index("h")]
a_1.reverse()
a_3 = a_1[0: a_1.index("h")]
a_3.reverse()
a_2.append("".join(map(str, a_3)))
print("".join(map(str, a_2)))