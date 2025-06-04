while True:
    n = int(input())
    if n == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(n)]
    row_mins = [min(row) for row in matrix]
    col_maxs = [max(matrix[i][j] for i in range(n)) for j in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == row_mins[i] and matrix[i][j] == col_maxs[j]:
                result = matrix[i][j]
                break
        if result != 0:
            break
    print(result)