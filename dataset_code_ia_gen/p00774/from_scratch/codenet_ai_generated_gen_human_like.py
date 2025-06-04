while True:
    H = input()
    if H == '0':
        break
    H = int(H)
    board = [list(map(int, input().split())) for _ in range(H)]
    score = 0

    while True:
        to_remove = [[False]*5 for _ in range(H)]
        # Detect horizontal groups of 3+ identical digits
        for r in range(H):
            c = 0
            while c < 3:
                val = board[r][c]
                if val != 0 and val == board[r][c+1] == board[r][c+2]:
                    length = 3
                    for k in range(c+3,5):
                        if board[r][k] == val:
                            length += 1
                        else:
                            break
                    for i in range(c, c+length):
                        to_remove[r][i] = True
                    c += length
                else:
                    c += 1

        # If no stones to remove, end loop
        if not any(any(row) for row in to_remove):
            break

        # Remove stones and add to score
        for r in range(H):
            for c in range(5):
                if to_remove[r][c]:
                    score += board[r][c]
                    board[r][c] = 0

        # Drop stones down column by column
        for c in range(5):
            new_col = []
            for r in range(H-1, -1, -1):
                if board[r][c] != 0:
                    new_col.append(board[r][c])
            # Fill the column from bottom up
            for r in range(H-1, -1, -1):
                if new_col:
                    board[r][c] = new_col.pop(0)
                else:
                    board[r][c] = 0

    print(score)