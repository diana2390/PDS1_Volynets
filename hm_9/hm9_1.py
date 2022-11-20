class Car:
    def __init__(self, brand, colour, engine_capacity):
        self.brand = brand
        self.colour = colour
        self.engine_capacity = engine_capacity

    def go_forward(self):
        print(f"The {self.brand} is going forward")

    def go_backwards(self):
        print(f"The {self.brand} is going backward")


class Car_2(Car):
    def turn_left(self):
        print(f"The {self.brand} is turning left")

    def turn_right(self):
        print(f"The {self.brand} is turning right")


car_1 = Car("BMW", "purple", 3000)

car_1.go_forward()
car_1.go_backwards()

car_2 = Car_2("Audi", "orange", 5000)
car_2.turn_left()
car_2.turn_right()
