import re
from io import TextIOWrapper

import pymorphy2
from translate import Translator

translator = Translator(from_lang="ru", to_lang="en")
morph = pymorphy2.MorphAnalyzer()


def get_normal_form():

    requested_file: TextIOWrapper = open('dialog.txt', mode='r+', encoding='utf-8')
    content: str = requested_file.read()
    content: str = content.lower()
    good_chars_pattern: str = r"(?:\я|\w+[^(\W|\d)]+)"
    match_words: list = re.findall(good_chars_pattern, content)
    return match_words


def get_dict():

    list_of_words: list = get_normal_form()
    dict_of_words: dict = {}

    for word in list_of_words:
        if word in dict_of_words:
            dict_of_words[word] += 1
        else:
            dict_of_words[word] = 1

    return dict_of_words


def translation_and_formating():

    dict_of_words: dict = get_dict()
    sorted_dict_of_words: dict = dict(sorted(dict_of_words.items()))
    sorted_list_of_words: list = sorted(sorted_dict_of_words, key=sorted_dict_of_words.get, reverse=True)
    result_file = open('word_translation.txt', mode='w+', encoding='utf-8')

    for word in sorted_list_of_words:
        for key, value in sorted_dict_of_words.items():
            if word == key:
                morph_word: pymorphy2.analyzer.Parse = morph.parse(word)[0]
                word: str = morph_word.normal_form
                word_translated: str = translator.translate(word)
                result_file.write(str(word))
                result_file.write("|")
                result_file.write(str(word_translated))
                result_file.write("|")
                result_file.write(str(value))
                result_file.write('\n')

    return "\n===Данные отформатированы и сохранены в указанный файл===\n"