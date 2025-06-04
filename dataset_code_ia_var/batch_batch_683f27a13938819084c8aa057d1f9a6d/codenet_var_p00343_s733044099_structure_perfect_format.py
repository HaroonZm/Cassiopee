n = int(input())
for i in range(n):
    F = set(map(int, input().split()))
    fl = min(F)
    fr = max(F)
    G = {i for i in range(1, 14)} - F - {7}
    gl = min(G)
    gr = max(G)

    memo = {}

    def dfs(s, t, u):
        if (s, t, u) in memo:
            return memo[s, t, u]
        T = [G, F][u]
        res = 0
        if s - 1 in T:
            if s - 1 <= [gl, fl][u] and [gr, fr][u] <= t:
                res = 1
            else:
                res |= dfs(s - 1, t, u ^ 1) ^ 1
        if t + 1 in T:
            if s <= [gl, fl][u] and [gr, fr][u] <= t + 1:
                res = 1
            else:
                res |= dfs(s, t + 1, u ^ 1) ^ 1
        if s - 1 not in T and t + 1 not in T:
            res = dfs(s, t, u ^ 1) ^ 1
        memo[s, t, u] = res
        return res

    print(["no", "yes"][dfs(7, 7, 1)])