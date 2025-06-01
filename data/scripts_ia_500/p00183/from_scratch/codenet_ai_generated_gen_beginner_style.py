while True:
    board = []
    for _ in range(3):
        line = input()
        if line == '0':
            exit()
        board.append(line)
    
    winner = "NA"
    
    # 縦のチェック
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] in ['b','w']:
            winner = board[0][col]
    
    # 横のチェック
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] in ['b','w']:
            winner = board[row][0]
    
    # 斜めのチェック
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] in ['b','w']:
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] in ['b','w']:
        winner = board[0][2]
    
    print(winner)