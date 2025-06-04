def create_zero_matrix_rows(n):
    return [0] * n

def add_row_to_matrix(matrix, row):
    matrix.append(row)
    return matrix

def build_zero_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        matrix = add_row_to_matrix(matrix, create_zero_matrix_rows(cols))
    return matrix

def get_input():
    return raw_input()

def split_string(s):
    return s.split(" ")

def convert_strings_to_ints(strings):
    return map(int, strings)

def get_int_list_from_input():
    s = get_input()
    ss = split_string(s)
    return convert_strings_to_ints(ss)

def read_matrix(n_rows, n_cols):
    matrix = build_zero_matrix(n_rows, n_cols)
    for i in range(n_rows):
        input_row = get_int_list_from_input()
        for j in range(n_cols):
            matrix[i][j] += input_row[j]
    return matrix

def multiply_matrices(A, B, n, m, p):
    C = build_zero_matrix(n, p)
    for i in range(n):
        for j in range(p):
            val = 0
            for l in range(m):
                val += A[i][l] * B[l][j]
            C[i][j] += val
    return C

def print_matrix_row(row, last_index):
    for j in range(len(row)):
        if j == last_index:
            print row[j]
        else:
            print row[j],

def print_matrix(matrix):
    for row in matrix:
        print_matrix_row(row, len(row) - 1)

def main():
    k_list = get_int_list_from_input()
    n = k_list[0]
    m = k_list[1]
    p = k_list[2]
    A = read_matrix(n, m)
    B = read_matrix(m, p)
    C = multiply_matrices(A, B, n, m, p)
    print_matrix(C)

main()