import random
l = 3
o = 0

while True:
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    S = a + b
    print(f"{a} + {b} = ?")
    answer = input("Введите ответ: ")
    if not answer.isdigit():
        print("Введите число!")
        continue
    answer = int(answer)
    if answer == S:
        o += 1
    else:
        l -= 1
        if l == 0:
            print(f"Набрано очков: {o}")
            break
        else:
            print(f"Жизни: {l}, Ошибка")