while True:
  n=int(input())
  if n==0: break
  g=[[] for _ in range(n)]
  for u in range(n):
    v1,w1,v2,w2=map(int,input().split())
    g[u].append((v1,w1))
    g[u].append((v2,w2))
  
  res=1
  vis=[False]*n
  for i in range(n):
    if vis[i]: continue
    ws=[]
    p,u=-1,i
    while True:
      vis[u]=True
      for v,w in g[u]:
        if v!=p:
          ws.append(w)
          p,u=u,v
          break
      if u==i: break
    res=res*ws.count(max(ws))%10007
  print(res)