def read_dimensions():
    return map(int, input().split())

def initialize_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def read_row(cols):
    return list(map(int, input().split()))

def assign_row(matrix, row_idx, values):
    for col_idx in range(len(values)):
        matrix[row_idx][col_idx] = values[col_idx]

def read_matrix(rows, cols):
    matrix = initialize_matrix(rows, cols)
    for i in range(rows):
        row_values = read_row(cols)
        assign_row(matrix, i, row_values)
    return matrix

def multiply_matrices(a, b, n, m, l):
    c = initialize_matrix(n, l)
    fill_result_matrix(c, a, b, n, m, l)
    return c

def compute_cell(a, b, i, j, m):
    total = 0
    for x in range(m):
        total += a[i][x] * b[x][j]
    return total

def fill_result_matrix(c, a, b, n, m, l):
    for i in range(n):
        fill_result_row(c, a, b, i, m, l)

def fill_result_row(c, a, b, i, m, l):
    for j in range(l):
        c[i][j] = compute_cell(a, b, i, j, m)

def print_matrix(matrix, n, l):
    for i in range(n):
        print_matrix_row(matrix, i, l)

def print_matrix_row(matrix, i, l):
    for j in range(l):
        print_matrix_cell(matrix, i, j, l)

def print_matrix_cell(matrix, i, j, l):
    if j == (l - 1):
        print(matrix[i][j])
    else:
        print(matrix[i][j], "", end = "")

def main():
    n, m, l = read_dimensions()
    a = read_matrix(n, m)
    b = read_matrix(m, l)
    c = multiply_matrices(a, b, n, m, l)
    print_matrix(c, n, l)

main()