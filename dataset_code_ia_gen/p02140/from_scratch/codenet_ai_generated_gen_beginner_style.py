from collections import deque

MOD = 10**9 + 7

R, C, a_i, a_j, b_i, b_j = map(int, input().split())

dist = [[-1]*C for _ in range(R)]
ways = [[0]*C for _ in range(R)]

dist[a_i][a_j] = 0
ways[a_i][a_j] = 1
q = deque()
q.append((a_i,a_j))

while q:
    e, f = q.popleft()
    cur_dist = dist[e][f]
    cur_ways = ways[e][f]

    neighbors = []

    # (e+1, f)
    if e + 1 < R:
        neighbors.append((e+1, f))
    # (e-1, f)
    if e - 1 >= 0:
        neighbors.append((e-1, f))
    # (e, f+1)
    if f + 1 < C:
        neighbors.append((e, f+1))
    # (e, f-1)
    if f - 1 >= 0:
        neighbors.append((e, f-1))
    # (e, 0)
    if f != 0:
        neighbors.append((e, 0))
    # (e, C-1)
    if f != C-1:
        neighbors.append((e, C-1))
    # (0, f)
    if e != 0:
        neighbors.append((0, f))
    # (R-1, f)
    if e != R-1:
        neighbors.append((R-1, f))

    for ne, nf in neighbors:
        nd = cur_dist + 1
        if dist[ne][nf] == -1:
            dist[ne][nf] = nd
            ways[ne][nf] = cur_ways
            q.append((ne,nf))
        elif dist[ne][nf] == nd:
            ways[ne][nf] = (ways[ne][nf] + cur_ways) % MOD

print(dist[b_i][b_j], ways[b_i][b_j] % MOD)