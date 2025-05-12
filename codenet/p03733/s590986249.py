N, T = map(int, input().split())
t = list(map(int, input().split()))

o = T
for i, j in zip(t, t[1:]):
  o += min(j-i, T)
print(o)