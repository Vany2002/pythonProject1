import random

def monty(iter = 10000):
    not_change = 0
    change = 0
    for i in range(iter):
        a = [0, 0, 1]
        choice = random.randint(0, 2)
        a.pop(choice)
        a.remove(0)
        if a[0] == 1:
            not_change += 1
        else:
            change += 1
    return(f'Вероятность если поменять выбор: {not_change / 100}%\nВероятность если не менять выбор: {change / 100}%')