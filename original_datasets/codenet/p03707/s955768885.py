N,M,Q=map(int,input().split())
G=[input() for i in range(N)]
node=[[0]*(M+1)]
edge_x=[[0]*M]
edge_y=[[0]*(M+1)]
for i in range(1,N+1):
  n,e_x,e_y=[0],[0],[0]
  for j in range(1,M+1):
    if G[i-1][j-1]=="1":
      n.append(n[-1]+node[i-1][j]-node[i-1][j-1]+1)
    else:
      n.append(n[-1]+node[i-1][j]-node[i-1][j-1])
    if j<M:
      if G[i-1][j-1]=="1" and G[i-1][j]=="1":
        e_x.append(e_x[-1]+edge_x[i-1][j]-edge_x[i-1][j-1]+1)
      else:
        e_x.append(e_x[-1]+edge_x[i-1][j]-edge_x[i-1][j-1])
    if i<N:
      if G[i-1][j-1]=="1" and G[i][j-1]=="1":
        e_y.append(e_y[-1]+edge_y[i-1][j]-edge_y[i-1][j-1]+1)
      else:
        e_y.append(e_y[-1]+edge_y[i-1][j]-edge_y[i-1][j-1])
  
  node.append(n)
  edge_x.append(e_x)
  if i<N:
    edge_y.append(e_y)

for q in range(Q):
  x1,y1,x2,y2=map(int,input().split())
  n=node[x2][y2]-node[x1-1][y2]-node[x2][y1-1]+node[x1-1][y1-1]
  e_y=edge_y[x2-1][y2]-edge_y[x1-1][y2]-edge_y[x2-1][y1-1]+edge_y[x1-1][y1-1]
  e_x=edge_x[x2][y2-1]-edge_x[x1-1][y2-1]-edge_x[x2][y1-1]+edge_x[x1-1][y1-1]
  e=e_x+e_y
  print(n-e)