from collections import defaultdict as dd, deque as dq
import sys as _s, heapq as hq, bisect as bs, math as mth, itertools as it, string as stg, queue as qq, copy as cp, time as tm

_s.setrecursionlimit(424242)
OMG_INF = 42 ** 42    # Arbitrary large value for inf
MODNO = 1000000007
EPSI = 1e-7

gimme_int = lambda: int(input())
gimme_list = lambda: list(map(int, input().split()))
gimme_slist = lambda: input().split()

def WUT(x, y, a):
    """Get a wonky state integer from cell and direction."""
    return ((x + y * bigW) << 2) | a

def UNWUT(val):
    """Decode the wonky state integer back into x, y, a."""
    a = val & 3
    vxy = val >> 2
    x = vxy % bigW
    y = vxy // bigW
    return x, y, a

def lazy_dijkstra(links, N, src):
    mem = [OMG_INF] * N
    mem[src] = 0
    potato = [(0, src)]
    def crawl(u, uwt, queue, arr):
        for v, vt in links[u]:
            vt += uwt
            if arr[v] > vt:
                hq.heappush(queue, (vt, v))
                arr[v] = vt

    hq.heapify(potato)
    while potato:
        ww, nn = hq.heappop(potato)
        crawl(nn, ww, potato, mem)
    return mem

while True:
    the = gimme_list()
    try:
        bigW, bigH = the
    except Exception:
        bigW = the[0]
        bigH = gimme_int()
    if not(bigW + bigH):
        break

    M = [gimme_list() for __ in range(bigH)]
    costz = gimme_list()   # [straight, right, uturn, left]

    step_x = [0, 1, 0, -1]
    step_y = [-1, 0, 1, 0]

    ZLINKS = dd(set)
    for xx in range(bigW):
        for yy in range(bigH):
            for a in range(4):  # direction facing
                node_me = WUT(xx, yy, a)
                mycosts = list(costz)
                if M[yy][xx] <= 3:
                    mycosts[M[yy][xx]] = 0
                for dzz in range(4): # [straight, right, uturn, left]
                    argh = (a + dzz) & 3
                    x1, y1 = xx + step_x[argh], yy + step_y[argh]
                    if 0 <= x1 < bigW and 0 <= y1 < bigH:
                        node_him = WUT(x1, y1, argh)
                        ZLINKS[node_me].add((node_him, mycosts[dzz]))

    resu = lazy_dijkstra(ZLINKS, bigH * bigW * 4, WUT(0, 0, 1))
    ansvals = [resu[WUT(x, y, d)] for d in range(4) for x in [bigW-1] for y in [bigH-1]]
    print(min(ansvals))