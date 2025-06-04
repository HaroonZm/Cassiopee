def get_N():
    return int(input())

def is_end(N):
    return N == 0

def make_matrix(N):
    return [ [0 for _ in range(N)] for _ in range(N) ]

def initial_i():
    return 0

def initial_j():
    return 0

def initial_val():
    return 1

def initial_prev_move():
    return "UR"

def inside_last_cell(i, j, N):
    return i == N - 1 and j == N - 1

def at_top_row(i):
    return i == 0

def at_bottom_row(i, N):
    return i == N - 1

def at_left_col(j):
    return j == 0

def at_right_col(j, N):
    return j == N - 1

def on_diagonal(cell_a, cell_b):
    return cell_a == cell_b

def do_UR_main(i, j):
    return i - 1, j + 1, "UR"

def do_DL_main(i, j):
    return i + 1, j - 1, "DL"

def do_R(j):
    return j + 1

def do_D(i):
    return i + 1

def do_D_moves(i, prevMove):
    return i + 1, prevMove

def do_R_moves(j, prevMove):
    return j + 1, prevMove

def handle_top_row(prevMove, j, N, i):
    if prevMove == "UR":
        if j != N - 1:
            return i, j + 1, "R"
        else:
            return i + 1, j, "D"
    else:
        return i + 1, j - 1, "DL"

def handle_bottom_row(prevMove, i, j):
    if prevMove == "DL":
        return i, j + 1, "R"
    else:
        return i - 1, j + 1, "UR"

def handle_left_col(prevMove, i, j):
    if prevMove == "DL":
        return i + 1, j, "D"
    else:
        return i - 1, j + 1, "UR"

def handle_right_col(prevMove, i, j):
    if prevMove == "UR":
        return i + 1, j, "D"
    else:
        return i + 1, j - 1, "DL"

def handle_inner(prevMove, i, j):
    if prevMove == "DL":
        return i + 1, j - 1, "DL"
    else:
        return i - 1, j + 1, "UR"

def move_next(i, j, N, prevMove):
    if inside_last_cell(i, j, N):
        return i, j, prevMove, True
    elif at_top_row(i):
        ni, nj, nprevMove = handle_top_row(prevMove, j, N, i)
        return ni, nj, nprevMove, False
    elif at_bottom_row(i, N):
        ni, nj, nprevMove = handle_bottom_row(prevMove, i, j)
        return ni, nj, nprevMove, False
    elif at_left_col(j):
        ni, nj, nprevMove = handle_left_col(prevMove, i, j)
        return ni, nj, nprevMove, False
    elif at_right_col(j, N):
        ni, nj, nprevMove = handle_right_col(prevMove, i, j)
        return ni, nj, nprevMove, False
    else:
        ni, nj, nprevMove = handle_inner(prevMove, i, j)
        return ni, nj, nprevMove, False

def fill_matrix(arr, N):
    i = initial_i()
    j = initial_j()
    val = initial_val()
    prevMove = initial_prev_move()
    while True:
        arr[i][j] = val
        val += 1
        i, j, prevMove, done = move_next(i, j, N, prevMove)
        if done:
            break
    return arr

def format_case_header(TC):
    return "Case {}:".format(TC)

def print_matrix(arr, N):
    for i in range(N):
        for j in range(N):
            print("{:3d}".format(arr[i][j]), end='')
        print()

def process_case(N, TC):
    arr = make_matrix(N)
    arr = fill_matrix(arr, N)
    print(format_case_header(TC))
    print_matrix(arr, N)

def main():
    TC = 1
    while True:
        N = get_N()
        if is_end(N):
            break
        process_case(N, TC)
        TC += 1

if __name__ == '__main__':
    main()