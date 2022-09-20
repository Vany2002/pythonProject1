a = int(input())
b = a // 10 % 10
if a // 100 < b < a % 10:
    print("Да")
else:
    print("Нет")