a, b, c, x, y = map(int, input().split())
ans = 10**18
for i in range(0, 2 * max(x, y) + 2, 2):
    X, Y = x, y
    X -= i // 2
    Y -= i // 2
    X = max(0, X)
    Y = max(0, Y)
    ans = min(ans, a * X + b * Y + c * i)
print(ans)