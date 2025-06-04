def get_input_row():
    return input()

def get_matrix_rows(num_rows):
    return [get_input_row() for _ in range(num_rows)]

def reverse_matrix_rows(matrix):
    return matrix[::-1]

def zip_matrix_rows(matrix):
    return list(zip(*matrix))

def convert_matrix_tuples_to_strings(matrix):
    return [''.join(row) for row in matrix]

def print_rotation_degree(degree):
    print(degree)

def print_matrix_row(row):
    print(row, end='')
    print()

def print_matrix(matrix):
    for row in matrix:
        print_matrix_row(row)

def rotate_and_print(matrix, n):
    degree = 90 * n
    print_rotation_degree(degree)
    str_matrix = convert_matrix_tuples_to_strings(matrix)
    print_matrix(str_matrix)

def perform_rotation(matrix, n):
    reversed_rows = reverse_matrix_rows(matrix)
    rotated = zip_matrix_rows(reversed_rows)
    return rotated

def main():
    m = get_matrix_rows(8)
    for i in range(3):
        m = perform_rotation(m, i)
        rotate_and_print(m, i + 1)

main()