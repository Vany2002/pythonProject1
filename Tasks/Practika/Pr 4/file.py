import re

def read_file(name: str) -> list[str]:
    file = open(name, 'r')
    text = file.read()
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    words = text.split()
    words = list(set(words))
    words.sort()
    file.close()
    return words

def save_file(name: str, words: list[str]) -> None:
    file = open(name, 'r')
    text = file.read()
    if len(text) != 0:
        file.seek(0)
        file.close()
        return 0

    file = open(name, 'a')
    file.write(f'Total words: {str(len(words))}\n\n')
    file.write('\n'.join(words))
    file.close()
words = read_file('data.txt')
save_file('count.txt', words)