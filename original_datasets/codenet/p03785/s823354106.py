# A - Airport Bus
# https://atcoder.jp/contests/agc011/tasks/agc011_a

n, c, k = map(int, input().split())
T = [int(input()) for _ in range(n)]

T.sort()

ans = 1
cnt = 0
st = T[0]
for t in T:
  cnt += 1
  if t - st > k or cnt > c:
    ans += 1
    st = t
    cnt = 1

print(ans)