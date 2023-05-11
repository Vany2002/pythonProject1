from Practika2.Pr_13.Pr13_Task_2 import SuperStr

s = SuperStr("123123123123")
print(s.is_repeatance("123"))
print(s.is_repeatance("123123"))
print(s.is_repeatance("123123123123"))
print(s.is_repeatance("12312"))
print(s.is_repeatance(123))
print(s.is_palindrom())
print(s)
print(int(s))
print(s + "qwe")
p = SuperStr("123_321")
print(p.is_palindrom())