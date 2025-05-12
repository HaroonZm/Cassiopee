n = int(input())
D = [list(map(int, input().split())) for i in range(n)]
# [cost, order]
memo = {(2**n-1, i): (0, ()) for i in range(n)}
def dfs(state, pos, w):
    if (state, pos) in memo:
        return memo[state, pos]
    res = None
    for i in range(n):
        if (state >> i) & 1 == 0:
            d0 = D[pos][1]
            s, d1, v = D[i]
            r = dfs(state | (1 << i), i, w + 20*v)
            val = (r[0]+abs(d0-d1)*(70+w), r[1]+(s,))
            if res is None or val < res:
                res = val
    if res:
        memo[state, pos] = res
    return res
def solve():
    for i in range(n):
        s0, d0, v0 = D[i]
        result = dfs(1 << i, i, 20*v0)
        yield result[0], result[1]+(s0,)
ans = min(solve())
print(*reversed(ans[1]))