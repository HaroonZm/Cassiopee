import sys
from sys import stdin
input = stdin.readline

def check_row(board, row, color):
    return board[row].count(color) == 3

def check_all_rows(board, color):
    for y in range(3):
        if check_row(board, y, color):
            return True
    return False

def check_column(board, col, color):
    return board[0][col] == color and board[1][col] == color and board[2][col] == color

def check_all_columns(board, color):
    for x in range(3):
        if check_column(board, x, color):
            return True
    return False

def check_diag1(board, color):
    return board[0][0] == color and board[1][1] == color and board[2][2] == color

def check_diag2(board, color):
    return board[0][2] == color and board[1][1] == color and board[2][0] == color

def check_diagonals(board, color):
    return check_diag1(board, color) or check_diag2(board, color)

def has_won(board, color):
    if check_all_rows(board, color):
        return True
    if check_all_columns(board, color):
        return True
    if check_diagonals(board, color):
        return True
    return False

def get_winner(board):
    colors = ['b', 'w']
    for color in colors:
        if has_won(board, color):
            return color
    return 'NA'

def read_board_line():
    return list(input().strip())

def read_board():
    board = []
    board.append(read_board_line())
    board.append(read_board_line())
    board.append(read_board_line())
    return board

def should_stop(line):
    return line[0] == '0'

def process_game():
    first_line = input().strip()
    if should_stop(first_line):
        return None
    board = [list(first_line)]
    board.extend(read_board()[1:])
    return board

def print_result(result):
    print(result)

def main(args):
    while True:
        line = input().strip()
        if should_stop(line):
            break
        board = [list(line)]
        board.append(read_board_line())
        board.append(read_board_line())
        result = get_winner(board)
        print_result(result)

if __name__ == '__main__':
    main(sys.argv[1:])