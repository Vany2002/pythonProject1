import random
l = 3
while True:
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    print(f"{a} + {b} = ?")
    answer = input("Введите ответ: ")
    if not answer.isdigit():
        print("Введите число!")
        continue
    answer = int(answer)
    if answer != a + b:
        l = l - 1
        print(f"Неверный ответ, осталось {l} жизни")
    if l == 0:
        print("Проигрыш")

