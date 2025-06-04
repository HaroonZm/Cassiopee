import sys; from functools import reduce
sys.setrecursionlimit(10**6)
input_ = sys.stdin.readline

def KosarajuSCC(n, g, rg):
    used = [False]*n; order = []; groups = [None]*n
    class Context: pass
    ctx = Context()
    def dfs(a):
        used[a] = True
        [dfs(b) for b in g[a] if not used[b]]
        order.append(a)
    def rdfs(a, col):
        groups[a] = col
        used[a] = True
        for b in rg[a]:
            used[b] or rdfs(b, col)
    for x in range(n):
        if used[x]: continue
        dfs(x)
    [used.__setitem__(i,False) for i in range(n)]
    label = 0; reversed_order = order[::-1]
    for node in reversed_order:
        if not used[node]:
            rdfs(node, label)
            label +=1
    return (label, groups)

def mkcondensed(n, og, l, gr):
    G2 = [set() for _ in range(l)]; GP = [[] for _ in range(l)]
    for v in range(n):
        lbv = gr[v]
        [_ for w in og[v] if (gr[w]!=lbv and not G2[lbv].add(gr[w]))]
        GP[lbv].append(v)
    return (G2, GP)

n, m = (int(x) for x in input_().split())
H, Hr = [[] for _ in range(n)], [[] for _ in range(n)]
list(map(lambda _: (lambda s,d: (H[d-1].append(s-1), Hr[s-1].append(d-1)))(*map(int, input_().split())), range(m)))
cnt, grp = KosarajuSCC(n, H, Hr)
H2, components = mkcondensed(n, H, cnt, grp)

deg=[0]*cnt
[v for v in range(cnt) for w in H2[v] if not deg.__setitem__(w, deg[w]+1)]
M=10**9+7
f = lambda u: reduce(lambda acc, x: acc* f(x)%M, H2[u],1)+1
r=1
for i,d in enumerate(deg):
    if not d:
        r=r*f(i)%M
sys.stdout.write(f"{r}\n")