import sys,math

def f(n,m):
  res=[]
  c=1
  while c*c<=m:
    if m%c==0:
      if m//c>=n:
        res+=[c]
      if c>=n and m//c > c:
        res.append(m//c)
    c+=1
  return sorted(res)

N,M=[int(_) for _ in sys.stdin.readline().split()]
B=f(N,M)
output=None
for y in range(len(B)-1,len(B)):
    output=B[y]
print(output)