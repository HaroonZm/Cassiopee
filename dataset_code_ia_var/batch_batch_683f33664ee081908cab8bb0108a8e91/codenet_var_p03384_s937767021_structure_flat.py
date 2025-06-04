import sys
readline = sys.stdin.readline

N = int(readline())
Edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)

dist = [0]*N
stack = [0]
used = [False]*N
used[0] = True
while stack:
    vn = stack.pop()
    for vf in Edge[vn]:
        if not used[vf]:
            used[vf] = True
            dist[vf] = 1 + dist[vn]
            stack.append(vf)
dist0 = dist[:]

fs = 0
mval = -1
for i in range(N):
    if dist0[i]>mval:
        mval = dist0[i]
        fs = i

dist = [0]*N
stack = [fs]
used = [False]*N
used[fs] = True
while stack:
    vn = stack.pop()
    for vf in Edge[vn]:
        if not used[vf]:
            used[vf] = True
            dist[vf] = 1 + dist[vn]
            stack.append(vf)
distfs = dist[:]

en = 0
mval = -1
for i in range(N):
    if distfs[i]>mval:
        mval = distfs[i]
        en = i

dist = [0]*N
stack = [en]
used = [False]*N
used[en] = True
while stack:
    vn = stack.pop()
    for vf in Edge[vn]:
        if not used[vf]:
            used[vf] = True
            dist[vf] = 1 + dist[vn]
            stack.append(vf)
disten = dist[:]

Dia = distfs[en]
path = []
for i in range(N):
    if distfs[i] + disten[i] == Dia:
        path.append(i)

dist = [0]*N
stack = path[:]
used = [False]*N
for s in path:
    used[s] = True
while stack:
    vn = stack.pop()
    for vf in Edge[vn]:
        if not used[vf]:
            used[vf] = True
            dist[vf] = 1 + dist[vn]
            stack.append(vf)
if max(dist) > 1:
    print(-1)
else:
    path.sort(key = lambda x: distfs[x])
    cnt = 1
    hold = 0
    perm1 = [None]*N
    onpath = set(path)
    idx = 0
    for i in range(Dia+1):
        vn = path[i]
        hold = 0
        for vf in Edge[vn]:
            if vf in onpath:
                continue
            hold += 1
            perm1[idx] = cnt + hold
            idx += 1
        perm1[idx] = cnt
        idx += 1
        cnt = cnt+hold+1

    cnt = 1
    hold = 0
    perm2 = [None]*N
    onpath = set(path)
    idx = 0
    for i in range(Dia+1):
        vn = path[Dia-i]
        hold = 0
        for vf in Edge[vn]:
            if vf in onpath:
                continue
            hold += 1
            perm2[idx] = cnt + hold
            idx += 1
        perm2[idx] = cnt
        idx += 1
        cnt = cnt+hold+1
    ans = []
    for a,b in zip(perm1,perm2):
        if a is None:
            ans.append(b)
        elif b is None:
            ans.append(a)
        else:
            ans.append(min(a,b))
    print(*ans)