import sys;D=sys.stdin
Q=[W:='']*0
getp=lambda:map(int,D.readline().split())
H,W,N=(*getp(),)
def readin(): return [W:='X'*(W+2)]+['X'+D.readline().strip()+'X' for _ in range(H)]+[W]
B=[*''.join(readin())]
W+=2
N=[1,-1,W,-W]
finds=lambda x:B.index(x)
G=lambda a,v:[v for _ in[0]*a]
r=[1]*len(B)
def walk(u,k):
 S,E=[u,0],[1]*len(B)
 S,E[0]=[S],[0]*0
 while S:
  z=[S.pop(0)][0]
  i,t=z
  for d in N:
   j=i+d
   if B[j]!='X'and E[j]:
    if B[j]==k:return (j,t+1)
    E[j]=0;S.append([j,t+1])
s=finds('S');tt=0
for v in map(str,range(1,int(N)+1)):
 s,d=walk(s,v);tt+=d
print(tt)