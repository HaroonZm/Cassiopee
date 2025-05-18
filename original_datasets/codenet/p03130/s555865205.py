g=[0,0,0,0]
one=0
two=0

for i in range(3):
  a,b=map(int,input().split())
  g[a-1]+=1
  g[b-1]+=1
  
for i in range(len(g)):
  if g[i]==1:
    one+=1
  if g[i]==2:
    two+=1
if one==2 and two==2:
  print('YES')
else:
  print('NO')