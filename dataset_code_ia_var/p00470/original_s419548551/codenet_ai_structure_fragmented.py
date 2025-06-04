def get_input():
    return iter(input, '0 0')

def parse_dimensions(line):
    return map(int, line.split())

def create_cell():
    return [1, 0, 1, 0]

def create_row(h):
    return [create_cell() for _ in range(h)]

def create_matrix(w, h):
    return [create_row(h) for _ in range(w)]

def extract_top_left(cell):
    return cell[:2]

def extract_bottom_right(cell):
    return cell[2:]

def compute_cell(left_cell, top_cell):
    a, b = extract_top_left(left_cell)
    c, d = extract_bottom_right(top_cell)
    return [d, a + b, b, c + d]

def fill_matrix(M, w, h):
    for i in range(1, w):
        for j in range(1, h):
            left_cell = M[i - 1][j]
            top_cell = M[i][j - 1]
            M[i][j] = compute_cell(left_cell, top_cell)

def sum_top_left_last_col(M, w, h):
    return sum(extract_top_left(M[w - 2][h - 1]))

def sum_bottom_right_last_row(M, w, h):
    return sum(extract_bottom_right(M[w - 1][h - 2]))

def final_sum(M, w, h):
    return (sum_top_left_last_col(M, w, h) + sum_bottom_right_last_row(M, w, h)) % 10 ** 5

def process_case(e):
    w, h = parse_dimensions(e)
    M = create_matrix(w, h)
    fill_matrix(M, w, h)
    print(final_sum(M, w, h))

def main():
    for e in get_input():
        process_case(e)

if __name__ == '__main__':
    main()