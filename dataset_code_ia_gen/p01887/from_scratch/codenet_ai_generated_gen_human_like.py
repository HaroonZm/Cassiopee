import sys
import math
sys.setrecursionlimit(10**7)

W, H, K = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

dog_blocks = set()
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    dog_blocks.add((x, y))

# Houses exist only where both coordinates are odd
# Number of houses along width and height:
wH = (W + 1) // 2
hH = (H + 1) // 2
total_houses = wH * hH

# We model the problem as a graph:
# Each house is a node.
# Edges connect houses at (x, y) to houses at (x-2, y+2), (x, y+2), (x+2, y+2) if those houses exist.
# We want to connect all houses by pipelines each starting with a special pipe at a house (root),
# and common pipes between consecutive houses in the pipeline.
# Each special pipe corresponds to one connected component.
# We want to cover all houses with K or fewer pipelines => number of connected components <= K.
# We want to minimize total cost of common pipes:
# Cost of common pipe depends on the block between two houses:
# (x, y) and (x', y') differ by y' = y + 2, and x' in {x - 2, x, x + 2}
# The common pipe is located at ( (x + x') / 2, y + 1 )
# If that block is home of a fierce dog, cost = 2, else 1 per pipe.
# Special pipes cost 0 (so don't add to cost).

# So:
# 1. Build graph of houses
# 2. Find connected components, edges weighted by cost of common pipe (1 or 2)
# 3. We want to select edges to connect houses into components
#    but must have <= K components => use MST to connect houses as much as possible
# 4. total cost = sum of costs of edges in MST (common pipes) + 0 (special pipes).
# 5. If number of MST components > K, print -1.

# Represent houses with indices for union-find:
# Map (x,y) -> id
house_id = dict()
id_house = []

idx = 0
for y in range(1, H+1, 2):
    for x in range(1, W+1, 2):
        house_id[(x, y)] = idx
        id_house.append((x, y))
        idx += 1

# Union-Find (Disjoint Set Union)
class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0]*n
        self.count = n
    def find(self,x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def unite(self,a,b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            self.par[a] = b
        else:
            self.par[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a]+=1
        self.count -= 1
        return True
    def size(self):
        return self.count

uf = UnionFind(total_houses)

edges = []

# Build edges between houses for possible pipes according to the rules:
# from house (x,y), possible next houses:
# (x-2, y+2), (x, y+2), (x+2, y+2), if they exist inside area and is a house (odd, odd)
for y in range(1, H-1, 2):
    for x in range(1, W+1, 2):
        u = house_id[(x, y)]
        for dx in [-2, 0, 2]:
            nx, ny = x + dx, y + 2
            if 1 <= nx <= W and 1 <= ny <= H and (nx, ny) in house_id:
                v = house_id[(nx, ny)]
                # common pipe position:
                cx, cy = (x + nx)//2, y + 1
                cost = 2 if (cx, cy) in dog_blocks else 1
                edges.append((cost, u, v))

# Kruskal's MST on houses to minimize common pipe cost while connecting as many as possible
edges.sort(key=lambda x: x[0])

total_cost = 0
for cost, u, v in edges:
    if uf.unite(u,v):
        total_cost += cost

# After MST, number of pipelines = number of connected components = uf.size()
if uf.size() > K:
    print(-1)
else:
    print(total_cost)