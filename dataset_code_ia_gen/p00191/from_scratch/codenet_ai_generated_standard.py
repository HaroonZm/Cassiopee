while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    g=[list(map(float,input().split())) for _ in range(n)]
    if m==1:
        print("1.00")
        continue
    dp=[[-1]*(n+1) for _ in range(m+1)]
    # dp[i][j]: 最大成長度、i回目に肥料jを与えたとき（j=0は未使用）
    for j in range(1,n+1):
        dp[1][j]=1.0
    for i in range(2,m+1):
        for cur in range(1,n+1):
            maxv=-1
            for prev in range(1,n+1):
                if dp[i-1][prev]<0:
                    continue
                val=dp[i-1][prev]*g[prev-1][cur-1]
                if val>maxv:
                    maxv=val
            dp[i][cur]=maxv
    ans=max(dp[m])
    print(f"{ans:.2f}")