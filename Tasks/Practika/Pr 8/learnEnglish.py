import re
import pymorphy2
from translate import Translator

def read_file(filename: str):
    f = open(filename, 'r', encoding='utf-8')
    words = f.read()
    words = re.sub(r'[^\w\s]', '', words)
    words = re.sub(r"\d+", '', words)
    return words.split()

def list_words(words: [str]):
    wordsCount = {}

    for word in words:
        if not word in wordsCount:
            wordsCount[word] = 0
        wordsCount[word] += 1

    sorted_dict = {}
    sorted_keys = sorted(wordsCount, key=wordsCount.get)
    sorted_keys.reverse()

    for values in sorted_keys:
        sorted_dict[values] = wordsCount[values]

    return sorted_dict

def translate(words: {}):
    morph = pymorphy2.MorphAnalyzer()
    translator = Translator(from_lang="russian", to_lang="english")

    translate_words = {}
    for key, value in words.items():
        normal_word = morph.parse(key)[0].normal_form
        en_word = translator.translate(normal_word)
        translate_words[en_word] = value
        print(en_word)

    return translate_words


def write_file(filename, translate_words: {}, sorted_words: {}):
    f = open(filename)

    for i in range(len(sorted_words)):
        line = f'{translate_words.keys()[i]}, {sorted_words.keys()[i]} - {sorted_words[i]}'
        print(line)

words = read_file('dialog.txt')
sorted_words = list_words(words)
transleted_words = translate(sorted_words)
write_file('TranslatedWords.txt', transleted_words, sorted_words)

print(sorted_words)
print(transleted_words)