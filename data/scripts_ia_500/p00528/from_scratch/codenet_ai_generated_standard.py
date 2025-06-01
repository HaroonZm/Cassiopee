import sys
import collections

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

M, N, K = map(int, input().split())
switches = set()
for _ in range(K):
    x, y = map(int, input().split())
    switches.add((x, y))

# 状態 s = 0: 東西扉閉、南北扉開
# 状態 s = 1: 東西扉開、南北扉閉

# 各状態での移動方向と条件
# s=0: 南北方向に移動可能（上下移動）
# s=1: 東西方向に移動可能（左右移動）

from heapq import heappush, heappop

def neighbors(x, y, s):
    if s == 0:
        # 南北移動(上下), y-1 or y+1
        if y > 1:
            yield (x, y-1)
        if y < N:
            yield (x, y+1)
    else:
        # 東西移動(左右), x-1 or x+1
        if x > 1:
            yield (x-1, y)
        if x < M:
            yield (x+1, y)

# 状態 = (x,y,s), sは扉の開閉状態
# 距離配列は不要で、訪問済み管理のみでよいが
# 最短時間を求めるためには優先度付きキューで探索(BFSでもよいが1分刻みなので Dijkstra)
dist = {}
start = (1,1,0)
dist[start] = 0
hq = [(0,1,1,0)]

while hq:
    d, x, y, s = heappop(hq)
    if (x,y) == (M,N):
        print(d)
        sys.exit()
    if dist[(x,y,s)] < d:
        continue
    # 移動
    for nx, ny in neighbors(x,y,s):
        ns = s
        nd = d+1
        if (nx, ny, ns) not in dist or dist[(nx, ny, ns)] > nd:
            dist[(nx, ny, ns)] = nd
            heappush(hq, (nd, nx, ny, ns))
    # スイッチ押す（扉開閉状態切替）可能なら
    if (x,y) in switches:
        ns = 1 - s
        nd = d + 1
        if (x, y, ns) not in dist or dist[(x, y, ns)] > nd:
            dist[(x, y, ns)] = nd
            heappush(hq, (nd, x, y, ns))

print(-1)