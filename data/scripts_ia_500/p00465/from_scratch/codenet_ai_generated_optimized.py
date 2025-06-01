import sys
import collections
import bisect
input=sys.stdin.readline

def bfs(L, W, H, X, Y, level):
    if level < 1:  # can't enter elevator hall if clearance < 1
        return 0
    q = collections.deque()
    q.append((X-1,Y-1))
    vis = [[False]*W for _ in range(H)]
    vis[Y-1][X-1] = True
    cnt = 1
    while q:
        x,y = q.popleft()
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<W and 0<=ny<H and not vis[ny][nx] and L[ny][nx]<=level:
                vis[ny][nx] = True
                cnt += 1
                q.append((nx, ny))
    return cnt

def max_reachable(L, W, H, X, Y, level):
    return bfs(L, W, H, X, Y, level)

def solve():
    while True:
        R = int(input())
        if R == 0:
            break
        W1,H1,X1,Y1 = map(int,input().split())
        L1 = [list(map(int,input().split())) for _ in range(H1)]
        W2,H2,X2,Y2 = map(int,input().split())
        L2 = [list(map(int,input().split())) for _ in range(H2)]

        max_level_1 = max(max(row) for row in L1)
        max_level_2 = max(max(row) for row in L2)

        # binary search on sum = a+b (a for office1, b for office2)
        # For each possible a, calculate max rooms in office1; for b= sum - a, calc max rooms in office2
        # try all a in [0..sum], sum in [0..max_level_1 + max_level_2] but this is huge
        # optimize: for counting reachable rooms for levels, precompute for all possible levels? impossible due to 10^8 max levels

        # Alternative: For each office, precompute for discrete sorted unique levels the number of reachable rooms
        # Then for a fixed level, number of reachable rooms non-decreasing
        # Then do binary search per office

        # Extract unique levels sorted, for office1 and office2
        levels1 = sorted({val for row in L1 for val in row})
        levels2 = sorted({val for row in L2 for val in row})

        # Precompute for office1: for each level in levels1, compute reachable rooms
        reachable1 = []
        for lv in levels1:
            reachable1.append(bfs(L1,W1,H1,X1,Y1,lv))
        # add 0 clearance (can't even enter elevator hall)
        levels1 = [0]+levels1
        reachable1 = [0]+reachable1

        # Same for office2
        reachable2 = []
        for lv in levels2:
            reachable2.append(bfs(L2,W2,H2,X2,Y2,lv))
        levels2 = [0]+levels2
        reachable2 = [0]+reachable2

        # For fast query of max reachable given clearance <= some level, use levels and reachable sorted increasing
        # Since reachable is nondecreasing with level

        # For levels1 and levels2, they are sorted ascending

        # For possible sums of clearance level from 0 to max_level_1 + max_level_2, find minimal sum that sum of rooms >= R

        # But max_level can be as big as 10^8, impossible to search naively

        # Observation: Levels are sparse and only certain levels are needed. Try all possible pairs of (a,b) with a in levels1, b in levels2

        # For each a in levels1, find minimal b in levels2 with reachable1[a] + reachable2[b] >= R
        # Use binary search on levels2 reachable

        ans = 10**15
        for i,a in enumerate(levels1):
            rooms1 = reachable1[i]
            need = R - rooms1
            if need <= 0:
                # no need for office2 clearance
                ans = min(ans, a)
                continue
            # want b minimal with reachable2[b_index]>=need
            idx = bisect.bisect_left(reachable2, need)
            if idx<len(reachable2):
                b = levels2[idx]
                ans = min(ans, a+b)

        print(ans)

if __name__ == "__main__":
    solve()