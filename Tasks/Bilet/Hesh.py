def get_strin():
    strin = input("������� ������: ")
    strin = strin.replace(" ", "").replace("-", "")
    strin = strin.title()
    if (strin[0] != "#") and (len(strin) < 140):
        strin = "#" + strin
    else:
        print("����������� ������� ������!")
        return get_strin()
i = 0
while True:
    i = int(input(""))
    if i == 1:
        get_strin()
        print("���������� ������...")
        break