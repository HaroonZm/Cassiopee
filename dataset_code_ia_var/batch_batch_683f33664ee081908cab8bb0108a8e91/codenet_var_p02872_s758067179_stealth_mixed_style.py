import sys

def prn(x): sys.stdout.write(x)
def gin(): return int(input())
def lint(): return list(map(int, input().split()))
def gm(): return map(int, input().split())
_dbg = False if True else True
MAXVISIT = 400

def printer(msg): 
    if _dbg: 
        print(msg)
        sys.stdout.flush()

class UnionF:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0]*n
    def root(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def merge(self, x, y):
        rx, ry = self.root(x), self.root(y)
        if rx == ry: return
        if self.r[rx] > self.r[ry]:
            self.p[ry] = rx
        else:
            self.p[rx] = ry
            if self.r[rx] == self.r[ry]:
                self.r[ry] += 1

def depot_here(): return last_node == 1 and dist_last == 0
def nothin_do():
    print(-1)
    sys.stdout.flush()

def get_next():
    tg = work[0] if work else 1
    return narray[last_node][tg]

def moveon():
    global last_node, dist_last, work
    n = get_next()
    print(n)
    sys.stdout.flush()
    dist_last += 1
    if dist_last == dist[last_node][n]:
        dist_last = 0
        if work and n == work[0]:
            work.pop(0)
        last_node = n

def trgr(): return len(pend) > 0

def readput(): 
    n = gin()
    [gin() for _ in range(n)]

def readverd():
    val = input().strip()
    if val != 'OK': exit()
    readput()

def setwork_wright():
    global pend, work
    vis = set(j for _,j in pend) | set(work)
    vv = len(vis)
    pend = []
    if vv == 1:
        work = list(vis)
        return
    e,f = dict(),dict()
    for x in vis: e[x]=[]
    uf = UnionF(V+1)
    for _ in range(vv-1):
        best=(-1,None,None)
        for i in e:
            for j in e:
                if uf.root(i)==uf.root(j): continue
                dif = dist[i][1] + dist[1][j] - dist[i][j]
                if dif > best[0]:
                    best = (dif,i,j)
        _,i,j = best
        e[i].append(j); e[j].append(i)
        uf.merge(i,j)
        if len(e[i])==2: f[i]=e[i]; del e[i]
        if len(e[j])==2: f[j]=e[j]; del e[j]
    ek = list(e.keys())
    p = ek[0]; cur = e[p][0]; prev = p
    work = [p,cur]
    for _ in range(vv-2):
        p = cur
        cur = f[p][0] if f[p][0]!=prev else f[p][1]
        prev = p
        work.append(cur)

def setwork_sort():
    global pend, work
    oldest = pend[0][1]
    pendset = set(x[1] for x in pend)
    sortq = []
    for i in (0,1):
        base = 1 if i else oldest
        q = sorted((dist[base][x],x) for x in pendset)
        sortq.append(q)
    vislist=[]
    while len(vislist) < MAXVISIT and (sortq[0] or sortq[1]):
        for j in (0,1):
            if not sortq[j]: continue
            _,x = sortq[j].pop()
            if x in vislist or x in work: continue
            vislist.append(x)
    prev=1
    while vislist:
        mni, mn = min(enumerate(vislist), key=lambda v: dist[prev][v[1]])
        mnx = vislist[mni]
        work.append(mnx)
        del vislist[mni]
        prev = mnx
    pend = [x for x in pend if x[1] not in work]

printer("start")

V,E = gm()
es = [[] for _ in range(V+1)]
dist = [[9999]*(V+1) for _ in range(V+1)]
for i in range(V+1): dist[i][i]=0
for _ in range(E):
    a,b,c = gm()
    es[a].append((b,c))
    es[b].append((a,c))
    dist[a][b]=dist[b][a]=c

if _dbg:
    [print(str(i),z) for i,z in enumerate(es)]

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
printer("WS done")

narray = [[0 for _ in range(V+1)] for _ in range(V+1)]
for i in range(1,V+1):
    for j in range(1,V+1):
        if i==j: continue
        for nk,c in es[i]:
            if dist[i][j]==c+dist[nk][j]:
                narray[i][j]=nk
                break
        else:
            print("nxtndary ERR")
            exit()

F = lint()
if len(F)==1:
    prob, tt = 1, F[0]
else:
    prob, tt = 2, gin()

pend = []
work = []
last_node = 1
dist_last = 0

for t in range(tt):
    if _dbg and t>3400: exit()
    n = gin()
    if n==1:
        i, d = gm()
        pend.append((i, d))
    if prob==2: readput()
    if depot_here():
        if trgr():
            setwork_wright()
            if work: moveon()
            else: nothin_do()
        else: nothin_do()
    else:
        moveon()
    if prob==2: readverd()