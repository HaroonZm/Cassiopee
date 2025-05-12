import numpy as np
from numba import njit
N=int(input())
a=np.array([int(i) for i in input().split()],dtype=np.int64)

s=[0]

dp=np.array([[-1 for i in range(N)] for _ in range(N)],dtype=np.int64)

for i in range(1,N+1):
    s.append(s[i-1]+a[i-1])

s=np.array(s,dtype=np.int64)
for i in range(N):
    dp[i][i]=0

@njit('i8(i8,i8,i8[:,:],i8[:])', cache=True)
def calc(i,j,dp,s):
    if dp[i][j]!=-1:
        return dp[i][j]
    m=10**14
    for k in range(i,j):
        m=min(m,calc(i,k,dp,s)+calc(k+1,j,dp,s)+s[j+1]-s[i])
    dp[i][j]=m
    return dp[i][j]

print(calc(0,N-1,dp,s))