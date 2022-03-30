class ComplexNumber:

    def __init__(self, a, b, *args):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b > 0:
            result = f'{self.a}+{self.b}j'
        else:
            result = f'{self.a}{self.b}j'
        return result

    def __add__(self, other):
        if self.b + other.b > 0:
            result = f'{self.a + other.a}+{self.b + other.b}j'
        else:
            result = f'{self.a + other.a}{self.b + other.b}j'
        return f'Cложение: {result}'

    def __sub__(self, other):
        if (self.b - other.b) > 0:
            result = f'{(self.a - other.a)}+{(self.b - other.b)}j'
        else:
            result = f'{(self.a - other.a)}{(self.b - other.b)}j'
        return f'Вычитание: {result}'

    def __mul__(self, other):
        if ((self.a * other.b) + (self.b * other.a)) > 0:
            result = f'{(self.a * other.a) - (self.b * other.b)}+{(self.a * other.b) + (self.b * other.a)}j'
        else:
            result = f'{(self.a * other.a) - (self.b * other.b)}{(self.a * other.b) + (self.b * other.a)}j'
        return f'Умножение: {result}'


z1 = ComplexNumber(2, 3)
z2 = ComplexNumber(-1, 1)
print(f'Число 1: {z1}')
print(F'Число 2: {z2}')
print(z1 + z2)
print(z1 - z2)
print(z1 * z2)
