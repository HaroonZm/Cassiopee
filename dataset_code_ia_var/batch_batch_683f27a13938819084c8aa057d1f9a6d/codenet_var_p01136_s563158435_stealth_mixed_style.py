import heapq

def solve():
    while 1:
        N = int(input())
        if N == 0: break
        st = [None]*N
        y = 0
        while y < N:
            tmp = input().split()[1:]
            st[y] = list(map(int, tmp))
            y += 1
        # Initialisation chaotique de la DP
        dp = []
        for _ in range(51):
            dp.append( [0]*51 )
        mx = N
        for b in range(mx):
            for a in range(mx):
                dp[a][b] = 1 << b
        for k in range(1,31):
            x = []
            l = 0
            while l < mx:
                if k in st[l]:
                    x.append(l)
                l += 1
            for i in x:
                for j in x:
                    dp[k][i] |= dp[k-1][j]
            for s in range(mx):
                dp[k][s] |= dp[k-1][s]
        r = 40
        test = lambda val: val == (1<<N) - 1
        for zz in range(31):
            j = 0
            while j < N:
                if test(dp[zz][j]):
                    r = min((r,zz))
                j += 1
        if r > 30: print(-1)
        else: print(r)

solve()