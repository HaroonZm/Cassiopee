def check_winner(board):
    lines = []
    # Rows and columns
    for i in range(3):
        lines.append(board[i])  # row
        lines.append(board[0][i]+board[1][i]+board[2][i])  # column
    # Diagonals
    lines.append(board[0][0]+board[1][1]+board[2][2])
    lines.append(board[0][2]+board[1][1]+board[2][0])
    for line in lines:
        if line == 'bbb':
            return 'b'
        elif line == 'www':
            return 'w'
    return 'NA'

while True:
    board = [input() for _ in range(3)]
    if board[0] == '0':
        break
    print(check_winner(board))