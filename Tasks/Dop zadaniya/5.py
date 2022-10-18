def deg_to_gms(deg, formats='string'):
    d = int(deg)
    m = int((deg - d) * 60)
    s = (deg - d - m / 60) * 3600.00
    s = round(s, 2)
    if formats == 'string':
        answer = f'{d}°, {m}, {s}'
    elif formats == 'num':
        answer = (d, m, s)
    else:
        answer = None