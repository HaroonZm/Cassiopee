import sys

DBG = True and False
MAXVISIT = 400

printn = lambda x: sys.stdout.write(x)
inn = lambda: int(input())
inl = lambda: list(map(int, input().split()))
inm = lambda: map(int, input().split())

ddprint = lambda x: (print(x), sys.stdout.flush()) if DBG else None

ddprint("start")

V, E = inm()
es = []
for i in range(V+1):
    es.append([])
dist = []
for i in range(V+1):
    dist.append([9999]*(V+1))
for i in range(V+1):
    dist[i][i] = 0
for i in range(E):
    a,b,c = inm()
    es[a].append((b,c))
    es[b].append((a,c))
    dist[a][b] = c
    dist[b][a] = c

if DBG:
    for i,z in enumerate(es):
        print(str(i)+' ' + str(z))

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
ddprint("WS done")

nxtndary = []
for i in range(V+1):
    nxtndary.append([0]*(V+1))
for i in range(1,V+1):
    for j in range(1,V+1):
        if j==i:
            continue
        found = False
        for z in es[i]:
            k = z[0]
            if dist[i][j] == z[1]+dist[k][j]:
                nxtndary[i][j] = k
                found = True
                break
        if not found:
            print("nxtndary ERR")
            exit()

F = inl()
if len(F)==1:
    prob = 1
    tt = F[0]
else:
    prob = 2
    tt = inn()

pendreq = []
workreq = []
lastnd = 1
distfromlast = 0
ufary = []
ufrank = []
for t in range(tt):

    if DBG and t>3400:
        exit()

    n = inn()
    if n==1:
        x = list(inm())
        new_id = x[0]
        dst = x[1]
        pendreq.append((new_id, dst))
    if prob==2:
        n2 = inn()
        for _ in range(n2):
            inn()
    def atdepot():
        return (lastnd==1 and distfromlast==0)
    def trigger():
        return (len(pendreq)>0)
    if atdepot():
        if trigger():
            vislist = set([x[1] for x in pendreq]) | set(workreq)
            vv = len(vislist)
            pendreq = []
            if vv==1:
                workreq = list(vislist)
            else:
                e = {}
                f = {}
                for x in vislist:
                    e[x] = []
                ufary = []
                ufrank = []
                for i in range(V+1):
                    ufary.append(i)
                    ufrank.append(0)
                def ufroot(i):
                    p = ufary[i]
                    if p==i:
                        return p
                    q = ufroot(p)
                    ufary[i] = q
                    return q
                def ufmerge(i,j):
                    ri = ufroot(i)
                    rj = ufroot(j)
                    if ri==rj:
                        return
                    if ufrank[ri]>ufrank[rj]:
                        ufary[rj] = ri
                    else:
                        ufary[ri] = rj
                        if ufrank[ri]==ufrank[rj]:
                            ufrank[rj] += 1
                for _ in range(vv-1):
                    mx = -1
                    mxi = None
                    mxj = None
                    for i in e:
                        for j in e:
                            if ufroot(i)==ufroot(j):
                                continue
                            df = dist[i][1] + dist[1][j] - dist[i][j]
                            if df>mx:
                                mx = df
                                mxi = i
                                mxj = j
                    i = mxi
                    j = mxj
                    e[i].append(j)
                    e[j].append(i)
                    ufmerge(i,j)
                    if len(e[i])==2:
                        f[i] = e[i]
                        del e[i]
                    if len(e[j])==2:
                        f[j] = e[j]
                        del e[j]
                ek = list(e.keys())
                p = ek[0]
                prev = p
                cur = e[p][0]
                workreq = [p,cur]
                for i in range(vv-2):
                    p = cur
                    cur = f[p][0]
                    if cur==prev:
                        cur = f[p][1]
                    prev = p
                    workreq.append(cur)
            if len(workreq)>0:
                nxtnd = None
                tgt = workreq[0] if len(workreq)>0 else 1
                nxtnd = nxtndary[lastnd][tgt]
                print(nxtnd)
                sys.stdout.flush()
                distfromlast += 1
                if distfromlast == dist[lastnd][nxtnd]:
                    distfromlast = 0
                    if len(workreq)>0 and nxtnd == workreq[0]:
                        del workreq[0]
                    lastnd = nxtnd
            else:
                print(-1)
                sys.stdout.flush()
        else:
            print(-1)
            sys.stdout.flush()
    else:
        nxtnd = None
        tgt = workreq[0] if len(workreq)>0 else 1
        nxtnd = nxtndary[lastnd][tgt]
        print(nxtnd)
        sys.stdout.flush()
        distfromlast += 1
        if distfromlast == dist[lastnd][nxtnd]:
            distfromlast = 0
            if len(workreq)>0 and nxtnd == workreq[0]:
                del workreq[0]
            lastnd = nxtnd
    if prob==2:
        v = input().strip()
        if v != 'OK':
            exit()
        n3 = inn()
        for _ in range(n3):
            inn()