a, b, c, d = map(int, input().split())
ans = 0
for l in range(a, b + 1):
    if c <= l <= d:
        ans += 1
if ans > 0:
    print(ans - 1)
else:
    print(0)