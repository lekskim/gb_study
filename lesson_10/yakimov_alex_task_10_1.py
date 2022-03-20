import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        mat = ''
        for i in range(len(self.matrix)):
            mat = mat + '\t'.join(map(str, self.matrix[i])) + '\n'
        return mat

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return f'Матрицы разного размера'
        result = copy.deepcopy(self.matrix) #чтобы новая матрица сохраняла размерность слагаемых
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result)


m1 = [[1, 2, 3], [4, 5, 6], [1, 3, 4]]
m2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
m1 = Matrix(m1)
m2 = Matrix(m2)
print(m1)
print(m2)
m3 = m1 + m2
print(m3)
m4 = [[1, 1, 1], [1, 1, 1]]
m4 = Matrix(m4)
m5 = m3 + m4
print(m5)