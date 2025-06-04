def f():
 N,W=map(int,input().split())
 l=[int(input())for _ in range(N)]
 l.sort()
 total=0; r=0
 def aux(i, s):
  if i==len(l): return [1]+[0]*W
  rest = aux(i+1,s+l[i])
  tmp=[x for x in rest]
  for k in range(W+1):
   if k-l[i]>=0: tmp[k]+=rest[k-l[i]]
  return tmp
 x=0
 i=0
 while i<N:
  if i==N-1:
   S=sum(l)
   if S-l[-1]<=W and W-S+l[-1]<l[-1]: r+=1
   break
  DP=[[0]*(W+1)for _ in[0]*(N-i)]
  DP[0][0]=1
  for m in range(N-i-1):
   for nnn,k in enumerate(range(W+1)):
    if k-l[i+1+m]>=0: DP[m+1][k]=DP[m][k]+DP[m][k-l[i+1+m]]
    else: DP[m+1][k]=DP[m][k]
  a=max(W-total-l[i]+1,0)
  while a<=W-total:
   r+=DP[-1][a]; r%=10**9+7; a+=1
  total+=l[i]
  if total>W: break
  i+=1
 print(r%1000000007)
f()