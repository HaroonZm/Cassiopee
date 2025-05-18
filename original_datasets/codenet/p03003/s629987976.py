import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N,M=map(int,input().split())
    S=tuple(map(int,input().split()))
    T=tuple(map(int,input().split()))
    dp=[[0]*(M+1) for _ in range(N+1)]
    SUM=[[0]*(M+2) for _ in range(N+2)]
    ans=1
    for s in range(N):
        for t in range(M):
            if S[s]==T[t]:
                dp[s+1][t+1]=SUM[s+1][t+1]+1
                ans+=dp[s+1][t+1]
                ans%=MOD
            else:
                dp[s+1][t+1]=0
            SUM[s+2][t+2]=SUM[s+1][t+2]+SUM[s+2][t+1]-SUM[s+1][t+1]+dp[s+1][t+1]
            SUM[s+2][t+2]%=MOD
    print(ans)
    

if __name__ == '__main__':
    main()