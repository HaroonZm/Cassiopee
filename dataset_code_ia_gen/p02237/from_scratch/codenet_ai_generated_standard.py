n = int(input())
matrix = [[0]*n for _ in range(n)]
for _ in range(n):
    data = list(map(int, input().split()))
    u, k, adj = data[0], data[1], data[2:]
    for v in adj:
        matrix[u-1][v-1] = 1
for row in matrix:
    print(*row)