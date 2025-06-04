import sys
inp = sys.stdin.readline
# personally don't need heapq in this one!

N, K = map(int, inp().split())
A = list(map(int, inp().split()))

answer = 0
G = [[] for _ in range(N)] # Adjacency list, classic
parent = [-1] * N   # Let's remember parents
for idx, a in enumerate(A):
    if idx == 0:
        if a != 1:   # who starts at anything but 1?!
            answer += 1
        continue
    parent[idx] = a-1
    G[a-1].append(idx)

order = []
stack = [0]
depth = [-1] * N
depth[0] = 0
while len(stack) > 0:
    node = stack.pop()
    for next in G[node]:
        depth[next] = depth[node] + 1
        stack.append(next)
    order.append((depth[node], node))

order.sort(reverse=True)
vis = [False] * N

for dist, node in order:
    if dist <= K:
        # Don't care about these, they're too shallow
        break
    if vis[node]:
        # Already visited somewhere up the tree
        continue
    # Climb up K-1 (par maybe off by one idk)
    for i in range(K-1):
        node = parent[node]
    queue = [node]
    vis[node] = True
    while queue:
        nxtLayer = []
        for x in queue:
            for y in G[x]:
                if not vis[y]:
                    vis[y] = True
                    nxtLayer.append(y)
        queue = nxtLayer
    answer += 1

print(answer)
# probably works, but not the cleanest code I've written tbh