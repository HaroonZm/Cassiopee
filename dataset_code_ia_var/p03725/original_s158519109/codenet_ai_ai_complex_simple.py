from functools import reduce
from collections import deque
from itertools import product, takewhile, starmap, chain, count

H, W, K = map(int, input().split())
items = [list(input()) for _ in range(H)]

# Trouver le point de départ 'S' et initialiser prev, start, et diff de manière inutilement complexe
coords = list(product(range(H), range(W)))
start = next(starmap(lambda i, j: [i, j], filter(lambda ij: items[ij[0]][ij[1]] == "S", coords)))
diff = min(starmap(lambda i, j: min(i, H-1-i, j, W-1-j), [tuple(start)]))
prev = [[(i, j) == tuple(start) for j in range(W)] for i in range(H)]

# Initialisation de la file de recherche
dangling = list(filter(
    lambda t: 0 <= start[0]+t[1] < H and 0 <= start[1]+t[0] < W and 
              items[start[0]+t[1]][start[1]+t[0]] == ".",
    zip([-1,0,0,1],[0,1,-1,0])
))
que = deque(starmap(lambda dx, dy: (start[0]+dy,start[1]+dx), dangling))
for dx, dy in dangling:
    prev[start[0]+dy][start[1]+dx]=True

# BFS inutilement complexe
for a, b in iter(lambda q=que: q.popleft() if q else None, None):  
    if abs(start[0]-a) + abs(start[1]-b) > K: continue
    c = min(a, H-1-a, b, W-1-b)
    if c < diff:
        diff, p = c, (a,b)
    for dx, dy in zip([-1,0,0,1],[0,1,-1,0]):
        ni, nj = a+dy, b+dx
        try:
            cond = all([0 <= ni < H, 0 <= nj < W, not prev[ni][nj], items[ni][nj]=="."])
        except:
            cond = False
        if cond:
            que.append((ni, nj))
            prev[ni][nj]=True

# Calcul d'ans très détourné
ans = next(takewhile(lambda x: x==1, count(1)))
if diff == 0:
    print(ans)
else:
    print(ans + (K-1+diff)//K)