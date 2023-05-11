class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b if not self.b == 0 else 0

    def subtraction(self):
        return self.a - self.b

math = Math(237, 23)
print(math.addition())
print(math.multiplication())
print(math.division())
print(math.subtraction())