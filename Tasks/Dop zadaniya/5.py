from math import pi
def deg_to_gms(deg, formats='string'):
    d = int(deg)
    m = int((deg - d) * 60)
    s = ((((deg - d) * 60) - m) * 60)
    s = round(s, 5)

    if formats == 'string':
        answer = f'{d}°, {m}’, {s}”'
    elif formats == 'num':
        answer = (d, m, s)
    else:
        answer = None
    return answer

def gms_to_deg(d, m, s):
    return d + (m / 60) + (s / 3600)

def deg_to_rad(deg):
    return deg * (pi / 180)

def rad_to_deg(rad):
    return rad * (180 / pi)

print(deg_to_gms(36.97, formats='num'))
print(gms_to_deg(36, 58, 12))
print(deg_to_rad(36.97))
print(rad_to_deg(deg_to_rad(36.97)))