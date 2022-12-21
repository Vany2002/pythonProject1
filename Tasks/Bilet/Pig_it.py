def pig_it(input_line):
    input_words = input_line.split(' ')

    result_words = []
    for word in input_words:
        result_words.append(f'{word[1:]}{word[0]}ay')

    return ' '.join(result_words)


print(pig_it('Pig latin is cool'))