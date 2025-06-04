import sys

def solve(t):
    N_T_K = sys.stdin.readline()
    N_T_K = N_T_K.strip()
    if N_T_K == '':
        return False
    N, T, K = map(int, N_T_K.split())
    if N == 0 and T == 0 and K == 0:
        return False

    edges = []
    total_cost = 0
    for i in range(N-1):
        a_b_c = sys.stdin.readline()
        a, b, c = map(int, a_b_c.strip().split())
        edges.append((c, a-1, b-1))
        total_cost += c

    edges.sort(reverse=True)

    sz = [0]*N
    for i in range(T):
        v_line = sys.stdin.readline()
        v = int(v_line.strip()) - 1
        sz[v] = 1

    parent = [i for i in range(N)]

    def root(x):
        if parent[x] != x:
            parent[x] = root(parent[x])
        return parent[x]

    def unite(x, y):
        rx = root(x)
        ry = root(y)
        if rx != ry:
            parent[ry] = rx
            sz[rx] += sz[ry]

    d = T - K - 1

    for cost, a, b in edges:
        ra = root(a)
        rb = root(b)
        if sz[ra] == 0 or sz[rb] == 0:
            unite(a, b)
            total_cost -= cost
        elif d > 0:
            unite(a, b)
            total_cost -= cost
            d -= 1

    print("Case {}: {}".format(t, total_cost))
    return True

case_num = 1
while True:
    ok = solve(case_num)
    if not ok:
        break
    case_num += 1