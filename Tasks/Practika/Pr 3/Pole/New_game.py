import random

def con_game(words: list[str]) -> bool:
    if len(words) == 0:
        return False
    choice = input('������ ������� ���? ��/��� ')
    if choice == '��':
        return True
    if choice == '���':
        return False
    con_game(words)

def find_word(words: list[str]) -> str:
    print(words)
    word = random.choice(words)
    words.remove(word)
    return word