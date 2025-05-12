while 1:
  try: n,m=map(int,input().split());
  except: break
  rs=[]
  while 1:
    line=input()
    if line=="0 0 0": break
    s,t,e=map(int,line.split())
    rs.append((s-1,t-1,e))
  l=int(input())
  b=[list(map(int,input().split())) for _ in range(l)]
  
  c=[[0]*n for _ in range(l)]
  for s,t,e in rs:
    for i in range(l):
      c[i][s]+=b[i][t]*e
  
  for i in range(l):
    print(" ".join(str(x) for x in c[i]))