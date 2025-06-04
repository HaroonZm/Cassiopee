def check_winner(board):
    lines = [
        [0,1,2], [3,4,5], [6,7,8],  # horizontal
        [0,3,6], [1,4,7], [2,5,8],  # vertical
        [0,4,8], [2,4,6]            # diagonal
    ]
    for line in lines:
        a, b, c = line
        if board[a] == board[b] == board[c]:
            if board[a] == 'o':
                return 'o'
            elif board[a] == 'x':
                return 'x'
    return 'd'

import sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    result = check_winner(line)
    print(result)