matrix_size = int(input())
matrix_data = [[] for _ in range(matrix_size)]

for row_index in range(matrix_size):
    input_row = list(map(int, input().split()))
    matrix_data[row_index] = input_row

for pivot_index in range(matrix_size):
    for from_index in range(matrix_size):
        for to_index in range(matrix_size):
            if matrix_data[from_index][to_index] > matrix_data[from_index][pivot_index] + matrix_data[pivot_index][to_index]:
                print('-1')
                exit()

total_sum = 0
for from_index in range(matrix_size):
    for to_index in range(from_index + 1, matrix_size):
        for via_index in range(matrix_size):
            if via_index == from_index or via_index == to_index:
                continue
            if matrix_data[from_index][to_index] == matrix_data[from_index][via_index] + matrix_data[via_index][to_index]:
                break
        else:
            total_sum += matrix_data[from_index][to_index]

print(total_sum)