import re

def choose_complexity() -> int:
    choice = input('\nВыберите сложность: 1 - 3 жизни, 2 - 5 жизней, 3 - 7 жизней ')
    return (2 * int(choice) + 1) if choice == '1' or choice == '2' or choice == '3' else choose_complexity()

def check_input(word: str) -> str:
    n = input('\nВведите букву или слово: ')
    if re.findall(r'[а-яА-Я]', n) == []:
        check_input(word)
    return n

def play(word: str) -> int:
    max_live = choose_complexity()
    live = max_live
    print_word = []
    for i in range(len(word)):
        print_word.append('\u25A0')
    print(*print_word)
    while live > 0:
        n = check_input(word)
        if len(n) == 1:
            if n in word:
                for i in range(len(word)):
                    if word[i] == n:
                        print_word[i] = n
                print('Верно!')
                print(*print_word)
                if not print_word.__contains__('\u25A0'):
                    print(f'Вы выиграли!')
                    return max_live - live
            else:
                live -= 1
                print(f'Неверно!. Осталось {live} жизней')
                print(*print_word)
        elif n == word:
            print(f'Вы выиграли!')
            return max_live - live
        else:
            live -= 1
            print(f'Неверно!. Осталось {live} жизней')
            print(*print_word)
    print(f'Вы проиграли! Правильное слово: {word}')
    return max_live - live