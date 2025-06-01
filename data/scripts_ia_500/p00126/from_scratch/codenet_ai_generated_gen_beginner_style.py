n = int(input())
for dataset in range(n):
    board = []
    for _ in range(9):
        row = input().split()
        board.append(row)

    # check rows
    row_counts = []
    for i in range(9):
        counts = {}
        for j in range(9):
            num = board[i][j]
            counts[num] = counts.get(num, 0) + 1
        row_counts.append(counts)

    # check columns
    col_counts = []
    for j in range(9):
        counts = {}
        for i in range(9):
            num = board[i][j]
            counts[num] = counts.get(num, 0) + 1
        col_counts.append(counts)

    # check boxes
    box_counts = []
    for box_i in range(3):
        for box_j in range(3):
            counts = {}
            for i in range(box_i*3, box_i*3+3):
                for j in range(box_j*3, box_j*3+3):
                    num = board[i][j]
                    counts[num] = counts.get(num, 0) + 1
            box_counts.append(counts)

    for i in range(9):
        line = ""
        for j in range(9):
            num = board[i][j]
            # check if duplicated in row, col or box
            in_row = row_counts[i][num] > 1
            in_col = col_counts[j][num] > 1
            box_index = (i//3)*3 + (j//3)
            in_box = box_counts[box_index][num] > 1
            if in_row or in_col or in_box:
                line += "*" + num
            else:
                line += " " + num
        print(line)
    if dataset != n-1:
        print()