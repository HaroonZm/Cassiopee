w, h, n = map(int, input().split())
a, b = map(int, input().split())
ans = 0
for i in range(n-1):
    x, y = map(int, input().split())
    ans += min(abs(y - x + a - b) + min(abs(y - b), abs(x - a)), abs(x - a) + abs(y - b))
    a, b = x, y
print(ans)