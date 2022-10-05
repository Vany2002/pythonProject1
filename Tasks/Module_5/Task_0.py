import random
not_change = 0
change = 0
for i in range(100000):
    a = [0, 0, 1]
    choice = random.randint(0, 2)
    a.pop(choice)
    a.remove(0)
    if a[0] == 1:
        not_change += 1
    else:
        change += 1
print(f'Вероятность если поменять выбор: {not_change/1000} %\nВероятность есди не менять выбор: {change/1000} %')