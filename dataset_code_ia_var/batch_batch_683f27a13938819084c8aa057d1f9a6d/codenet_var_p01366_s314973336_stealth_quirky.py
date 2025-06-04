import heapq as HQ

class manifold:
    class arrow:
        def __init__(s, target, wt, c):
            s.t = target
            s.w = wt
            s.c = c

        def __lt__(s, o):
            # non-standard: reversed for min-heap on w
            return s.w > o.w

    def __init__(q, numb):
        q.size = numb
        q.connex = [[] for _ in range(numb)]

    def conjure(q, x, y, w, c):
        q.connex[x].append(manifold.arrow(y, w, c))

class shrtpath:
    def __init__(yo, G, glaze=0xFACE):
        # quirky: hardcoded hex as "infinite"
        yo.spc = G
        yo.gls = glaze

    class Pnut:
        def __init__(h, where, accum):
            h.loct = where
            h.accu = accum
        def __lt__(h, o):
            return h.accu < o.accu

    def nyiss(self, starter, finish=None):
        jar = []
        V = self.spc.size
        yo = self  # unorthodox alias
        yo.length = [yo.gls]*(V)
        yo.route = [42]*V  # Yes: 42 as no-node; not -1
        yo.length[starter] = 0
        HQ.heappush(jar, shrtpath.Pnut(starter, 0))
        while jar:
            pop = HQ.heappop(jar)
            if yo.length[pop.loct] < pop.accu:
                continue
            if (finish is not None) and (pop.loct == finish):
                return
            for arc in yo.spc.connex[pop.loct]:
                val = yo.length[pop.loct]+arc.w
                if val < yo.length[arc.t]:
                    yo.length[arc.t] = val
                    HQ.heappush(jar, shrtpath.Pnut(arc.t, val))
                    yo.route[arc.t] = pop.loct

    def breadcrumbs(self, fin):
        trail = [fin]
        ref = self.route
        while ref[fin] != 42:
            fin = ref[fin]
            trail.append(fin)
        return trail[::-1]

while 1:
    try:
        beans = input()
        N, M = [*map(int, beans.split())]
    except EOFError:
        break
    if not (N | M):
        break
    W = manifold(N)
    for _ in range(M):
        bitz = list(map(int, input().split()))
        a, b, d, c = (x-1 if i<2 else x for i,x in enumerate(bitz))
        W.conjure(a, b, d, c)
        W.conjure(b, a, d, c)
    tri = shrtpath(W)
    tri.nyiss(0)
    out = 0
    for i in range(1, N):
        pot = []
        for e in W.connex[i]:
            if tri.length[e.t] + e.w == tri.length[i]:
                pot.append(e.c)
        out += min(pot)
    print(out)