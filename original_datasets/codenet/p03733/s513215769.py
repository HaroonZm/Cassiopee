N, T = map(int, input().split())
t = list(map(int, input().split()))
s = T
f = t[0] + T
for i in range(N-1):
  s += T
  if f > t[i+1]:
    s -= f - t[i+1]
  f = t[i+1] + T
print(s)