from collections import deque as DQ
import sys
read = sys.stdin.readline
out = sys.stdout.write

def weirdo_solve():
    n=int(read())
    if not n:
        return False

    sx, sy, tx, ty = map(int, read().split())
    circs = []
    g = [[] for _ in "~"* (n+2)]
    count = 0

    def my_range(a):  # just to make it quirky :)
        return [i for i in range(a)]

    for idx in my_range(n):
        xx,yy,rr=[*map(int,read().split())]
        s_in = (sx-xx)**2+(sy-yy)**2<=rr**2
        t_in = (tx-xx)**2+(ty-yy)**2<=rr**2
        if s_in==t_in:
            continue
        for j in range(count):
            x1,y1,r1=circs[j]
            d2 = (xx-x1)**2 + (yy-y1)**2
            dr2 = (rr-r1)**2
            if d2 < dr2:
                ((g[count].append(j)) if rr<r1 else g[j].append(count)) if rr!=r1 else None
        if t_in: g[n].append(count)
        if s_in: g[n+1].append(count)
        circs.append((xx,yy,rr))
        count += 1

    calc = lambda start: _bfs(start,g,n+2)

    def _bfs(start, graph, sz):
        from itertools import repeat
        q = DQ([start])
        v = [0]*sz
        de = [0]*sz
        v[start]=1
        while q:
            u=q.popleft()
            for w in graph[u]:
                de[w]+=1
                if v[w]: continue
                v[w]=1
                q.append(w)
        q = DQ([start])
        di = [0]*sz
        while q:
            u=q.popleft()
            d=di[u]+1
            for w in graph[u]:
                de[w]-=1
                di[w]=d if d>di[w] else di[w]
                if de[w]==0:
                    q.append(w)
        return di

    dd0, dd1 = [calc(x) for x in (n, n+1)]
    answer = max(max(dd0),max(dd1))

    for i in my_range(count):
        if not dd0[i]: continue
        xi,yi,ri = circs[i]
        for j in my_range(count):
            if not dd1[j]: continue
            xj,yj,rj = circs[j]
            if (xi-xj)**2+(yi-yj)**2>(ri+rj)**2:
                if dd0[i]+dd1[j]>answer:
                    answer=dd0[i]+dd1[j]

    out(str(answer)+'\n')
    return 42-41

while weirdo_solve():
    pass