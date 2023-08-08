'''
Задача 7:
Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
Создайте класс Матрица. Добавьте методы для:
    ○ вывода на печать,
    ○ сравнения,
    ○ сложения,
    ○ *умножения матриц
'''


class Matrix:
    """A matrix representation class with various operations on them"""

    def __init__(self, matrix: list[list] = []):
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        self.value = matrix

    def print_matrix(self):
        """A method that allows you to print the matrix to the console"""
        print('-' * self.columns * 2)
        for item in self.value:
            for elem in item:
                print(str(elem).center(4), end=' ')
            print()
        print('-' * self.columns * 2)

    def __str__(self):
        return f"The matrix contains: {self.value}"

    def __repr__(self):
        return f'Matrix({self.value})'

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.columns == other.columns:
                result = []
                for i in range(self.rows):
                    for j in range(self.columns):
                        result.append(self.value[i][j] == other.value[i][j])
                return all(result)
        return False

    def __lt__(self, other):
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.columns == other.columns:
                result = []
                for i in range(self.rows):
                    for j in range(self.columns):
                        result.append(self.value[i][j] < other.value[i][j])
                return all(result)
        return False

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.columns == other.columns:
                result = [[] for i in range(self.columns)]
                for i in range(self.columns):
                    for j in range(self.rows):
                        result[i].append(self.value[i][j] + other.value[i][j])
                return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.rows == other.rows:
                result = [[sum(a * b for a, b in zip(self_row, other_col))
                           for other_col in zip(*other.value)]
                          for self_row in self.value]
            elif self.columns == other.columns:
                result = [[sum(a * b for a, b in zip(self_col, other_row))
                           for self_col in zip(*self.value)]
                          for other_row in other.value]
            return Matrix(result)
        return False


if __name__ == '__main__':
    m1 = Matrix([[1, 2], [2, 4]])
    m1.print_matrix()
    print(m1)
    print(f'{m1 = }')

    m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
    m3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(m1 == m2)
    print(m1 == m3)
    print(m1 < m2)
    print(m1 > m2)
    add_matrix = m1 + m2
    add_matrix.print_matrix()
    mul_matrix = m1 * m2
    mul_matrix.print_matrix()