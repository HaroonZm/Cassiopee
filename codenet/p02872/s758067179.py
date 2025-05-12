import sys
printn = lambda x: sys.stdout.write(x)
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
DBG = True  and False
#PROBL = 1
MAXVISIT = 400

def ddprint(x):
  if DBG:
    print(x)
    sys.stdout.flush()

def trigger():
    return (len(pendreq) > 0)

def nxtnode():
    global lastnd, workreq, nxtndary
    tgt = workreq[0] if len(workreq)>0 else 1
    #ddprint("in nxtnode lastnd {} wr0 {} tgt {} ret {}".format(\
    # lastnd, workreq[0] if len(workreq)>0 else -1, tgt, nxtndary[lastnd][tgt]))
    return nxtndary[lastnd][tgt]

def atdepot():
    return (lastnd==1 and distfromlast==0)

def stay():
    #print(-1, flush=True)
    print(-1)
    sys.stdout.flush()

def readput():
    n = inn()
    for i in range(n):
        inn()

def readverd():
    v = input().strip()
    if v != 'OK':
        exit()
    readput()

def move():
    global distfromlast, lastnd, workreq
    nxtnd = nxtnode()
    #print(nxtnd, flush=True)
    print(nxtnd)
    sys.stdout.flush()
    distfromlast += 1
    if distfromlast == dist[lastnd][nxtnd]:
        distfromlast = 0
        if len(workreq)>0 and nxtnd == workreq[0]:
            del workreq[0]
        lastnd = nxtnd

def ufinit(n):
    global ufary, ufrank
    ufary = [i for i in range(n)]
    ufrank = [0] * n

def ufroot(i):
    p = ufary[i]
    if p==i:
        return p
    q = ufroot(p)
    ufary[i] = q
    return q

def ufmerge(i,j):
    global ufary, ufrank
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

def setwork():
    global pendreq, workreq
    vislist = set([x[1] for x in pendreq]) | set(workreq)
    vv = len(vislist)
    pendreq = []
    if vv==1:
        workreq = list(vislist)
        return
    # Clark & Wright
    e = {}
    f = {}
    for x in vislist:
        e[x] = []
    ufinit(V+1)
    #ddprint("e pre")
    #ddprint(e)
    for _ in range(vv-1):
        mx = -1
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
    # now len(e) is 2.  find the first
    #ddprint("e {}".format(e))
    #ddprint("f {}".format(f))
    ek = list(e.keys())
    p = ek[0]
    #q = ek[1]
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
    #workreq.append(q)
    #ddprint("w {}".format(workreq))

def setwork1():
    global pendreq, workreq
    # sort pend reqs by distance from depot/oldest
    oldest = pendreq[0][1]
    pendset = set([x[1] for x in pendreq])
    sortq = []
    for i in [0,1]:
        q = []
        base = 1 if i==1 else oldest # 0:oldest 1:depot
        for x in pendset:
            q.append((dist[base][x], x))
        q.sort(reverse=True) # shortest at tail
        sortq.append(q)

    # create visit node list - closest to depot/oldest
    vislist = []
    while len(vislist) < MAXVISIT and \
           (len(sortq[0])>0 or len(sortq[1])>0):
        for j in [0,1]:
            if len(sortq[j])==0:
                continue
            d,x = sortq[j].pop()
            if x in vislist or x in workreq:
                continue
            vislist.append(x)
    #ddprint("vislist")
    #ddprint(vislist)

    # create route
    prev = 1
    while len(vislist)>0:
        mn = 9999
        for i,x in enumerate(vislist):
            d = dist[prev][x]
            if d<mn:
                mn = d
                mni = i
        mnx = vislist[mni]
        workreq.append(mnx)
        del vislist[mni]
        prev = mnx

    # update pendreq
    pendreq = [x for x in pendreq if x[1] not in workreq]

# # # # main start # # # #
ddprint("start")
#prob = PROBL # int(sys.argv[1])

V, E = inm()
es = [[] for i in range(V+1)]
dist = [[9999]*(V+1) for i in range(V+1)]

for i in range(V+1):
    dist[i][i] = 0

for i in range(E):
    a, b, c = inm()
    #a, b = a-1, b-1
    es[a].append((b,c))
    es[b].append((a,c))
    dist[a][b] = dist[b][a] = c

if DBG:
    for i,z in enumerate(es):
        print(str(i)+' ' + str(z))

# Warshal-Floyd
for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            dist[i][j] = min(dist[i][j], \
                           dist[i][k]+dist[k][j])
ddprint("WS done")

nxtndary = [[0]*(V+1) for i in range(V+1)]
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

#if prob==2:
#    F = inl()
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
for t in range(tt):
    #ddprint("t {} lastnd {} dist {}".format( \
    #        t,lastnd,distfromlast))
    #ddprint(pendreq)
    #ddprint(workreq)
    if DBG and t>3400:
        exit()

    # read a new req if any
    n = inn()
    if n==1:
        new_id, dst = inm()
        #ddprint("new req id {} dst {}".format(new_id, dst))
        pendreq.append((new_id, dst))
    if prob==2:
        readput()
    # determine action
    if atdepot():
        if trigger():
            setwork()
            if len(workreq)>0:
                move()
            else:
                stay()
        else:
            stay()
    else:
        move()
    if prob==2:
        readverd()