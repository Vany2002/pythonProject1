class Car:
    def __init__(self, color="White", type="Pickup", year=2003):
        self.color = color
        self.type = type
        self.year = year

    def turn_on(self):
        print("Car started")

    def turn_off(self):
        print("Car stopped")

    def setColor(self, color):
        self.color = color

    def setType(self, type):
        self.type = type

    def setYear(self, year):
        self.year = year

    def printInfo(self):
        print("Color: ", self.color)
        print("Type: ", self.type)
        print("Year: ", self.year)

car = Car("Yellow", "Sedan", 2017)
car.printInfo()
car.turn_on()
car.turn_off()

car.setColor("Rad")
car.printInfo()