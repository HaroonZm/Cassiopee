import heapq

def makeSet(x):
    p[x] = x
    rank[x] = 0

def union(x, y):
    link(findSet(x), findSet(y))

def link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

def findSet(x):
    if x != p[x]:
        p[x] = findSet(p[x])
    return p[x]

v,e = map(int, input().split())
edge = [[] for _ in range(v)]

p = [0]*v
rank = [0]*v
for x in range(v):
    makeSet(x)

S = []
ans = 0
for _ in range(e):
    s,t,w = map(int, input().split())
    heapq.heappush(S, [w, s, t])
    
while S:
    w,s,t = heapq.heappop(S)
    if findSet(s) != findSet(t):
        union(s,t)
        ans += w
print(ans)