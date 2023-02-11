class Car:
    amount_of_cars = 0
    def __init__(self, brand="BMW", model="X7", color="Dark Blue", cost=50, plate="ABC12345"):
        self.brand = brand
        self.model = model
        self.color = color
        self.cost = cost
        self.total_value = cost*1000
        self.plate = plate
        Car.amount_of_cars += 1

    def __str__(self):
        return f"A {self.color} {self.brand} {self.model} is ${self.cost}/per day"

    def __del__(self):
       print(f"{self.brand} sold")


    def rent_out(self):
        self.total_value = self.total_value - (self.cost * 0.1)
        print(f"{self.brand} rented out!")



first_car = Car()

second_car = Car("Subaru", "Outback", "Green", 40, "XYZ98765")

print(second_car)