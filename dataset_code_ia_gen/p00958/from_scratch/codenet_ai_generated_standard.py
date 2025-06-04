import sys
from math import gcd
sys.setrecursionlimit(10**7)

def norm(dx, dy):
    if dx == 0:
        return (0,1)
    if dy == 0:
        return (1,0)
    g = gcd(dx,dy)
    dx //= g
    dy //= g
    if dx < 0:
        dx, dy = -dx, -dy
    return (dx, dy)

def backtrack(used, points, memo):
    if used == (1<<len(points))-1:
        return 0
    if used in memo:
        return memo[used]
    first = 0
    while (used & (1<<first)):
        first +=1
    res = 0
    trends = {}
    for j in range(first+1, len(points)):
        if not (used & (1<<j)):
            dx = points[j][0]-points[first][0]
            dy = points[j][1]-points[first][1]
            d = norm(dx, dy)
            nused = used | (1<<first) | (1<<j)
            subres = backtrack(nused, points, memo)
            # Count parallel lines formed by adding this line to the current pairing
            # lines parallel to d already counted in subres don't exist because subproblems don't know about current lines
            # So count is count of lines parallel to d in pairs not included in subres
            # Thus we store counts subtree and count pair in place: tricky, use caching approach
            # So we try a different approach: maintain counts in state? too big.
            # Instead, let's store lines and count after constructing pairs.
            # But here we do DP w/o storing pairs.
            # Fix approach: Instead, in DP, store count of lines by slope.
            # So use a dict of counts per mask? Too big
            # Alternative: store for each mask the map slope->count and max total, too big.
            # Instead, precompute all pair slopes' counts later
            # Back to original plan: store for each mask the counts of slopes
            # But huge memory
            # Alternative: brute force all matchings and compute counts after.
            # At most 8 pairs for 16 points. Number of matchings is huge.
            # But problem allows up to 16 points.
            # Implement backtracking with memoization, generating all matchings and for each compute counts.
            # Optimize by backtracking then count slopes after.
            memo_res = (subres, {})
            # But now, to break recursion, do only count lines
            res = max(res, subres)
    memo[used] = res
    return res

def all_matchings(points):
    n = len(points)
    used = [False]*n
    res = 0
    slopes = []
    def backtrack_pairs(pairs):
        nonlocal res
        i = 0
        while i < n and used[i]: i+=1
        if i==n:
            slope_count = {}
            for a,b in pairs:
                dx = points[b][0]-points[a][0]
                dy = points[b][1]-points[a][1]
                d = norm(dx, dy)
                slope_count[d] = slope_count.get(d,0)+1
            total = 0
            for v in slope_count.values():
                total += v*(v-1)//2
            if total > res:
                res = total
            return
        used[i] = True
        for j in range(i+1, n):
            if not used[j]:
                used[j] = True
                pairs.append((i,j))
                backtrack_pairs(pairs)
                pairs.pop()
                used[j] = False
        used[i] = False
    backtrack_pairs([])
    return res

m=int(sys.stdin.readline())
pts=[tuple(map(int,sys.stdin.readline().split())) for _ in range(m)]
print(all_matchings(pts))