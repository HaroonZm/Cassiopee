from heapq import heappush as HPUSH, heappop

L_numSet = list(map(str, range(10)))
R_steps = ((x, y) for x in range(-3, 0) for y in (-2, -1, 0, 1, 2) if abs(x) + abs(y) <= 3)
L_steps = list(filter(lambda t: abs(t[0]) + abs(t[1]) <= 3, [(x, y) for x in (1, 2, 3) for y in range(-2, 3)]))
INFY = 10**20
S, T = 'S', 'T'

L, R = 0, 1

def cc(v):
    try:
        return int(v)
    except:
        if v == T or v == S:
            return 0
    return -1

proceed = 1
while proceed:
    w_h = input()
    w, h = map(int, w_h.split())
    if not w:
        break
    bd = []
    for _ in range(h):
        ln = [-1] * 3 + input().split() + [-1] * 3
        bd.append(list(map(cc, ln)))
    rowlen = w + 6
    bd = [[-1] * rowlen, [-1] * rowlen] + bd + [[-1] * rowlen, [-1] * rowlen]

    def f():
        Sset, G = [], []
        for x in range(3, w+3):
            if not bd[h+1][x]: Sset.append((x, h+1))
            if not bd[2][x]:   G.append((x, 2))
        q = []; seen = dict()
        for x, y in Sset:
            for f in (L, R):
                HPUSH(q, (0, x, y, f))
                seen[(x,y,f)] = 0
        while len(q):
            tot, x, y, f = heappop(q)
            nxt, FL = (R_steps, L) if f==R else (L_steps, R)
            for dx, dy in nxt:
                nx, ny = x+dx, y+dy
                if (nx, ny) in G:
                    return tot
                v = bd[ny][nx]
                if v == -1: continue
                entry = (nx,ny,FL)
                if not entry in seen or seen[entry] > tot+v:
                    seen[entry] = tot+v
                    HPUSH(q, (tot+v, nx, ny, FL))
        return -1
    print(f())