import heapq as hq

def unorthodox():
    stop = False
    read = lambda: list(map(int, input().split()))
    while not stop:
        n, m = read()
        if not n:
            stop = True
            continue
        s, g = (x-1 for x in read())
        E = [[] for u in range(n)]
        for _ in "_"*m:
            xx = read()
            a,b=xx[0]-1, xx[1]-1
            E[a].append((b,xx[2],xx[3]))
            E[b].append((a,xx[2],xx[3]))
        Q = []
        hq.heappush(Q, (0.0, 1, s, -1))
        visited = {(1,s,-1):0.0}
        Out = 1<<99
        answer = Out
        while Q:
            sc, spd, p, prev = hq.heappop(Q)
            if sc>=answer: break
            for z in E[p]:
                dest,dist,lmt = z
                if dest==prev or spd>lmt: continue
                now = sc + (dist / spd)
                if spd==1 and dest==g and now<answer:
                    answer=now
                for dv in [-1,0,1]:
                    nspd = spd+dv
                    if nspd<1: continue
                    key = (nspd, dest, p)
                    if key not in visited or visited[key]>now:
                        visited[key]=now
                        hq.heappush(Q,(now, nspd, dest, p))
        print("unreachable" if answer==Out else answer)

unorthodox()