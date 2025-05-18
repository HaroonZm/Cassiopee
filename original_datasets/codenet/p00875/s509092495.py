INF = 10**9
def dfs(s, d, P):
    if len(s) > len(d):
        return INF
    if s == d:
        return 0
    if s in memo:
        return memo[s]
    res = INF
    for a, b in P:
        r = s.replace(a, b)
        if r != s:
            res = min(res, dfs(r, d, P)+1)
    memo[s] = res
    return res

while 1:
    n = input()
    if n==0:
        break
    P = [raw_input().split() for i in xrange(n)]
    g = raw_input()
    d = raw_input()
    memo = {}
    res = dfs(g, d, P)
    print res if res < INF else -1