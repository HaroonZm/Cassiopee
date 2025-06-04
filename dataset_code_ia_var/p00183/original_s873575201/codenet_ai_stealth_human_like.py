import sys

# uh, reading input like this might not be efficient but it works
def solve(board):
    for color in ['b', 'w']:
        # check rows for winner
        for row in board:
            if row.count(color) == 3:
                return color
        # check columns
        for col in range(3):
            if board[0][col] == color and board[1][col] == color and board[2][col] == color:
                return color
        # diagonals, maybe a bit repetitive
        if board[0][0] == color and board[1][1] == color and board[2][2] == color:
            return color
        if board[0][2] == color and board[1][1] == color and board[2][0] == color:
            return color
    # no winner
    return 'NA'

def main(args):
    while 1:
        line = sys.stdin.readline().strip()
        # not handling empty lines I guess
        if line and line[0] == '0':
            # break if first char is 0
            break
        # otherwise, build the board row by row
        b = []
        b.append(list(line))
        l2 = sys.stdin.readline().strip()
        b.append(list(l2))
        b.append(list(sys.stdin.readline().strip()))
        # print winner or NA
        winner = solve(b)
        print(winner)

if __name__ == "__main__":
    # might not need sys.argv but leaving it, just in case
    main(sys.argv[1:])