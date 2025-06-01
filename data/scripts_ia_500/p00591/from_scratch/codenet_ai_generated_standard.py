while True:
    n = int(input())
    if n == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(n)]
    row_min = [min(row) for row in matrix]
    col_max = [max(matrix[r][c] for r in range(n)) for c in range(n)]
    res = 0
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == row_min[r] and matrix[r][c] == col_max[c]:
                res = matrix[r][c]
                break
        if res != 0:
            break
    print(res)