import math

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * (self.r ** 2)


# Driver for custom testing
q = int(input())

for _ in range(q):
    parts = input().split()
    shape = parts[0]

    if shape == "rectangle":
        a, b = map(float, parts[1:])
        obj = Rectangle(a, b)

    elif shape == "circle":
        r = float(parts[1])
        obj = Circle(r)

    print(f"{obj.area():.2f}")
