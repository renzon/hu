import math


class Vetor():
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def __repr__(self):
        return 'Vetor({x!r},{y!r})'.format(**self.__dict__)

    def __add__(self, other):
        return Vetor(self.x + other.x, self.y + other.y)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


v = Vetor(2, 4)
v2 = Vetor(2, 1)

print(v + v2)
print(abs(v))
