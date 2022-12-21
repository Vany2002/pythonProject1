import re

def pig_it(input_line):
    input_words = input_line.split(' ')

    result_words = []
    for word in input_words:
        clear_word = re.sub(r'[^\w\s]', '', word)
        special_symbols = re.sub(r'[A-Za-z]', '', word)

        if len(clear_word) > 1:
            result_words.append(f'{clear_word[1:]}{clear_word[0]}ay{special_symbols}')
        elif len(clear_word) == 1:
            result_words.append(f'{clear_word}ay{special_symbols}')
        else:
            result_words.append(special_symbols)

    return ' '.join(result_words)


print(pig_it('Pig latin, is cool !'))