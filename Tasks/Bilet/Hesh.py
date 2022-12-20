import re

def get_hash_tag(input_string):
    if len(input_string) > 140 or len(input_string) == 0:
        return False

    input_string = re.sub(r'[^\w\s]', '', input_string)

    result = input_string.title()
    result = result.replace(' ', '')
    return f'#{result}'

print(get_hash_tag('weviruv wevnon; rwn;erow rweoi;'))




