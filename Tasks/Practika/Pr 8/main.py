from translate import Translator

if __name__ == '__main__':
    with open("dialog.txt", "r") as file:
        text = file.read()
        text = text.lower()
        file.close()
    text_lst = text.split()
    dict = {}
    # Создание словаря {слово: кол-во употреблений}
    for i in text_lst:
        try:
            dict[i] = dict[i] + 1
        except:
            dict[i] = 0
    # Сортировка по убыванию значений
    sorted_values = sorted(dict.values(), reverse=True)
    sorted_dict = {}
    for i in sorted_values:
        for k in dict.keys():
            if dict[k] == i:
                sorted_dict[k] = dict[k]
                dict[k] = -1
    #Переводим слова и создаем список списков
    translated_lst = []
    for k, v in sorted_dict.items():
        trans = Translator(from_lang='ru', to_lang='en')
        word = trans.translate(k)
        translated_lst.append([k, word.lower(), v])
    #Создаем новый файл и записываем в него переводы
    with open("translated.txt", "w+") as file:
        for i in translated_lst:
            file.write(f"{i[0]} | {i[1]} | {i[2]} \n")
        file.close()
    print(translated_lst)