import sys
from sys import stdin
input = stdin.readline

def determine_winner(game_board):
    player_symbols = ['b', 'w']
    for symbol in player_symbols:
        for row_index in range(3):
            if game_board[row_index].count(symbol) == 3:
                return symbol
        for col_index in range(3):
            if game_board[0][col_index] == symbol and game_board[1][col_index] == symbol and game_board[2][col_index] == symbol:
                return symbol
        if game_board[0][0] == symbol and game_board[1][1] == symbol and game_board[2][2] == symbol:
            return symbol
        if game_board[0][2] == symbol and game_board[1][1] == symbol and game_board[2][0] == symbol:
            return symbol
    return 'NA'

def main(arguments):
    while True:
        first_line = input().strip()
        if first_line[0] == '0':
            break
        current_board = []
        current_board.append(list(first_line))
        current_board.append(list(input().strip()))
        current_board.append(list(input().strip()))
        outcome = determine_winner(current_board)
        print(outcome)

if __name__ == '__main__':
    main(sys.argv[1:])