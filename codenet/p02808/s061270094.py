import sys
input = sys.stdin.readline

N,K=map(int,input().split())
A=list(map(int,input().split()))
mod=10**9+7

Combi=[[] for i in range(N+1)]
Combi[0]=[1,0]

for i in range(1,N+1):
    Combi[i].append(1)
    for j in range(i):
        Combi[i].append((Combi[i-1][j]+Combi[i-1][j+1])%mod)
    Combi[i].append(0)

DP=[0]*(N+1)
DP[0]=1

for k in range(K):
    use=A[k]

    NDP=[0]*(N+1)

    for i in range(N+1):
        ANS=0
        for j in range(i+1):
            if use-(i-j)>=0:
                ANS=(ANS+DP[j]*Combi[N-j][i-j]*Combi[N-(i-j)][use-(i-j)])%mod

        NDP[i]=ANS

    #print(DP)

    DP=NDP

print(DP[N])