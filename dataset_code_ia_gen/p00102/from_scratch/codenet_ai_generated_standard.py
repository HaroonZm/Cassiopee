while True:
    n = int(input())
    if n == 0:
        break
    table = [list(map(int, input().split())) for _ in range(n)]
    row_sums = [sum(row) for row in table]
    col_sums = [sum(table[i][j] for i in range(n)) for j in range(n)]
    total_sum = sum(row_sums)
    for i in range(n):
        print(''.join(f"{table[i][j]:5d}" for j in range(n)), f"{row_sums[i]:5d}")
    print(''.join(f"{col_sums[j]:5d}" for j in range(n)), f"{total_sum:5d}")