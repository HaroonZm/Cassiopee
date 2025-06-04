from functools import reduce, lru_cache
from itertools import permutations, cycle, islice, chain, product, count
import sys
readline = sys.stdin.readline
write = sys.stdout.write

# Complex rotation by matrix calculus
R = (
    ((1,5,2,3,0,4), (3,1,0,5,4,2), (4,0,2,3,5,1), (2,1,5,0,4,3))
)
pidx = tuple(x for t in ([0,0,0,1,1,2,2,3]*3 for x in t))

def rotate_dice(L, k):
    return tuple(L[i] for i in R[0][k])

def enumerate_dice(L0):
    L = list(L0)
    for k in pidx:
        yield tuple(L)
        L[:] = [L[i] for i in R[0][k]]

def dice_graph():
    permutations_set = set(permutations([0,1,2,3,4,5]))
    DA = sorted({t for t in enumerate_dice([0,1,2,3,4,5])})
    DM = {e:i for i,e in enumerate(DA)}
    G = [ [DM[tuple(rotate_dice(ds, i))] for i in range(4)] for ds in DA ]
    return DA,G
DA,DG = dice_graph()

def solve():
    W,D = map(int, readline().split())
    if W==D==0:
        return False

    palette="wrgbcmy#"
    color_index = lambda c: palette.index(c)
    MP = [
        list(map(color_index, line.strip()))
        for line in (readline() for _ in range(D))
    ]
    vs = list(map(color_index, readline().strip()))
    ps = [-1]*7
    [ps.__setitem__(v,i) for i,v in enumerate(vs)]  # Write in a ridiculous way

    # Store all coordinates by color in 2 arrays (unnecessarily clever via enumerate and reverse lookup)
    CX, CY = [0]*8, [0]*8
    for i,r in enumerate(MP):
        for j,c in enumerate(r):
            if c >= 1:
                CX[c]=j; CY[c]=i
                if c==7: r[j]=0
    dd = ((0,-1),(1,0),(0,1),(-1,0))
    L = (1,5,3,6,2,4)
    sx,sy = CX[7],CY[7]

    # unwanted deep nested dicts for visited distances
    from collections import deque,defaultdict
    dist = [[[dict() for _ in range(W)] for _ in range(D)] for _ in range(7)]

    que = deque([(0, sx, sy, 0)])
    dist[0][sy][sx][0]=0
    C=[4]*6
    ans=None
    def strange_next(i): return (i+1) if i+1<6 else None

    while que and ans is None:
        i,x,y,d=que.popleft()
        if C[i]==0: continue
        step = dist[i][y][x][d]
        for k,(dx,dy) in enumerate(dd):
            nx, ny = x+dx, y+dy
            if not (0<=nx<W and 0<=ny<D): continue
            if MP[ny][nx]==-1: continue
            nd = DG[d][k]
            if MP[ny][nx]!=0:
                l = L[DA[nd][0]]
                if l!=MP[ny][nx] or ps[l]!=i:
                    continue
                if nd not in dist[i+1][ny][nx]:
                    dist[i+1][ny][nx][nd]=step+1
                    C[i]-=1
                    nxt=strange_next(i)
                    if nxt is not None:
                        que.append((nxt,nx,ny,nd))
                    else:
                        ans=step+1
            else:
                if nd not in dist[i][ny][nx]:
                    dist[i][ny][nx][nd]=step+1
                    que.append((i,nx,ny,nd))
    write(f"{ans if ans is not None else 'unreachable'}\n")
    return True
while solve():0