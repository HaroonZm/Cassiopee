import sys
sys.setrecursionlimit(10**7)
V,E=map(int,input().split())
a=list(input().split())
adj=[[] for _ in range(V)]
for _ in range(E):
 s,t=map(int,input().split())
 adj[s].append(t)
 adj[t].append(s)

res=a[:]
from collections import deque
q=deque(i for i,x in enumerate(a) if x!='?')
visited=[False]*V
for i in q:
 visited[i]=True
while True:
 changed=False
 for i in range(V):
  if res[i]!='?':
   used=set(res[j] for j in adj[i] if res[j]!='?')
   if res[i] in used:
    # conflict, problem states input always possible? So ignore
    pass
 for i in range(V):
  if res[i]=='?':
   used=set(res[j] for j in adj[i] if res[j]!='?')
   for c in 'abcdefghijklmnopqrstuvwxyz':
    if c not in used:
     res[i]=c
     changed=True
     break
 if not changed:
  break
print(''.join(res))