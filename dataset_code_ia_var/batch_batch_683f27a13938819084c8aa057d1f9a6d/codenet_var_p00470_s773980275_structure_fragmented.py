def read_input():
    return iter(input, '0 0')

def parse_dimensions(e):
    w, h = map(int, e.split())
    return w, h

def create_cell():
    return [1, 0, 1, 0]

def create_row(h):
    return [create_cell() for _ in range(h)]

def create_matrix(w, h):
    return [create_row(h) for _ in range(w)]

def extract_previous_values(M, i, j):
    prev_row = M[i-1][j][:2]
    prev_col = M[i][j-1][2:]
    return prev_row + prev_col

def compute_cell_values(values):
    a, b, c, d = values
    return [d, a+b, b, c+d]

def update_matrix(M, w, h):
    for i in range(1, w):
        for j in range(1, h):
            vals = extract_previous_values(M, i, j)
            M[i][j] = compute_cell_values(vals)

def sum_two_first(L):
    return sum(L[:2])

def sum_two_last(L):
    return sum(L[2:])

def print_result(M, w, h):
    total = sum_two_first(M[w-2][h-1]) + sum_two_last(M[w-1][h-2])
    print(total % (10**5))

def process_case(e):
    w, h = parse_dimensions(e)
    M = create_matrix(w, h)
    update_matrix(M, w, h)
    print_result(M, w, h)

def main():
    for e in read_input():
        process_case(e)

main()