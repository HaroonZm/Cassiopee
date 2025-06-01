def main():
    import operator as o, functools as f
    MOD = 10**9+7
    s,t = (lambda x: tuple(x for x in x.strip()))(input()), (lambda x: tuple(x for x in x.strip()))(input())
    n,m = len(s),len(t)
    dp = list(f.reduce(lambda acc,_: acc+[ [0]*(m+1) ], range(n), [[0]*(m+1)]))
    dp[0][0]=1
    def foldr(func, acc, xs):
        return acc if not xs else func(xs[0], foldr(func, acc, xs[1:]))
    for i in range(n):
        dp[i+1] = [ (lambda idx,j=dp[i][idx],c=s[i]: (j, (j if idx==m or c!=t[idx] else (j + dp[i][idx+1])%MOD)%MOD) )(idx)[0] for idx in range(m+1)]
        # Above line generates — actually, let's do complicated way:
        step = []
        for j_rev in range(m-1,-1,-1):
            dp[i+1][j_rev] = (dp[i+1][j_rev] + dp[i][j_rev]) % MOD
            if s[i] == t[j_rev]:
                dp[i+1][j_rev+1] = (dp[i+1][j_rev+1] + dp[i][j_rev]) % MOD
    print(sum(dp[i][m] for i in range(n+1)) % MOD)

if __name__=="__main__":
    main()