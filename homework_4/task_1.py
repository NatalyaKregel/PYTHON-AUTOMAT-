'''
Задача №1:
Напишите функцию для транспонирования матрицы
'''

# Способ №1 с использованием вложенного цикла

matrix_A = [[5,4,3],
            [3,4,5],
            [10,9,6]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for a in range(len(matrix_A)):
    for b in range(len(matrix_A[0])):
        result[b][a] = matrix_A[a][b]
print('Транспонированная матрица: ')        
print(result)


#Способ №2 с использованием функций

def print_matrix(m):
    for item in m:
        print(item)


def trans_matrix(matrix):
    temp = []
    for i in range(len(matrix[0])):
        temp_col = []
        for j in range(len(matrix)):
            temp_col.append(matrix[j][i])
        temp.append(temp_col)
    return temp


matrix = [[5,4,3],
          [3,4,5],
          [10,9,6]]
print_matrix(trans_matrix(matrix))











'''
Задача (доп) умножение матриц

matrix_A = [[5,4,3],
            [3,4,5],
            [10,9,6]]

matrix_B = [[2,1,3],
            [8,6,2],
            [1,3,5]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for m in range(len(matrix_A)):
    for n in range(len(matrix_B[0])):
        for p in range(len(matrix_B)):
            result[m][n] += matrix_A[m][p] * matrix_B[p][n]
print(result)
'''