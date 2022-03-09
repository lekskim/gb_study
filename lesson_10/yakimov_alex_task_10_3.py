class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Сложение: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Вычитание: {sub}' if sub > 0 else 'Разность отрицательная'

    def __floordiv__(self, other):
        return f'Деление: {self.quantity // other.quantity}'

    def __mul__(self, other):
        return f'Умножение: {self.quantity * other.quantity}'

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell_1 = Cell(12)
cell_2 = Cell(10)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 // cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(5))

cell_1 = Cell(33)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 // cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(5))

cell_1 = Cell(15)
cell_2 = Cell(4)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 // cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(5))

cell_1 = Cell(16)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 // cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(5))

cell_1 = Cell(2)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 // cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(5))