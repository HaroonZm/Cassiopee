def check_winner(board):
    lines = board + [list(col) for col in zip(*board)]  # rows and columns
    lines.append([board[i][i] for i in range(3)])      # main diagonal
    lines.append([board[i][2 - i] for i in range(3)])  # anti-diagonal
    for line in lines:
        if line == ['b'] * 3:
            return 'b'
        if line == ['w'] * 3:
            return 'w'
    return 'NA'

while True:
    board = [list(input().strip()) for _ in range(3)]
    if board[0] == ['0']:
        break
    print(check_winner(board))