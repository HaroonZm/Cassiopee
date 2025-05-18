while 1:
  n,m,q=map(int,input().split())
  if (n|m|q)==0: break
  
  p=[]
  res=[{_ for _ in range(n)} for _ in range(m)]
  for i in range(q):
    s,b=[[int(c) for c in s] for s in input().split()]
    if i>0:
      for j in range(n):
        s[j]^=p[j]
    zero={i for i in range(n) if s[i]==0}
    one={i for i in range(n) if s[i]==1}
    for j in range(m):
      if(b[j]==0): res[j]-=one
      if(b[j]==1): res[j]-=zero
    p=s
  
  table="".join([str(i) for i in range(10)]+[chr(ord("A")+i) for i in range(26)])
  for i in range(m):
    if len(res[i])==1:
      print(table[res[i].pop()],sep="",end="")
    else:
      print("?",sep="",end="")
  print()