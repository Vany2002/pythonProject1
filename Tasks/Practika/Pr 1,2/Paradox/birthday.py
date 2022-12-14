import random
def birth(iter = 10000, c_ch = 23):
    for p in range(c_ch):
        st = 0
        for k in range(iter):
            birthday = []
            for i in range(0, p):
                bday = random.randrange(0, 365)
                birthday.append(bday)
            set_of_bdays = set(birthday)
            if len(set_of_bdays) < len(birthday):
                st += 1
    rez = st/10000
    return(f"Парадокс дня рождения: {rez}")