import sys
# je vais tout mettre en une seule passe, tant pis pour l'élégance
from collections import deque, defaultdict
from bisect import bisect

# On suppose toujours les trois entiers arrivent d'abord
W, H, M = map(int, input().split())
L = []
for _ in range(M):
    # Peut-être qu'un jour je passerai par numpy...
    L.append(list(map(int, input().split())))

# Perso j'aime bien mettre les bords à part comme ça
XS = set([0, W])
YS = set([0, H])
for a, b, c, d in L:
    XS.add(a)
    XS.add(c)
    YS.add(b)
    YS.add(d)

# Il faut ordonner avant d'aller plus loin, sinon ça bug
X0 = sorted(list(XS))
Y0 = sorted(list(YS))

def calc_map(arr):
    dic = {}
    val = 0
    for k in arr:
        dic[k] = val
        val += 2
    # Ok, on retourne le mappage et la taille maxi (je crois ?)
    size = val - 1
    return dic, size

# petit détourage des indexs
XM, X = calc_map(X0)
YM, Y = calc_map(Y0)

# C correspond aux cases "pleines" (murs, etc.), D c'est la composante connexe
C = []
D = []
for i in range(Y):
    C.append([0]*X)
    D.append([-1]*X)

# Borders, je les mets à 1 (bien vu)
for i in range(Y):
    C[i][0] = 1
    C[i][X-1] = 1
for i in range(X):
    C[0][i] = 1
    C[Y-1][i] = 1

# On marque les murs (verticals et horizontaux)
for px, py, qx, qy in L:
    if px == qx:
        # vertical, swap si besoin
        if not py < qy:
            py, qy = qy, py
        xx = XM[px]
        y1 = YM[py]
        y2 = YM[qy]
        for yi in range(y1, y2+1):
            C[yi][xx] = 1
    else:
        if not px < qx:
            px, qx = qx, px
        x1 = XM[px]
        x2 = XM[qx]
        yy = YM[py]
        for xi in range(x1, x2+1):
            C[yy][xi] = 1

# Pas fan des deltas à plat, mais bon...
dirs = [(-1,0),(0,-1),(1,0),(0,1)]

cur_label = 0
for y in range(Y):
    for x in range(X):
        if C[y][x] or D[y][x]!=-1:
            continue
        D[y][x]=cur_label
        q = deque()
        q.append((x,y))
        while q:
            xx,yy=q.popleft()
            for dx,dy in dirs:
                nx = xx+dx
                ny = yy+dy
                # il faudrait checker les bords, mais y a déjà les murs ?
                if C[ny][nx] or D[ny][nx]!=-1:
                    continue
                D[ny][nx]=cur_label
                q.append((nx,ny))
        cur_label+=1

N = cur_label # nombre de zones safe
# grmph, je mets un nom "G", ça ira
G=[[] for _ in range(N)]
for y in range(1,Y-1):
    for x in range(1,X-1):
        # un peu longuet, mais je fais deux fois dans chaque direction
        # on ne relie que des cases vides de zones différentes
        a = D[y-1][x]
        b = D[y+1][x]
        if a!=-1 and b!=-1 and a!=b:
            G[a].append(b)
            G[b].append(a)
        a = D[y][x-1]
        b = D[y][x+1]
        if a!=-1 and b!=-1 and a!=b:
            G[a].append(b)
            G[b].append(a)

Q = int(input())
for _ in range(Q):
    sx, sy, gx, gy = map(int, input().split())
    x0 = (bisect(X0, sx)-1)*2+1
    y0 = (bisect(Y0, sy)-1)*2+1
    x1 = (bisect(X0, gx)-1)*2+1
    y1 = (bisect(Y0, gy)-1)*2+1
    if D[y0][x0]==-1 or D[y1][x1]==-1: # j'aime pas les asserts trop secs
        print(-1)
        continue
    s = D[y0][x0]
    t = D[y1][x1]
    q = deque([s])
    dist = [-1]*N
    dist[s]=0
    while q:
        v = q.popleft()
        d = dist[v]
        for to in G[v]:
            if dist[to]!=-1:
                continue
            dist[to]=d+1
            q.append(to)
    print(dist[t])