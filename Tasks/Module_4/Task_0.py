import random
a = random.randint(0, 100)
print(a)
b = random.randint(0, 100)
print(b)
s = a + b
print(s)
l = 3

while True:
    answer = input("Введите число: ")
    if not answer.isdigit():
        print("Введите число!")
        continue
    answer = int(answer)
    if answer != s:
        l = l - 1
        print("Неверный ответ")
    elif l == 0:
        print("Проигрыш")
        break
    else:
        print("Верный ответ")
        break