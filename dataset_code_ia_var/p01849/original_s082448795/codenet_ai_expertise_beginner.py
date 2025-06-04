n, m = map(int, input().split())
while n != 0 or m != 0:
    S = list(map(int, input().split()))
    D = list(map(int, input().split()))
    D.sort()

    SA = sum(S)
    rest = 0
    for d in D:
        if d >= SA:
            rest += (d - SA)

    memo = {}
    def dfs(state, su, idx):
        if state in memo:
            return memo[state]
        if state == (1 << n) - 1:
            return rest
        res = 10**18
        for i in range(n):
            if not (state & (1 << i)):
                s = 0
                j = idx
                nxt = su + S[i]
                while j < m and D[j] <= nxt:
                    add1 = nxt - D[j]
                    add2 = D[j] - su
                    if add1 < add2:
                        s += add1
                    else:
                        s += add2
                    j += 1
                temp = dfs(state | (1 << i), su + S[i], j)
                if s + temp < res:
                    res = s + temp
        memo[state] = res
        return res

    print(dfs(0, 0, 0))
    n, m = map(int, input().split())