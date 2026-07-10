class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def print_point(self):
        print(f"x = {self.x}, y = {self.y}")

p1 = Point(3, 4)
p2 = Point(5, 9)

p = p1 + p2
p.print_point()