matrix_power = int(input())

matrix = []

for _ in range(0, matrix_power):
    input_row = input()
    row = [int(element) for element in input_row if element != ' ']
    matrix.append(row)

transparent = []

for i in range(0, matrix_power):
    time = []
    for j in range(0, matrix_power):
        time.append(matrix[j][i])
    transparent.append(time)

if transparent == matrix:
    print('yes')
else:
    print('no')