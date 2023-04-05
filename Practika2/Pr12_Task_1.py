# coding=<encoding name>
class Student:
    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber

    def printInfo(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("GroupNumber: ", self.groupNumber)

Alex = Student("Alex", 20, "11B")
Alex.printInfo()
print("")

Peter = Student("Peter", 17, "10B")
Peter.printInfo()
print("")

Vitya = Student()
Vitya.setNameAge("Vitya", 19)
Vitya.setGroupNumber("11A")
Vitya.printInfo()
print("")

Gena = Student("Gena", 16)
Gena.setGroupNumber("10A")
Gena.printInfo()
print("")

Dima = Student()
Dima.setNameAge("Dima", 18)
Dima.setGroupNumber("11A")
Dima.printInfo()