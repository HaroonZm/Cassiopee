import copy

def read_input_row():
    return list(raw_input())

def read_input():
    return [read_input_row() for _ in range(8)]

def create_empty_row():
    return ['' for _ in range(8)]

def create_empty_board():
    return [create_empty_row() for _ in range(8)]

def rotate_board_once(V, _V):
    for r in range(8):
        for c in range(8):
            _V[c][7 - r] = V[r][c]

def deepcopy_board(board):
    return copy.deepcopy(board)

def print_angle(angle):
    print angle

def print_board(V):
    for line in V:
        print ''.join(line)

def rotate_and_print(V, angles=[90, 180, 270]):
    _V = create_empty_board()
    for angle in angles:
        rotate_board_once(V, _V)
        V = deepcopy_board(_V)
        print_angle(angle)
        print_board(V)

def main():
    V = read_input()
    rotate_and_print(V)

main()