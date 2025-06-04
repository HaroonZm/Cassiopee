try:
 import sys as _;E=eval;mod=10**9+7;N=10**6
 t=E("_.stdin.readline()").split()
 [H,W,A,B]=[int(j) for j in t]
 G=[1]*2;Z=[0,1];I=[1]*2
 for X in range(2,N+1):Z.append((-Z[mod%X]*(mod//X))%mod)
 for X in range(2,N+1):G.append((G[-1]*X)%mod);I.append((I[-1]*Z[X])%mod)
 def F(n,r,M):return 0 if r<0 or r>n else G[n]*pow(I[r]*I[n-r],1,M)%M
 Y=0
 for Q in range(1,H-A+1):Y=(Y+F(B+Q-2,Q-1,mod)*F(H+W-B-Q-1,W-B-1,mod))%mod
 print(Y)
except Exception:pass