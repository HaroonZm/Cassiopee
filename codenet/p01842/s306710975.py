n, m = map(int, input().split())
*A, = map(int, input().split())
*B, = map(int, input().split())

memo = {}
def dfs(p, q, s, t, turn, pss):
    if (p, q, s, t, turn, pss) in memo:
        return memo[p, q, s, t, turn, pss]
    if p == len(A) and q == len(B):
        return s-t

    res = 0
    if turn:
        # first
        if pss < 2:
            if s+t:
                res = (s - t) + dfs(p, q, 0, 0, 0, 0)
            else:
                res = dfs(p, q, 0, 0, 0, pss+1)
        else:
            return 0
        if p < len(A):
            if A[p] == -1:
                res = max(res, dfs(p+1, q, s, 0, 0, 0))
            else:
                res = max(res, dfs(p+1, q, s+A[p], t, 0, 0))
    else:
        # second
        if pss < 2:
            if s+t:
                res = (s - t) + dfs(p, q, 0, 0, 1, 0)
            else:
                res = dfs(p, q, 0, 0, 1, pss+1)
        else:
            return 0
        if q < len(B):
            if B[q] == -1:
                res = min(res, dfs(p, q+1, 0, t, 1, 0))
            else:
                res = min(res, dfs(p, q+1, s, t+B[q], 1, 0))
    memo[p, q, s, t, turn, pss] = res
    return res
print(dfs(0, 0, 0, 0, 1, 0))