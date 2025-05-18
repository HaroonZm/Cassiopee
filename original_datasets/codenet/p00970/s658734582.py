r, s, p = map(int, input().split())
ps = [None] * p
for k in range(p):
    i, j = map(int, input().split())
    if j <= s:
        j -= 1
    ps[k] = r + 1 - i + abs(s - j)
ans = 0
for t, p in enumerate(sorted(ps)[::-1]):
    ans = max(ans, t + p)
print(ans)