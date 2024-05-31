class Triangle:
    def __init__(self, a_pm: int, b_pm: int, c_pm: int):
        self.a = a_pm
        self.b = b_pm
        self.c = c_pm

    def perimeter(self):
        perimeter1 = self.a + self.b + self.c
        return perimeter1

    def square(self):
        p = self.perimeter() / 2
        square1 = (p * (self.a) * (self.b) * (self.c)) ** 0.5
        return square1


t1 = Triangle(5, 10, 8)

print(t1.perimeter())
print(t1.square())