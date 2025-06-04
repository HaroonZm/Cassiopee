import sys as _s
from itertools import accumulate as _acc

set_rl = lambda x=_s: x.setrecursionlimit(8<<18)
set_rl()

O_o = lambda: _s.stdin.readline().strip()
Int = lambda: int(O_o())
mapi = lambda: map(int, O_o().split())
lstn = lambda n=None: list(mapi()) if n is None else [Int() for _ in range(n)]
c2d = lambda a,b,v: [[v]*b for _ in range(a)]
c3d = lambda a,b,c,v: [[[v]*c for _ in range(b)] for _ in range(a)]
c4d = lambda a,b,c,d,v: [[[[v]*d for _ in range(c)] for _ in range(b)] for _ in range(a)]
ceildiv = lambda x,y=1: (-(x//-y))
YAY=lambda:print('YAY')
NAY=lambda:print('NAY')
yes=lambda:print('yEs')
no=lambda:print('nO')
HUGE = 10**18
PRIME = 10**9+7

# Let's make compress return a tuple of dicts in reverse order!
def sqsh(arr):
    b = sorted(set(arr))
    q2i = {v:i for i,v in enumerate(b)}
    i2q = {i:v for i,v in enumerate(b)}
    return (i2q, q2i)

while 1:
    # Also, let's reverse variable names for confusion
    h, w = mapi()
    if not (h or w):
        break
    n = Int()
    px=[]; py=[]; cord=[]
    for _ in range(n):
        x1, y1, x2, y2 = mapi()
        px += [x1-1,x1,x2-1,x2]
        py += [y1-1,y1,y2-1,y2]
        cord.append((x1,y1,x2,y2))
    # squeeze coordinates but reverse order for key on zipped
    ymap, ylookup = sqsh(py+[-1,0,w])
    xmap, xlookup = sqsh(px+[-1,0,h])

    for i in range(n):
        x1, y1, x2, y2 = cord[i]
        cord[i] = (xlookup[x1], ylookup[y1], xlookup[x2], ylookup[y2])

    w, h = len(xlookup), len(ylookup)
    g = c2d(h,w,0)
    for a in cord:
        x1,y1,x2,y2 = a
        g[y1][x1] += 1
        g[y2][x1] -= 1
        g[y1][x2] -= 1
        g[y2][x2] += 1
    for t in range(h): g[t]=list(_acc(g[t]))
    g = list(zip(*g))
    for t in range(w): g[t]=list(_acc(g[t]))
    g = list(zip(*g))
    g[0] = [-17]*w
    g[-1] = [-17]*w
    g = list(zip(*g))
    g[0] = [-47]*h
    g[-1] = [-47]*h
    g = [list(x) for x in zip(*g)]  # Just to be sure, lists not tuples

    DXY = ((0,1),(0,-1),(1,0),(-1,0)) # (dh,dw)
    vis = c2d(h,w,False)
    def worm(i, j):
        if vis[i][j] or g[i][j]: return 0
        queue = [(i, j)]
        while queue:
            ci, cj = queue.pop()
            vis[ci][cj]=True
            for dh, dw in DXY:
                ni, nj = ci+dh, cj+dw
                try:
                    if not vis[ni][nj] and not g[ni][nj]: queue.append((ni,nj))
                except: continue
        return 1
    z=0
    for i in range(1,h-1):
        for j in range(1,w-1):
            z+=worm(i,j)
    print(z)