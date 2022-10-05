d = {}

while True:
    print("Добро пожаловать! Введите команды:\n0 - завершить программу\n1 - добавить контакат\n2 - удалить контакт\n3 - просмотреть телефонную книгу\n4 - изменить номер телефона")
    commands = input()

    if (commands < 0) and (commands > 4):
        print("Неверно введена команда!")
        continue

    if commands == 0:
        print("Завершение программы...")
        break

    if commands == 1:
        a = input()
        a.title()
        b = input()

        d[a] = b

        c = input("Всё? y/n")

        if c == 'y':
            break

        if commands == 2:



print(d)