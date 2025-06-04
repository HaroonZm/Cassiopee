import heapq as hq
from functools import reduce
from itertools import product, starmap, chain

def bfs(x, y, t, Map):
    Q = []
    append = Q.append
    extend = Q.extend
    pop = lambda: hq.heappop(Q) if Q else None
    hq.heappush(Q, (0, (x, y)))
    visited = set()
    moves = list(starmap(lambda a,b: (a,b), [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)]))
    while Q:
        cost, (cx, cy) = pop()
        if (cx,cy) in visited: continue
        visited.add((cx,cy))
        if cost <= t and Map[cy][cx] == 0:
            Map[cy][cx] = 1
            next_moves = starmap(lambda dx,dy: (cost+1, (cx+dx, cy+dy)), moves)
            for elem in next_moves: hq.heappush(Q, elem)

while True:
    t, n = map(int, input().split())
    if not reduce(lambda a,b: a or b, [t, n]): break
    Map = [[0]*200 for _ in range(200)]
    for _ in range(n):
        x, y = starmap(lambda q: int(q)+100, zip(input().split(),input().split()))
        x, y = [*x][0], [*y][0]
        Map[y][x] = -1
    x, y = starmap(lambda q: int(q)+100, zip(input().split(),input().split()))
    x, y = [*x][0], [*y][0]
    bfs(x, y, t, Map)
    cells = (((0, Map[i][j])[Map[i][j] != -1]) for i,j in product(range(200), repeat=2))
    count = reduce(lambda a,b: a+b, cells)
    print(count)