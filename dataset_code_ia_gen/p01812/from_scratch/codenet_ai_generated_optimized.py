from collections import deque
N, M, K = map(int, input().split())
dark = list(map(int, input().split()))
adj = [list(map(int, [input() for _ in range(K)])) for _ in range(N)]
# Preprocessing adjacency: adj[i][j] with zero-based i,j
graph = [list(map(int, input().split())) for _ in range(N)]
# Actually input differs, read v_{i,1}..v_{i,K} per line per room
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dark_set = set(dark)
bright = set(range(1, N + 1)) - dark_set

# For bitmask, map dark room number to index 0..M-1
index = {room: i for i, room in enumerate(dark)}

# initial state: all dark rooms active -> mask with all bits set
full_mask = (1 << M) - 1

from collections import deque
queue = deque()
visited = set()
queue.append((full_mask,0))
visited.add(full_mask)

while queue:
    mask, depth = queue.popleft()
    if mask == 0:
        print(depth)
        break
    for i in range(K):
        nxtmask = 0
        for j in range(M):
            room = dark[j]
            if mask & (1 << j):
                nxtroom = graph[room - 1][i]
                if nxtroom in dark_set:
                    nxtmask |= 1 << index[nxtroom]
        if nxtmask not in visited:
            visited.add(nxtmask)
            queue.append((nxtmask, depth + 1))