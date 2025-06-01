n, m, d = map(int, input().split())
floor = [input() for _ in range(n)]

cnt = sum(
    (all(floor[i][j + k] == '.' for k in range(d)) +
     all(floor[i + k][j] == '.' for k in range(d)))
    for i in range(n)
    for j in range(m)
    if floor[i][j] == '.' and j + d <= m and i + d <= n
)

print(cnt)