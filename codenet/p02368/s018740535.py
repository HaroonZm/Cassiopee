def input(f):
    global V, E, s, t, Q, u, v
    
    V, E = map(int, f.readline().split())
    s = [None for _ in range(E)]
    t = [None for _ in range(E)]
    for i in range(E):
        s[i], t[i] = map(int, f.readline().split())
        
    Q = int(f.readline())
    u = [None for _ in range(Q)]
    v = [None for _ in range(Q)]
    for i in range(Q):
        u[i], v[i] = map(int, f.readline().split())

import sys
sys.setrecursionlimit(1000000)

def solve():
    G = [[] for _ in range(V)]
    G_inv = [[] for _ in range(V)]
    for i in range(E):
        G[s[i]].append(t[i])
        G_inv[t[i]].append(s[i])

    def find_order():
        order = []
        used = [False for _ in range(V)]
        def rec(cur):
            if used[cur]:
                return
            used[cur] = True
            for nxt in G[cur]:
                rec(nxt)
            order.append(cur)
        
        for i in range(V):
            rec(i)
        
        return reversed(order)

    def decomp(order):
        groups = [None for _ in range(V)]
        used = [False for _ in range(V)]
        def rec(cur, group_id):
            if used[cur]:
                return
            used[cur] = True
            groups[cur] = group_id
            for nxt in G_inv[cur]:
                rec(nxt, group_id)
        
        group_id = 0
        for start in order:
            if used[start]:
                continue
            rec(start, group_id)
            group_id += 1
        
        return groups

    order = find_order()
    groups = decomp(order)

    for i in range(Q):
        if groups[u[i]] == groups[v[i]]:
            print('1')
        else:
            print('0')

with open('/dev/stdin') as f:
    input(f)
    solve()