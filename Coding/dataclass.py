from dataclasses import dataclass


# Normal Class Implementation
class Points:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Points(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Points(1, 2)
p2 = Points(2, 1)
print(p1, p2)
print(p1 == p2)


# Data Class Implementation
@dataclass
class Points:
    x: int
    y: int


p1 = Points(1, 2)
p2 = Points(2, 1)
print(p1, p2)
print(p1 == p2)