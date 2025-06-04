def tatami_ways(H, W):
    if (H * W) % 2 != 0:
        return 0
    from functools import lru_cache
    full = (1 << W) - 1
    @lru_cache(None)
    def dfs(row, mask, prev):
        if row == H:
            return 1 if mask == 0 else 0
        if mask == full:
            return dfs(row + 1, 0, 0)
        pos = 0
        while (mask & (1 << pos)) != 0:
            pos += 1
        res = 0
        # try horizontal tatami
        if pos + 1 < W and (mask & (1 << (pos + 1)) ) == 0:
            if not (prev & (1 << pos)) and not (prev & (1 << (pos + 1))):
                res += dfs(row, mask | (1 << pos) | (1 << (pos + 1)), prev)
        # try vertical tatami
        if row + 1 < H and not (prev & (1 << pos)):
            res += dfs(row, mask | (1 << pos), prev | (1 << pos))
        return res
    return dfs(0,0,0)

while True:
    H,W=map(int,input().split())
    if H==0 and W==0:
        break
    print(tatami_ways(H,W))