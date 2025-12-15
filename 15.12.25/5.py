# Напишите программу, которая с помощью модуля random перемешивает 
# случайным образом содержимое матрицы (двумерного списка).

import random

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

row = []
for i in range(len(matrix)):
    row.extend(matrix[i])
random.shuffle(row)

matrix[:] = []
for i in range(4):
    new_row = row[i*4:(i+1)*4]
    matrix.append(new_row)




