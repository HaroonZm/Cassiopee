n = int(input())
adj_matrix = [[0]*n for _ in range(n)]

for _ in range(n):
    data = list(map(int, input().split()))
    u = data[0] - 1
    k = data[1]
    for v in data[2:2+k]:
        adj_matrix[u][v-1] = 1

for row in adj_matrix:
    print(' '.join(map(str, row)))