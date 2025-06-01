def read_input():
    return int(input())

def create_empty_matrix(size):
    return [[0 for _ in range(size)] for _ in range(size)]

def initialize_indices_and_values():
    return 0, 0, 1, "UR"

def place_value(arr, i, j, val):
    arr[i][j] = val

def increment_value(val):
    return val + 1

def reached_end(i, j, N):
    return i == N - 1 and j == N - 1

def at_top(i):
    return i == 0

def at_bottom(i, N):
    return i == N - 1

def at_left(j):
    return j == 0

def at_right(j, N):
    return j == N - 1

def update_position_and_move(i, j, prevMove, N):
    if at_top(i):
        if prevMove == "UR":
            if j != N - 1:
                j = move_right(j)
                prevMove = "R"
            else:
                i = move_down(i)
                prevMove = "D"
        else:
            i, j = move_down_left(i, j)
            prevMove = "DL"
    elif at_bottom(i, N):
        if prevMove == "DL":
            j = move_right(j)
            prevMove = "R"
        else:
            i, j = move_up_right(i, j)
            prevMove = "UR"
    elif at_left(j):
        if prevMove == "DL":
            i = move_down(i)
            prevMove = "D"
        else:
            i, j = move_up_right(i, j)
            prevMove = "UR"
    elif at_right(j, N):
        if prevMove == "UR":
            i = move_down(i)
            prevMove = "D"
        else:
            i, j = move_down_left(i, j)
            prevMove = "DL"
    else:
        if prevMove == "DL":
            i, j = move_down_left(i, j)
        else:
            i, j = move_up_right(i, j)
    return i, j, prevMove

def move_right(j):
    return j + 1

def move_down(i):
    return i + 1

def move_down_left(i, j):
    return i + 1, j - 1

def move_up_right(i, j):
    return i - 1, j + 1

def print_case_number(tc):
    print("Case {}:".format(tc))

def print_matrix(arr, N):
    for i in range(N):
        print_row(arr, i, N)

def print_row(arr, i, N):
    for j in range(N):
        print_cell(arr, i, j)
    print()

def print_cell(arr, i, j):
    print("{:3d}".format(arr[i][j]), end='')

def main_loop():
    TC = 1
    while True:
        N = read_input()
        if N == 0:
            break
        arr = create_empty_matrix(N)
        i, j, val, prevMove = initialize_indices_and_values()
        while True:
            place_value(arr, i, j, val)
            val = increment_value(val)
            if reached_end(i, j, N):
                break
            i, j, prevMove = update_position_and_move(i, j, prevMove, N)
        print_case_number(TC)
        TC += 1
        print_matrix(arr, N)

if __name__ == '__main__':
    main_loop()