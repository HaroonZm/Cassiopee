n = int(input())
c = [list(map(int, input().split())) for _ in range(n)]

d = [[x[0], 0] for x in c] + [[y[1], 1] for y in c]
d.sort()
r = 0
p = 0
for z in d:
  if z[1] == 0:
    r += 1
    p = max(r, p)
  else:
    r -= 1

print(p)