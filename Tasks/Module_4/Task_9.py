a = int(input())
b = int(input())
c = int(input())
if a == b and a == c:
    print(3)
elif a == b and a != c or a == c and a != b or b == a and b != c or b == c and b != a:
    print(2)
else:
    print(0)