X, Y = map(int, input().split())
ans = 0
for z in [X,Y]:
  if z == 3:
    ans += 10**5
  elif z == 2:
    ans += 2*10**5
  elif z == 1:
    ans += 3*10**5
if X == Y == 1:
  ans += 4*10**5
print(ans)