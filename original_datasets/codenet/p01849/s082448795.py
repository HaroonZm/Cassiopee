from collections import deque
while 1:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    *S, = map(int, input().split())
    D = sorted(map(int, input().split()))

    SA = sum(S)
    rest = sum(d-SA for d in D if SA <= d)

    memo = {2**n-1: rest}
    def dfs(state, su, idx):
        if state in memo:
            return memo[state]
        res = 10**18
        for i in range(n):
            if (state >> i) & 1 == 0:
                s = 0; j = idx
                nxt = su + S[i]
                while j < m and D[j] <= nxt:
                    s += min(nxt - D[j], D[j] - su); j += 1
                res = min(res, s + dfs(state | (1 << i), su + S[i], j))
        memo[state] = res
        return res
    print(dfs(0, 0, 0))