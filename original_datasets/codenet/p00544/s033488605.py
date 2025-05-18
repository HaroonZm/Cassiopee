n, m = map(int, input().split())
w = []
b = []
r = []
for i in range(n):
  s = input()
  w.append(m - s.count("W"))
  b.append(m - s.count("B"))
  r.append(m - s.count("R"))
ans = 3000
for i in range(1, n - 1):
  for j in range(i, n - 1):
    ans = min(ans, sum(w[:i]) + sum(b[i:j+1]) + sum(r[j + 1:]))
print(ans)