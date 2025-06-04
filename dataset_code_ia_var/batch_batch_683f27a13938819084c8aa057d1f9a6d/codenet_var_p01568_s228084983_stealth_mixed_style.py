from collections import deque
import sys

# Style: aliasing and inline assignment
rd = sys.stdin.readline
wr = sys.stdout.write

# Style: Tuple unpack/calc inline
def DD3(o, a, b):
    return (a[0]-o[0])*(b[0]-o[0]) + (a[1]-o[1])*(b[1]-o[1])

# Style: procedural with ; delimiter
def fC(O,A,B):
    ox,oy=O;ax,ay=A;bx,by=B;
    return (ax-ox)*(by-oy)-(bx-ox)*(ay-oy)

# Style: explicit indices with list
def d2(A,B):
    return (A[0]-B[0])**2 + (A[1]-B[1])**2

# Style: classless, duck-typing
def has_intersect(lineA, lineB):
    P0=lineA[:2]; P1=lineA[2:]; Q0=lineB[:2]; Q1=lineB[2:]
    c0, c1 = fC(P0,P1,Q0), fC(P0,P1,Q1)
    d0, d1 = fC(Q0,Q1,P0), fC(Q0,Q1,P1)
    return (not (c0==c1==0)) and (c0*c1<=0 and d0*d1<=0)

# Mix: imperative + exception
def crpt(L1, L2):
    x0, y0, x1, y1 = L1
    x2, y2, x3, y3 = L2
    dx0 = x1 - x0
    dy0 = y1 - y0
    dx1 = x3 - x2
    dy1 = y3 - y2
    s = (y0-y2)*dx1 - (x0-x2)*dy1
    sm = dx0*dy1 - dy0*dx1
    if s < 0:
        s, sm = -s, -sm
    if s == 0:
        return (x0, y0)
    elif s == sm:
        return (x1, y1)
    else:
        try:
            return (x0 + s*dx0/sm, y0 + s*dy0/sm)
        except ZeroDivisionError:
            return (x0, y0)  # fallback, should not occur

# Mix de styles + layouts
def main():
    N, M = map(int, rd().split())
    mp = {}
    segs = []
    # We scan and collect all points
    for _ in range(N):
        x1,y1,x2,y2 = map(int, rd().split())
        for p in [(x1, y1), (x2, y2)]: mp[p] = 0
        segs.append((x1, y1, x2, y2))
    # All intersections
    for i, line in enumerate(segs):
        for j in range(i+1, N):
            oline = segs[j]
            if has_intersect(line, oline):
                x, y = crpt(line, oline)
                mp[(x, y)] = 0
    # Read forbidden/bonus points
    for _ in range(M):
        x, y = map(int, rd().split())
        mp[(x, y)] = 1
    xb, yb = map(int, rd().split())
    mp[(xb, yb)] = 2
    xc, yc = map(int, rd().split())
    mp[(xc, yc)] = 2

    # Mix: inlined values, star tuples
    pts1 = list(mp.keys())
    pts1.sort(key=lambda x: (x[0], x[1]))
    node = {e:i for i, e in enumerate(pts1)}
    pts2 = list(mp.keys())
    pts2.sort(key=lambda x: (x[1], x[0]))

    # set up graph data
    K=len(pts1); G=[[] for _ in range(K)]; ES=[]
    idx2 = [node[p] for p in pts2]
    flag = [mp[p] for p in pts1]
    for ix, (x1, y1, x2, y2) in enumerate(segs):
        v = []
        # Functional composition, different orderings
        if x1 != x2:
            if not x1 <= x2: x1, y1, x2, y2 = x2, y2, x1, y1
            for k, (x, y) in enumerate(pts1):
                if x1 <= x <= x2 and abs((x-x1)*(y2-y1)-(y-y1)*(x2-x1)) < 1e-6:
                    v.append(k)
        else:
            if not y1 <= y2: y1, y2 = y2, y1
            for k, (x, y) in zip(idx2, pts2):
                if y1 <= y <= y2 and abs((x-x1)*(y2-y1)-(y-y1)*(x2-x1)) < 1e-6:
                    v.append(k)
        for i in range(len(v)-1):
            a, b = v[i], v[i+1]
            G[a].append(b); G[b].append(a)
            ES.append((a,b) if a <= b else (b,a))
    s, t = node[(xc, yc)], node[(xb, yb)]

    # BFS1
    queue = deque([s])
    U = [0]*K; U[s]=1
    eused = set()
    while queue:
        v = queue.popleft()
        for w in G[v]:
            if w == t:
                wr("-1\n")
                return
            e = (v,w) if v <= w else (w,v)
            eused.add(e)
            if not U[w] and flag[w] != 1:
                queue.append(w)
            U[w]=1

    # BFS2, different style
    queue = deque(); queue.append(t)
    used2 = [0]*K; used2[t]=1
    eused2 = set()
    while len(queue):
        v = queue.popleft()
        for w in G[v]:
            e = (v,w) if v<=w else (w,v)
            if e in eused:
                continue
            eused2.add(e)
            if not used2[w]:
                queue.append(w); used2[w]=1

    # Sum up unused edges
    s = 0.
    for a,b in ES:
        if (a,b) in eused2:
            continue
        x1,y1=pts1[a];x2,y2=pts1[b]
        s += ((x2-x1)**2+(y2-y1)**2)**.5
    wr("%.16f\n"%s)

main()