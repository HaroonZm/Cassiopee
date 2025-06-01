def check_board():
    def get_input():
        return [list(map(int, list(input()))) for _ in range(8)]
    board = get_input()
    
    y_sums = []
    for row in board:
        y_sums.append(sum(row))
        
    x_sums = list(map(sum, zip(*board)))

    if 4 in x_sums:
        print('B')
        return
    elif 4 in y_sums:
        print('C')
        return
        
    if 1 in y_sums:
        row_idx = y_sums.index(1)
        col_idx = x_sums.index(2)
        print('D' if board[row_idx][col_idx] == 0 else 'F')
        return
    
    if 1 in x_sums:
        col_idx = x_sums.index(1)
        row_idx = y_sums.index(2)
        res = 'G' if board[row_idx][col_idx] == 0 else 'E'
        print(res)
        return
    
    print('A')

while True:
    try:
        check_board()
        input()
    except EOFError:
        break