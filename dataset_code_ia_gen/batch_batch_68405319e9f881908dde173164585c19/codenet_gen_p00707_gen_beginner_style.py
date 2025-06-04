def find_secret_number(matrix, W, H):
    max_number = -1

    # Function to perform DFS and find numbers starting from (r, c)
    def dfs(r, c, current_num):
        nonlocal max_number
        if not (0 <= r < H) or not (0 <= c < W):
            return
        if not matrix[r][c].isdigit():
            return
        new_num = current_num + matrix[r][c]
        # Update max_number
        new_num_val = int(new_num)
        if new_num_val > max_number:
            max_number = new_num_val
        # Next steps: right or down
        if c + 1 < W and matrix[r][c+1].isdigit():
            dfs(r, c+1, new_num)
        if r + 1 < H and matrix[r+1][c].isdigit():
            dfs(r+1, c, new_num)

    for i in range(H):
        for j in range(W):
            if matrix[i][j].isdigit() and matrix[i][j] != '0':
                dfs(i, j, "")

    return str(max_number)

while True:
    line = input()
    if line.strip() == '':
        continue
    W, H = map(int, line.split())
    if W == 0 and H == 0:
        break
    matrix = []
    for _ in range(H):
        row = input()
        while len(row) < W:
            row += input()
        matrix.append(row)
    print(find_secret_number(matrix, W, H))