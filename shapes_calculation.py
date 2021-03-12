# Hangyu Chen

import math

# Shape class and other shapes classes. Each class override the area and perimeter in shape class to calculate area and
# perimeter in each shape type.

#%% part 1
# init method takes arguments as key <- value, str method returns attributes
class Shape:
    def __init__(self, **kwargs): # **kwargs takes in unknown numbers of arguments
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        info = ""
        for attribute, value in self.__dict__.items():
            info += attribute + " : " + "%f" %(value)

        return self.__class__.__name__ + " " + info


# Rectangle attributes: length, width
class Rectangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def find_area(self):
        self.area = self.length * self.width

    def find_perimeter(self):
        self.perimeter = 2 * (self.length + self.width)

# Oval attributes: major, minor
class Oval(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def find_area(self):
        self.area = math.pi * self.major * self.minor

    def find_perimeter(self):
        self.perimeter = math.pi * (3 * (self.major + self.minor) - math.sqrt((3 * self.major + self.minor) * (self.major + 3 * self.minor)))

# Polygon attributes: sides, length
class Polygon(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def find_area(self):
        self.area = self.sides * self.length ** 2 * (math.tan(math.pi / self.sides) ** -1) / 4

    def find_perimeter(self):
        self.perimeter = self.sides * self.length

# Square attributes: length
class Square(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def find_area(self):
        self.area = self.length ** 2

    def find_perimeter(self):
        self.perimeter = 4 * self.length

# Triangle attributes: base, height, leg_a, leg_b
class Triangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def find_area(self):
        self.area = 0.5 * self.base * self.height

    def find_perimeter(self):
        self.perimeter = self.base + self.leg_a + self.leg_b

# Pentagon attributes: length
class Pentagon(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def find_area(self):
        self.area = 5 * self.length ** 2 * (math.tan(math.pi / 5) ** -1) / 4

    def find_perimeter(self):
        self.perimeter = 5 * self.length

# Circle attributes: radius
class Circle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def find_area(self):
        self.area = math.pi * self.radius ** 2

    def find_perimeter(self):
        self.perimeter = (math.pi * self.radius) + (2 * self.radius)

# Parallelogram attributes: length, height, width
class Parallelogram(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def find_area(self):
        self.area = self.length * self.height

    def find_perimeter(self):
        self.perimeter = 2 * (self.length + self.width)

# Rhombus attributes: diagonal_1, diagonal_2, length
class Rhombus(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def find_area(self):
        self.area = 0.5 * self.diagonal_1 * self.diagonal_2

    def find_perimeter(self):
        self.perimeter = 4 * self.length



if __name__ == '__main__':
    rect = Rectangle(length=2, width=2) # test run a rectangle calculation
    rect.find_area()
    rect.find_perimeter()



#%% part 2
suits = ['hearts', 'diamonds', 'spades', 'clubs']
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# zip function to create a list of a standard set of cards
cards = [(s, v) for s in zip(suits) for v in zip(values)]



