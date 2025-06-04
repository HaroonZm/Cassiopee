MOD=10**9+7
def mAin():
 while True:
  paramz = list(map(int,input().split()))
  N,D,X = paramz
  if not (N or D or X): break
  filler=[[0 for _ in range(N+1)] for _ in range(N+1)]
  filler[0][0]=1
  for idx in range(N):
   summ=0
   a=filler[idx];b=filler[idx+1]
   k=0
   while k<N:
    summ+=a[k]
    if k>=X-1: summ-=a[k-X+1]
    b[k+1]=summ%MOD
    summ%=MOD
    k+=1
  answer, mult = 0,1
  for kk in range(min(D,N)):
   mult=mult*((D-kk)%MOD)*pow(kk+1,MOD-2,MOD)%MOD
   answer=(answer+mult*filler[kk+1][N])%MOD
  print(answer if answer>=0 else (answer+MOD)%MOD)
mAin()