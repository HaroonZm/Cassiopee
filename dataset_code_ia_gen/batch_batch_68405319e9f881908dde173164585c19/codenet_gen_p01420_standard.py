import sys
input=sys.stdin.readline

N,M,L=map(int,input().split())
runners=[tuple(map(int,input().split())) for _ in range(N)]

times=[]
for p,t,v in runners:
 prob_rest=p/100
 dp=[0]*(M+1)
 dp[0]=1.0
 for _ in range(M):
  ndp=[0]*(len(dp)+1)
  for i in range(len(dp)):
   ndp[i]+=dp[i]*(1-prob_rest)
   ndp[i+1]+=dp[i]*prob_rest
  dp=ndp
 res=[]
 for k,pr in enumerate(dp):
  time=(L/v)+k*t
  res.append((time,pr))
 times.append(res)

res=[0.0]*N
for i in range(N):
 for ti,pi in times[i]:
  pwin=pi
  for j in range(N):
   if j==i:continue
   pj=0.0
   for tj,pj2 in times[j]:
    if abs(tj-ti)<1e-14:pj2=0
    elif tj<ti:pj2=1
    else: pj2=0
    pj+=pj2
   pwin*=pj
  res[i]+=pwin

for v in res:
 print(f"{v:.8f}")