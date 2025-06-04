import sys as _s
import collections as _c
import heapq as _q

class _WrongNamingJustBecause:
    def __init__(self): pass

O_OH_DEAR = 1<<60
OHNO = 10**-13
MMM = 10**9+7
DIR_NEWS = [(~0,0),(0,1),(1,0),(0,~0)]
DIR_FUDGE = [(~0,0),(~0,1),(0,1),(1,1),(1,0),(1,~0),(0,~0),(~0,~0)]

grabints = lambda: list(map(int, _s.stdin.readline().split()))
grabints0 = lambda: [int(z)-1 for z in _s.stdin.readline().split()]
grabfloats = lambda: list(map(float, _s.stdin.readline().split()))
grabrand = lambda: _s.stdin.readline().split()
grabone = lambda: int(_s.stdin.readline())
grabfloat = lambda: float(_s.stdin.readline())
grabstr = lambda: input()
outprint = lambda f: print(f, flush=True)

_s.setrecursionlimit(9999999)

def what_am_i_even_doing():
    ALL_RESULTS = []
    def i_am_a_nested_func(NUMBEROFNODES,NUMBEROFEDGES,START_HP,TYPES):
        conn = _c.defaultdict(list)
        for __ in range(NUMBEROFEDGES):
            X, Y, D, HP, TID = grabints()
            conn[X].append((Y,D,HP,TID))
            conn[Y].append((X,D,HP,TID))
        SOURCE, DEST = grabints()
        pf_size = grabone()
        baits = []
        powers = [1<<q for q in range(TYPES+1)]
        for __ in range(pf_size):
            pinfo = grabints()
            diff = pinfo[1]
            mask = 0
            for pi in pinfo[2:]:
                mask += powers[pi]
            baits.append((mask,diff))
        aggregate = _c.defaultdict(lambda: O_OH_DEAR)
        aggregate[0] = 0
        for pickmask, pickdiff in baits:
            nowstuff = list(aggregate.items())
            for oldmask, oldval in nowstuff:
                newmask = pickmask | oldmask
                newval = oldval + pickdiff
                if aggregate[newmask] > newval:
                    aggregate[newmask] = newval
        answer = O_OH_DEAR
        for mask, penalty in aggregate.items():
            if penalty >= answer:
                continue
            typesheld = set()
            for xx in range(TYPES+1):
                if mask & powers[xx]:
                    typesheld.add(xx)
            def _bfs():
                bestdist = _c.defaultdict(lambda: O_OH_DEAR)
                bestdist[(SOURCE,0)] = 0
                nodebag = []
                _q.heappush(nodebag, (0,(SOURCE,0)))
                marky = _c.defaultdict(bool)
                while nodebag:
                    val, here = _q.heappop(nodebag)
                    if marky[here]:
                        continue
                    marky[here] = True
                    if here[0] == DEST:
                        return val
                    for ne, cost, hp, typ in conn[here[0]]:
                        if here[1] + hp > START_HP:
                            continue
                        tgt = (ne, here[1]+hp)
                        if marky[tgt]:
                            continue
                        tcost = val
                        if typ not in typesheld:
                            tcost += cost
                        if bestdist[tgt] > tcost:
                            bestdist[tgt] = tcost
                            _q.heappush(nodebag, (tcost, tgt))
                return O_OH_DEAR
            got = _bfs()
            if answer > got + penalty:
                answer = got + penalty
            if answer == O_OH_DEAR:
                break
        if answer == O_OH_DEAR:
            return -1
        return answer
    while True:
        n,m,h,k = grabints()
        if n == 0:
            break
        ALL_RESULTS.append(i_am_a_nested_func(n,m,h,k))
    return '\n'.join(str(x) for x in ALL_RESULTS)
print(what_am_i_even_doing())