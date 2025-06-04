def get_input_line():
    return input()

def parse_ints_from_line(line):
    return list(map(int, line.split()))

def read_dimensions():
    line = get_input_line()
    return parse_ints_from_line(line)

def read_matrix_row():
    line = get_input_line()
    return parse_ints_from_line(line)

def read_matrix(rows):
    matrix = []
    for _ in range(rows):
        matrix.append(read_matrix_row())
    return matrix

def init_result_row():
    return []

def compute_dot_product(a_row, b_col):
    s = 0
    for x, y in zip(a_row, b_col):
        s += x * y
    return s

def extract_column(matrix, col_idx):
    col = []
    for row in matrix:
        col.append(row[col_idx])
    return col

def compute_result_row(a_row, b_matrix, l):
    result_row = init_result_row()
    for j in range(l):
        col = extract_column(b_matrix, j)
        val = compute_dot_product(a_row, col)
        result_row.append(val)
    return result_row

def format_row(row):
    return ' '.join(map(str, row))

def print_matrix_result(matrix):
    for row in matrix:
        print(format_row(row))

def matrix_multiplication():
    n, m, l = read_dimensions()
    A = read_matrix(n)
    B = read_matrix(m)
    result = []
    for i in range(n):
        a_row = A[i]
        result_row = compute_result_row(a_row, B, l)
        result.append(result_row)
    print_matrix_result(result)

matrix_multiplication()