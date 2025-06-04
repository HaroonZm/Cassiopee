from heapq import heappush as _hpush, heappop
R, L = 1, 0
Rnext = [(a, b) for a in range(-3, 0) for b in (-2, -1, 0, 1, 2) if abs(a)+abs(b) <= 3]
Lnext = []
for dx in [1,2,3]:
    for dy in range(-2,3):
        if abs(dx) + abs(dy) <= 3:
            Lnext.append((dx, dy))
DIG = []
for c in range(10): DIG.append(str(c))
OO = 100000000000000000000
def getval(c):
    if c in DIG: return int(c)
    elif c == 'T' or c == 'S': return 0
    return -1

while 1:
    w_h = input().split()
    w = int(w_h[0]); h = int(w_h[1])
    if w==0: break
    rawmp = []
    for _ in range(h):
        l = input().split()
        line = [-1]*3 + l + [-1]*3
        rawmp.append(list(map(getval, line)))
    rawmp = [[-1]*(w+6), [-1]*(w+6)] + rawmp + [[-1]*(w+6), [-1]*(w+6)]
    starts, goals = [], []
    for xi in range(3, w+3):
        if rawmp[h+1][xi]==0:    starts.append((xi,h+1))
        if rawmp[2][xi]==0:      goals.append((xi,2))
    q = []
    visited = dict()
    for s in starts:
        for foot in (L, R):
            _hpush(q, (0, s[0], s[1], foot))
            visited[s[0], s[1], foot] = 0
    while len(q):
        t, px, py, f = heappop(q)
        dirs = (Rnext if f==R else Lnext)
        nf = (L if f==R else R)
        for dxy in dirs:
            xx, yy = px+dxy[0], py+dxy[1]
            v = rawmp[yy][xx]
            if v==-1: continue
            key = (xx,yy,nf)
            s = t+v
            if key not in visited or visited[key] > s:
                visited[key] = s
                _hpush(q, (s, xx, yy, nf))
    answer = OO
    for qx, qy in goals:
        for f in (L,R):
            p = (qx,qy,f)
            if p in visited and visited[p]<answer: answer=visited[p]
    print(answer if answer!=OO else -1)