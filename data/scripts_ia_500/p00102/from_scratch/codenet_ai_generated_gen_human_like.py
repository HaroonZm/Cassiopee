while True:
    n = int(input())
    if n == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(n)]
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(matrix[i][j] for i in range(n)) for j in range(n)]
    total_sum = sum(row_sums)

    for i in range(n):
        for j in range(n):
            print(f"{matrix[i][j]:5d}", end='')
        print(f"{row_sums[i]:5d}")
    for j in range(n):
        print(f"{col_sums[j]:5d}", end='')
    print(f"{total_sum:5d}")