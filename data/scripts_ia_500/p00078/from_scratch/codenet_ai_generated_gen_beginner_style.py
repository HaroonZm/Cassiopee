while True:
    n = int(input())
    if n == 0:
        break
    magic = [[0]*n for _ in range(n)]
    # start position: middle column, row just below middle
    row = n//2 + 1
    col = n//2
    for num in range(1, n*n+1):
        # adjust row and col if they go out of bounds
        if row == n:
            row = 0
        if col == n:
            col = 0
        if row < 0:
            row = n - 1
        if col < 0:
            col = n - 1
        if magic[row][col] != 0:
            # if cell occupied, move left down from previous position
            row = prev_row + 1
            col = prev_col - 1
            if row == n:
                row = 0
            if col < 0:
                col = n - 1
        magic[row][col] = num
        prev_row = row
        prev_col = col
        # next position is one row down and one column right
        row += 1
        col += 1
    for r in range(n):
        line = []
        for c in range(n):
            line.append(str(magic[r][c]).rjust(4))
        print(''.join(line).lstrip())