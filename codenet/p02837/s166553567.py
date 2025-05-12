N = int(input())
dic = []
ls = [[] for i in range(N)]
for i in range(N):
  a = int(input())
  dic += [a]
  for j in range(a):
    x, y = map(int, input().split())
    ls[i] += [(x-1,y)]
ans = 0
for i in range(2**N):
  inf = []
  m = 0
  for j in range(N):
    if i%2==0:
      inf += [1]
      m += 1
    else:
      inf += [0]
    i >>= 1
  flag = False
  for j in range(N):
    if inf[j]==0:
      continue
    for h in range(dic[j]):
      x, y = ls[j][h]
      if inf[x]!=y:
        flag = True
        break
    if flag:
      break
  else:
    if ans<m:
      ans = m
print(ans)