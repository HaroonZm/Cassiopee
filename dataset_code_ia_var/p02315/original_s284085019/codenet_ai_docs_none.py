n, w = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]
memo = [[0] + [-1] * w for _ in range(n+1)]
for i in range(n):
    for j in range(w+1):
        if memo[i][j] > -1 and j+items[i][1] <= w:
            memo[i+1][j+items[i][1]] = max(memo[i+1][j+items[i][1]], memo[i][j]+items[i][0])
        memo[i+1][j] = max(memo[i+1][j], memo[i][j])
print(max(memo[-1]))