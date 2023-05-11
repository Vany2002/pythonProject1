class SuperStr(str):
    def __init__(self, str):
        self.str = str

    def is_repeatance(self, string):
        if not isinstance(string, str):
            return False

        repeat = len(self) / len(string)

        if repeat != round(repeat):
            return False

        if string * int(repeat) != self:
            return False

        return True

    def is_palindrom(self):
        return self == self[::-1]