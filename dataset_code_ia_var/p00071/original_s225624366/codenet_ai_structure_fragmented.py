def get_initial_range():
    return range(14)

def get_inner_range():
    return range(3, 11)

def get_zero_prefix():
    return "000"

def create_empty_matrix(rows, cols):
    return ["0" * cols for _ in rows]

def get_ranges():
    return get_initial_range(), get_inner_range()

def prepare_matrix():
    A, B = get_ranges()
    return create_empty_matrix(A, 14)

def get_input_count():
    return input()

def get_test_range():
    return range(get_input_count())

def get_raw_input():
    return raw_input()

def get_prefixed_line():
    z = get_zero_prefix()
    return z + get_raw_input() + z

def read_matrix_lines(M):
    _, B = get_ranges()
    lines = []
    for _ in B:
        lines.append(get_prefixed_line())
    return lines

def set_matrix_lines(M, lines):
    _, B = get_ranges()
    for ind, j in enumerate(B):
        M[j] = lines[ind]
    return M

def get_xy():
    x = input() + 2
    y = input() + 2
    return x, y

def get_neighbour_range():
    return [-3,-2,-1,1,2,3]

def get_row(M, y):
    return M[y]

def set_row(M, y, s):
    M[y] = s

def update_row_zero(s, x):
    return s[:x] + "0" + s[x+1:]

def already_zero(s, x):
    return s[x] == "0"

def bomb(x, y):
    s = get_row(M, y)
    if already_zero(s, x):
        return
    set_row(M, y, update_row_zero(s, x))
    R = get_neighbour_range()
    for e in R:
        bomb(x+e, y)
        bomb(x, y+e)
    return

def print_data_case(data_index):
    print "Data %d:" % (data_index + 1)

def print_matrix(M):
    _, B = get_ranges()
    for j in B:
        print M[j][3:-3]

def main():
    global M
    A, B = get_ranges()
    M = prepare_matrix()
    z = get_zero_prefix()
    N = get_test_range()
    for i in N:
        s = get_raw_input()
        lines = []
        for _ in B:
            lines.append(get_prefixed_line())
        M = set_matrix_lines(M, lines)
        x, y = get_xy()
        bomb(x, y)
        print_data_case(i)
        print_matrix(M)

main()