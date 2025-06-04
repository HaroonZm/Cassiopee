N,Q=[int(_x)for _x in input().split()]
_𝓛=[[]for _𝕜 in range(N)]
for __ in range(Q):
 🦄=list(map(int,input().split()))
 if 🦄[0] is 0:(lambda L,i,v:L[i].append(v))(_𝓛,🦄[1],🦄[2])
 elif 🦄[0] is 1:
  try:print((_𝓛[🦄[1]]or[_ for _ in()])[0])
  except:pass
 else:
  try:_𝓛[🦄[1]].pop(0)
  except:pass