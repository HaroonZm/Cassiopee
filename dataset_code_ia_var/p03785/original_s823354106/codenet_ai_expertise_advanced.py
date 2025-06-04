from itertools import islice

n, c, k = map(int, input().split())
T = sorted(int(input()) for _ in range(n))

ans = 1
cnt = 0
st = T[0]
for t in islice(T, 0, None):
    cnt += 1
    if t - st > k or cnt > c:
        ans += 1
        st = t
        cnt = 1

print(ans)