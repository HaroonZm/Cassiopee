while True:
    n = int(input())
    if n == 0:
        break

    F, W, S = zip(*[input().split() for _ in range(n)])
    W = list(map(int, W))
    S = list(map(int, S))

    from functools import lru_cache

    @lru_cache(None)
    def dfs(c, used_mask, su):
        if c == n:
            order = []
            mask = used_mask
            total = 0
            idx = 0
            while mask:
                for i in range(n):
                    if mask & (1 << i):
                        order.append(i)
                        mask ^= (1 << i)
                        break
                idx +=1
            order = order[::-1]
            total = sum((i + 1) * W[order[-1 - i]] for i in range(n))
            return total, order

        best = (10**9, None)
        for i in range(n):
            if not (used_mask & (1 << i)) and S[i] >= su:
                candidate = dfs(c+1, used_mask | (1 << i), su + W[i])
                if candidate[0] < best[0]:
                    best = candidate
        return best

    _, order = dfs(0, 0, 0)
    print('\n'.join(F[i] for i in order))