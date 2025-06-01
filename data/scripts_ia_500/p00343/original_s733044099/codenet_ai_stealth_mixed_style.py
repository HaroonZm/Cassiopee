def main():
    n = int(input())
    from functools import lru_cache

    for _ in range(n):
        F = set(map(int, input().split()))
        fl, fr = min(F), max(F)
        G = set(range(1,14)).difference(F).difference({7})
        gl, gr = min(G), max(G)

        memo = {}

        def dfs(s, t, u):
            if (s, t, u) in memo:
                return memo[(s, t, u)]
            T = [G, F][u]
            res = 0

            # recursive checks with bitwise ops
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

            if (s - 1 not in T) and (t + 1 not in T):
                res = dfs(s, t, u ^ 1) ^ 1

            memo[(s, t, u)] = res
            return res

        print("yes" if dfs(7,7,1) else "no")

if __name__ == "__main__":
    # procedural + functional + object-oriented 
    main()