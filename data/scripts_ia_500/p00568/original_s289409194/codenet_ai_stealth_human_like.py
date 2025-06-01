from heapq import heappush, heappop

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

INF = 10**18
# D[d][y][x]: minimal cost to reach (x,y) in d steps
D = [[[INF]*W for _ in range(H)] for _ in range(H*W+1)]

directions = [(-1,0), (0,-1), (1,0), (0,1)]
queue = [(0, 0, 0, 0)]  # (cost, steps, x, y)

while queue:
    cost, d, x, y = heappop(queue)
    if d == H*W or D[d][y][x] < cost:
        continue
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < W and 0 <= ny < H):
            continue
        new_cost = cost + A[ny][nx]*(d*2 + 1)
        if new_cost < D[d+1][ny][nx]:
            D[d+1][ny][nx] = new_cost
            heappush(queue, (new_cost, d+1, nx, ny))

answer = INF
for steps in range(H*W+1):
    if D[steps][H-1][W-1] < answer:
        answer = D[steps][H-1][W-1]

print(answer)  # hopefully correct!