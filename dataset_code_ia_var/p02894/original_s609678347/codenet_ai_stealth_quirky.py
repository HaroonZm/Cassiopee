import math as M
n,l=[*map(int,input().split())]
s = (n**3-n*3+2*n)//6
t=[]
for O in range(n): t+=[int(input())*M.pi/l]
def Q(f):
  X=0
  for a in range(n):
    for b in range(a+1,n):
      X+=f(t[a]+t[b])*(n+2*(a-b))
  return X/s
print(Q(M.cos),Q(M.sin))