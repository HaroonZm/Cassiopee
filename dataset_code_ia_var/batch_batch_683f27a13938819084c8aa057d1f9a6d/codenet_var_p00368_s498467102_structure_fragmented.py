def read_dimensions():
    return [int(i) for i in input().split()]

def read_matrix(H):
    return [read_matrix_row() for _ in range(H)]

def read_matrix_row():
    return [i for i in input().split()]

def compute_not_up(up):
    return [invert_bit(i) for i in up]

def invert_bit(i):
    return str(int(not int(i)))

def count_zero_difference(up, W):
    return abs(up.count("0") * 2 - W)

def is_up_balance_ok(up, W):
    return count_zero_difference(up, W) < 2

def is_same_row(row1, row2):
    return row1 == row2

def are_rows_opposite(row, not_up):
    return is_same_row(row, not_up)

def has_valid_rows(matrix, up, not_up):
    same = 1
    for line in get_lines_starting_from_second(matrix):
        if is_first_elements_equal(up, line):
            same = increment(same)
            if not is_same_row(up, line):
                return False, same
        elif is_first_elements_equal(not_up, line):
            if not are_rows_opposite(line, not_up):
                return False, same
        else:
            return False, same
    return True, same

def get_lines_starting_from_second(matrix):
    return matrix[1:]

def is_first_elements_equal(a, b):
    return a[0] == b[0]

def increment(x):
    return x + 1

def is_height_balance_ok(same, H):
    return abs(same * 2 - H) < 2

def print_result(is_ok):
    if is_ok:
        print("yes")
    else:
        print("no")

def main():
    is_ok = True
    W, H = read_dimensions()
    matrix = read_matrix(H)
    up = matrix[0]
    not_up = compute_not_up(up)

    if not is_up_balance_ok(up, W):
        is_ok = False

    rows_valid, same = has_valid_rows(matrix, up, not_up)
    if not rows_valid:
        is_ok = False

    if not is_height_balance_ok(same, H):
        is_ok = False

    print_result(is_ok)

main()