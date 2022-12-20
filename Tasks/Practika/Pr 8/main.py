import re
import pymorphy2
from translate import Translator
import translate

def read_file(filename: str):
    f = open(filename, 'r', encoding='utf-8')
    words = f.read()
    words = re.sub(r'[^\w\s]', '', words)
    words = re.sub(r"\d+", '', words)
    return words.split()

def list_words(words: [str]):
    wordsCount = {}

    for word in words:
        if len(word) > 1:
            if not word in wordsCount:
                wordsCount[word] = 0
            wordsCount[word] += 1

    sorted_words = {}
    sorted_keys = sorted(wordsCount, key=wordsCount.get)
    sorted_keys.reverse()

    for values in sorted_keys:
        sorted_words[values] = wordsCount[values]

    return sorted_words

def translate(words: {}):
    morph = pymorphy2.MorphAnalyzer()
    translator = Translator(from_lang="ru", to_lang="en")

    translate_words = {}
    for key, value in words.items():
        en_word = str
        try:
            normal_word = morph.parse(key)[0].normal_form
            en_word = translator.translate(normal_word)
            if en_word == None:
                raise Exception
        except:
            en_word = 'untranslated'

        print(en_word)
        translate_words[en_word] = value

    return translate_words


def write_file(filename, translate_words: {}, sorted_words: {}):
    ru_words = []
    en_words = []
    words_count = []

    for key, value in sorted_words.items():
        ru_words.append(key)

    for key, value in translate_words.items():
        en_words.append(key)
        words_count.append(value)

    f = open(filename, 'a')
    for i in range(len(translate_words)):
        line = "{0} - {1} {2} \n".format(en_words[i], ru_words[i], words_count[i])
        f.write(line)

words = read_file('dialog.txt')
sorted_words = list_words(words)
transleted_words = translate(sorted_words)
write_file('TranslatedWords.txt', transleted_words, sorted_words)