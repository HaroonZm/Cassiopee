from collections import deque

def read_n_k_s():
    n, k, s = map(int, raw_input().split())
    return n, k, s

def read_points(n):
    return [map(int, raw_input().split()) for _ in xrange(n)]

def build_graph(n, s, ps):
    G = [[] for _ in xrange(n)]
    for i in xrange(n):
        xi, yi, zi = ps[i]
        for j in xrange(i + 1, n):
            xj, yj, zj = ps[j]
            dx = abs(xi - xj)
            dy = abs(yi - yj)
            dz = abs(zi - zj)
            if dx < s and dy < s and dz < s:
                cost = calculate_cost(s, dx, dy, dz)
                add_edge(G, i, j, cost)
    return G

def calculate_cost(s, dx, dy, dz):
    return 2 * ((s - dx) * (s - dy) + (s - dy) * (s - dz) + (s - dz) * (s - dx))

def add_edge(G, i, j, cost):
    G[i].append((j, cost))
    G[j].append((i, cost))

def is_single_k(k):
    return k == 1

def print_single_k(s):
    print 6 * s * s

def initialize_used(n):
    return [0] * n

def find_leaves_and_update_used(G, used):
    leaf = set()
    for i in xrange(len(G)):
        if len(G[i]) == 0:
            used[i] = 1
        elif len(G[i]) == 1:
            leaf.add(i)
    return leaf

def process_leaf_paths(leaf, G, used, k, n):
    ans = -1
    for v in leaf:
        if used[v]:
            continue
        used[v] = 1
        ans = process_single_leaf(v, G, used, k, ans)
    return ans

def process_single_leaf(v, G, used, k, ans):
    prev = t = None
    deq = deque()
    su = 0
    while True:
        if prev is not None and len(G[v]) == 1:
            break
        updated = False
        for t1, cost in G[v]:
            if t1 == prev:
                continue
            used[t1] = 1
            if len(deq) < k - 1:
                deq.append(cost)
                su += cost
            else:
                su -= deq.popleft()
                deq.append(cost)
                su += cost
            t = t1
            updated = True
            break
        if not updated:
            break
        if len(deq) == k - 1:
            ans = max(ans, su)
        v, prev = t, v
    return ans

def process_cycles(G, used, k, n, current_ans):
    ans = current_ans
    for v in xrange(n):
        if used[v]:
            continue
        ans = process_single_cycle(v, G, used, k, ans)
    return ans

def process_single_cycle(v, G, used, k, ans):
    prev = t = None
    used[v] = 1
    u = set([v])
    v0 = v
    while v is not None and used[v] < 3:
        updated = False
        for t1, cost in G[v]:
            if t1 == prev:
                continue
            used[t1] += 1
            u.add(t1)
            t = t1
            updated = True
            break
        if not updated:
            break
        v, prev = t, v
    cont = k if len(u) == k else k - 1
    prev = t = None
    deq = deque()
    su = 0
    v = v0
    for i in xrange(2 * len(u)):
        updated = False
        for t1, cost in G[v]:
            if t1 == prev:
                continue
            if len(deq) < cont:
                deq.append(cost)
                su += cost
            else:
                su -= deq.popleft()
                su += cost
                deq.append(cost)
            t = t1
            updated = True
            break
        if not updated:
            break
        if len(deq) == cont:
            ans = max(ans, su)
        v, prev = t, v
    return ans

def print_result(ans, k, s):
    if ans == -1:
        print -1
    else:
        print 6 * k * s * s - ans

def main_loop():
    while True:
        n, k, s = read_n_k_s()
        if n == 0:
            break
        ps = read_points(n)
        G = build_graph(n, s, ps)
        if is_single_k(k):
            print_single_k(s)
            continue
        ans = -1
        used = initialize_used(n)
        leaf = find_leaves_and_update_used(G, used)
        ans = process_leaf_paths(leaf, G, used, k, n)
        ans = process_cycles(G, used, k, n, ans)
        print_result(ans, k, s)

main_loop()