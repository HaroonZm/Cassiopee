N=int(input())
S=input()
mod=10**9+7

#DP[i]#最後においた数の右にある残っている個数
rest=N-1
DP=[1]*(N)

for s in S:
    NDP=[0]*(N)
    if s=="<":
        for i in range(rest+1):
            if i>=1:
                NDP[i-1]=(DP[i]+NDP[i-1])%mod

        DP=NDP
        for i in range(N-2,-1,-1):
            DP[i]=(DP[i+1]+DP[i])%mod

    else:
        DP=[DP[rest-i] for i in range(N)]#左右逆にして考える

        #print(DP)
        for i in range(rest+1):
            if i>=1:
                NDP[i-1]=(DP[i]+NDP[i-1])%mod

        DP=NDP
        for i in range(N-2,-1,-1):
            DP[i]=(DP[i+1]+DP[i])%mod

        DP=[DP[rest-1-i] for i in range(N)]

    rest-=1
    #print(DP,rest)

print(DP[0])