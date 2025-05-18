def In(n): return [map(int, raw_input().split()) for _ in [0]*n]
  
while 1:
  n = int(raw_input())
  if n==0: break
  M1 = In(n)
  m = int(raw_input())
  M2 = In(m)
  j=0
  f1 = [-1 for _ in [0]*n]
  f2 = [-1 for _ in [0]*m]
  for i in range(n):
    h1, r1 = M1[i]
    for j in range(m):
      h2, r2 = M2[j]
      if h1 < h2 and r1 < r2: f2[j] = i
      if h1 > h2 and r1 > r2: f1[i] = j
  c1 = [-1 for _ in [0]*(n+1)]
  c2 = [-1 for _ in [0]*(m+1)]
  p1 = p2 = 0
  while p1<n or p2<m:
    if p1<n:
      if f1[p1]<0:
        if p1==0: c1[0]=1
        else: c1[p1] = c1[p1-1] + 1
        p1+=1
      elif c2[f1[p1]]>=0:
        c1[p1] = max(c1[p1-1], c2[f1[p1]]) + 1
        p1+=1
    if p2<m:
      if f2[p2]<0:
        if p2==0: c2[0]=1
        else: c2[p2] = c2[p2-1]+1
        p2+=1
      elif c1[f2[p2]]>=0:
        c2[p2] = max(c2[p2-1], c1[f2[p2]]) + 1
        p2+=1
  print max(c1+c2)