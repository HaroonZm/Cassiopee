import sys
sys.setrecursionlimit(10**8)
N=int(input())
G=[[] for i in range(N)]
E=[]
ans=[0]*(N-1)
for i in range(N-1):
  a,b=map(int,input().split())
  G[a-1].append((b-1,i))
  G[b-1].append((a-1,i))
s=[int(i) for i in input().split()]
n=[0]*N
visited=[False]*N
def size(x):
  res=1
  visited[x]=True
  for i,e in G[x]:
    if visited[i]:
      continue
    res+=size(i)
    E.append((e,x,i))
  n[x]=res
  return res
size(0)
#print(n)
flag=0
E.sort()
for i in range(N-1):
  e,a,b=E[i]
  if 2*n[b]==N:
    flag=e+1
    continue
  ans[e]=abs((s[a]-s[b])//(2*n[b]-N))
#print(ans,flag)
#print(E)
if flag:
  A=s[0]
  for i in range(N-1):
    A-=n[E[i][2]]*ans[i]
  ans[flag-1]=A//n[E[flag-1][2]]
for i in range(N-1):
  print(ans[i])