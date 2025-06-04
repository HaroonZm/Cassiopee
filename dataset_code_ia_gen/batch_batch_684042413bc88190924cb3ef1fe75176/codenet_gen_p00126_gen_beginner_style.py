n = int(input())
for data_i in range(n):
    grid = []
    for _ in range(9):
        line = input().split()
        grid.append(line)

    # compter les occurrences dans les lignes
    row_counts = []
    for i in range(9):
        d = {}
        for num in grid[i]:
            d[num] = d.get(num,0)+1
        row_counts.append(d)

    # compter les occurrences dans les colonnes
    col_counts = []
    for j in range(9):
        d = {}
        for i in range(9):
            num = grid[i][j]
            d[num] = d.get(num,0)+1
        col_counts.append(d)

    # compter les occurrences dans les blocs 3x3
    block_counts = []
    for bi in range(3):
        for bj in range(3):
            d = {}
            for i in range(3):
                for j in range(3):
                    num = grid[bi*3+i][bj*3+j]
                    d[num] = d.get(num,0)+1
            block_counts.append(d)

    # checker chaque nombre si il est en double dans ligne/col/block
    for i in range(9):
        line_out = ''
        for j in range(9):
            num = grid[i][j]
            block_id = (i//3)*3 + (j//3)
            wrong = False
            if row_counts[i][num] > 1:
                wrong = True
            if col_counts[j][num] > 1:
                wrong = True
            if block_counts[block_id][num] > 1:
                wrong = True
            if wrong:
                line_out += '*' + num
            else:
                line_out += ' ' + num
        print(line_out)
    if data_i != n-1:
        print()