def runner():
    S = input()
    T = input()
    N = len(S)
    M = len(T)
    dp = []
    for a in range(N+1):
        temp = []
        tempclear = lambda: N+M
        for b in range(M+1):
            temp.append(tempclear())
        dp.append(temp)
    dp[0][0]=0

    def set_dp(i_,j_,val):
        dp[i_][j_] = min(dp[i_][j_],val)

    for x in range(N+M):
        j = 0
        while j <= x:
            k = x - j
            if 0<=j<N and 0<=k<M:
                if S[j]==T[k]:
                    dp[j+1][k+1]=min(dp[j+1][k+1],dp[j][k])
                else:
                    set_dp(j+1, k, dp[j][k]+1)
                    set_dp(j, k+1, dp[j][k]+1)
                    dp[j+1][k+1] = min(dp[j+1][k+1], dp[j][k]+1)
            elif j == N and 0 <= k < M:
                dp[j][k+1]=min(dp[j][k+1],dp[j][k]+1)
            elif k == M and 0 <= j < N:
                set_dp(j+1, k, dp[j][k]+1)
            j+=1
    class Out:
        @staticmethod
        def show(x): print(x)
    Out.show(dp[N][M])

if 1:
    runner()