def parse_input_line(e):
    return map(int, e.split())

def create_cell():
    return [1, 0, 1, 0]

def create_row(h):
    return [create_cell() for _ in range(h)]

def create_matrix(w, h):
    return [create_row(h) for _ in range(w)]

def get_matrix_element(M, i, j):
    return M[i][j]

def get_prev_left(M, i, j):
    return M[i - 1][j][:2]

def get_prev_above(M, i, j):
    return M[i][j - 1][2:]

def merge_cells(a, b, c, d):
    return [d, a + b, b, c + d]

def update_matrix_cell(M, i, j):
    a, b = get_prev_left(M, i, j)
    c, d = get_prev_above(M, i, j)
    M[i][j] = merge_cells(a, b, c, d)

def fill_matrix(M, w, h):
    for i in range(1, w):
        for j in range(1, h):
            update_matrix_cell(M, i, j)

def get_result(M, w, h):
    left = sum(M[w-2][h-1][:2])
    above = sum(M[w-1][h-2][2:])
    return (left + above) % 10**5

def process_input_line(e):
    w, h = parse_input_line(e)
    M = create_matrix(w, h)
    fill_matrix(M, w, h)
    result = get_result(M, w, h)
    print(result)

def main():
    for e in iter(input, '0 0'):
        process_input_line(e)

main()