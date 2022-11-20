class Parallelogram:
    def __init__(self, width, length=None):
        self.width = width
        self.length = length

    def get_area(self):
        print(self.width * self.length)


pal_1 = Parallelogram(12, 24)
pal_1.get_area()


class Square(Parallelogram):
    def get_area(self):
        print(self.width ** 2)


square_2 = Square(10)
square_2.get_area()
