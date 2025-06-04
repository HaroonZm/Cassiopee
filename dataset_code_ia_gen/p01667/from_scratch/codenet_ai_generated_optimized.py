M,N=map(int,input().split())
low=[0]*N
upp=[10**9]*N
for _ in range(M):
 K=int(input())
 for __ in range(K):
  s,cond,t=input().split()
  s,t=int(s),int(t)
  if cond=='>=':
   low[s-1]=max(low[s-1],t)
  else:
   upp[s-1]=min(upp[s-1],t)
print("Yes" if all(low[i]<=upp[i] for i in range(N)) else "No")