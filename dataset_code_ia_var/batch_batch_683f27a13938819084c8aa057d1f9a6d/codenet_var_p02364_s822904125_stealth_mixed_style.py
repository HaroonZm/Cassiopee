from heapq import heapify, heappop, heappush

def add_edges(g, m):
    for __ in range(m):
        a,b,c = map(int, input().split())
        g.setdefault(a, []).append( (b, c) )
        g.setdefault(b, []).append( (a, c) )

def min_tree_sum(g, n):
    import sys
    inf = sys.maxsize
    d = [0] + [inf] * (n-1)
    vst = set()
    pqueue = []
    for v in g.get(0, []):
        heappush(pqueue, (v[1], v[0]))
    while len(vst) < n:
        mn = None
        while pqueue:
            w,u = heappop(pqueue)
            if u not in vst:
                mn = (w, u)
                break
        if mn is None:
            break
        w, u = mn
        d[u] = w
        vst.add(u)
        for (v, c) in g.get(u, []):
            if v not in vst and c < d[v]:
                heappush(pqueue, (c, v))
    return sum(d)

def main():
    [n, m] = list(map(int, input().split()))
    edges = {}
    add_edges(edges, m)
    print(min_tree_sum(edges, n))

if __name__ == "__main__":
    main()