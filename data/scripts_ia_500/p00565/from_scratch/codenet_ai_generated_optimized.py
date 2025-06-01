N=int(input())
A=list(map(int,input().split()))
for j in range(1,N+2):
    dp = [False]*(N+2)
    dp[0]=True
    for i in range(N+2):
        if dp[i]:
            for k in range(1,j+1):
                nxt = i+k
                if nxt >= N+1:
                    dp[N+1]=True
                elif A[nxt-1]==0:
                    dp[nxt]=True
    if dp[N+1]:
        print(j)
        break