n, m = map(int, input().split())
hs = list(map(int, input().split()))

ans = [1] * n

for _ in range(m):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  if hs[a] < hs[b]:
    ans[a] = 0
  elif hs[a] == hs[b]:
    ans[a] = 0
    ans[b] = 0
  else:
    ans[b] = 0

print(sum(ans))