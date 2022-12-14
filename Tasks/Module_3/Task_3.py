a = input()
if a.count('f') == 1:
    print(a.find('f'))
elif a.count('f') >= 2:
    print(a.find('f'), a.rfind('f'))
