a = int(input())
b = int(input())
if b == 31:
    a = a + 1
    b = b - 30
    print(f"{b}-{a}-2022")
elif a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
    print(f"{b + 1}-{a}-2022")
if b == 28:
    a = 3
    b = b - 27
    print(f"{b}-{a}-2022")
elif a == 2:
    print(f"{b + 1}-{a}-2022")
if b == 30:
    a = a + 1
    b = b - 29
    print(f"{b}-{a}-2022")
elif a == 4 or a == 6 or a == 9 or a == 11:
    print(f"{b + 1}-{a}-2022")