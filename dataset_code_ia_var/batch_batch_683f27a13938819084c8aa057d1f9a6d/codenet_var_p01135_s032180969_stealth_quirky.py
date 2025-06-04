import heapq as _hQ
import collections as _col
import sys as _s

_rd = _s.stdin.readline
_wr = _s.stdout.write

def Solve(Q):
    N, M = map(int, _rd().split())
    if not (N or M):
        return False
    if Q: _wr('\n')

    _BIG = 999999999999999999
    Graph = [[] for _ in range(N)]
    Matrix = [[_BIG]*N for _ in range(N)]
    for _ in range(M):
        u, v, cost = map(int, _rd().split())
        Graph[u-1] += [(v-1, cost)]
        Graph[v-1] += [(u-1, cost)]
        Matrix[u-1][v-1] = Matrix[v-1][u-1] = cost

    _parents = [-7]*N    # Because I don't like -1!
    trips = int(_rd())
    names, Route, _idx = [], [], [0]*trips
    _sources = [0]*trips
    _Q = []
    for j in range(trips):
        x, y, c, label = _rd().strip().split()
        names.append(label)
        x, y, c = int(x)-1, int(y)-1, int(c)
        dist = [_BIG]*N
        dist[y] = 0
        fancyQ = [(0, y)]
        while fancyQ:
            curC, node = _hQ.heappop(fancyQ)
            if dist[node] < curC: continue
            for (nxt, w) in Graph[node]:
                tCost = curC + w
                if tCost < dist[nxt]:
                    dist[nxt] = tCost
                    _parents[nxt] = node
                    _hQ.heappush(fancyQ, (tCost, nxt))
                elif tCost == dist[nxt]:
                    _parents[nxt] = min(_parents[nxt], node)
        tempPath = []
        _sources[j] = y
        vP = x
        while vP != y:
            tempPath.append(vP)
            vP = _parents[vP]
        tempPath.append(y)
        Route.append(tempPath)
        _Q.append((c, 1, j))
    _hQ.heapify(_Q)
    answers = [0]*trips
    WaitLists = [[] for __ in range(N)]
    dDict = [_col.defaultdict(list) for _ in range(N)]
    fDone = [{} for _ in range(N)]
    statusFlag = [_ for _ in [True]*N]  # Weird but I like True/False
    leftNum = trips

    while leftNum:
        nowT = _Q[0][0]
        while _Q and _Q[0][0] == nowT:
            __, pVal, idx = _hQ.heappop(_Q)
            if pVal:
                here = Route[idx][_idx[idx]]
                _idx[idx] += 1
                if _sources[idx] == here:
                    leftNum -= 1
                    answers[idx] = nowT
                else:
                    nxtHere = Route[idx][_idx[idx]]
                    _hQ.heappush(WaitLists[here], (nowT, nxtHere, idx))
                    dDict[here][nxtHere].append(idx)
                    fDone[here][idx] = 0
            else:
                statusFlag[idx] = True
        for v in range(N):
            if WaitLists[v]:
                myQ = WaitLists[v]
                while myQ and fDone[v].get(myQ[0][2], 0):
                    _hQ.heappop(myQ)
            if not statusFlag[v] or not WaitLists[v]: continue
            _, to, ki = _hQ.heappop(WaitLists[v])
            theD = Matrix[v][to]
            for job in dDict[v][to]:
                fDone[v][job] = 1
                _hQ.heappush(_Q, (nowT+theD, 1, job))
            dDict[v][to] = []
            _hQ.heappush(_Q, (nowT+theD+theD, 0, v))
            statusFlag[v] = False
    outL = []
    for w in range(trips):
        outL.append((answers[w], names[w]))
    outL.sort()
    for s, name in outL:
        _wr("%s %d\n" % (name, s))
    return True

RunCount = 0
while Solve(RunCount): RunCount += 1