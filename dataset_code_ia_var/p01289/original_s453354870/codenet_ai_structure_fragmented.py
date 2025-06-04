import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

def set_sys_params():
    sys.setrecursionlimit(10**7)

def get_inf():
    return 10**20

def get_eps():
    return 1.0 / 10**10

def get_mod():
    return 10**9 + 7

def get_mod2():
    return 998244353

def get_dd():
    return [(-1,0),(0,1),(1,0),(0,-1)]

def get_ddn():
    return [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI():
    return list(map(int, sys.stdin.readline().split()))

def LLI():
    return [list(map(int, l.split())) for l in sys.stdin.readlines()]

def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    return sys.stdin.readline().split()

def I():
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def S():
    return input()

def pf(s):
    return print(s, flush=True)

def pe(s):
    return print(str(s), file=sys.stderr)

def JA(a, sep):
    return sep.join(map(str, a))

def JAA(a, s, t):
    return s.join(t.join(map(str, b)) for b in a)

def copy_matrix(A):
    return [row[:] for row in A]

def augment_matrix(B, b):
    for i in range(len(B)):
        B[i].append(b[i])
    return B

def find_pivot(B, i):
    n = len(B)
    pivot = i
    abp = abs(B[i][i])
    for j in range(i+1, n):
        if abp < abs(B[j][i]):
            abp = abs(B[j][i])
            pivot = j
    return pivot, abp

def swap_rows(B, i, pivot):
    B[i], B[pivot] = B[pivot], B[i]

def is_almost_zero(value, eps):
    return value < eps

def normalize_row(B, i, n):
    for j in range(i+1, n+1):
        B[i][j] /= B[i][i]

def eliminate_other_rows(B, i, n):
    for j in range(n):
        if j == i:
            continue
        for k in range(i+1, n+1):
            B[j][k] -= B[j][i] * B[i][k]

def extract_solution(B):
    return list(map(lambda x: x[-1], B))

def gauss_jordan(A, b):
    n = len(A)
    B = copy_matrix(A)
    B = augment_matrix(B, b)
    eps = get_eps()

    for i in range(n):
        pivot, abp = find_pivot(B, i)
        swap_rows(B, i, pivot)
        if is_almost_zero(abp, eps):
            return
        normalize_row(B, i, n)
        eliminate_other_rows(B, i, n)

    return extract_solution(B)

def get_problem_inputs():
    n, s, t = LI()
    if n < 1:
        return None, None, None, None
    s -= 1
    t -= 1
    p = LI()
    aa = [LI() for _ in range(n)]
    return n, s, t, p, aa

def build_edges(n, aa):
    e = collections.defaultdict(list)
    for i in range(n):
        ai = aa[i]
        for j in range(n):
            if ai[j] == 0:
                continue
            e[i].append((j, ai[j]))
    return e

def init_d(n, inf, s):
    d = collections.defaultdict(lambda: inf)
    d[s] = 0
    return d

def init_queue(s):
    q = []
    heapq.heappush(q, (0, s))
    return q

def init_visited():
    return collections.defaultdict(bool)

def process_neighbors(e, u, k, d, v, q):
    for uv, ud in e[u]:
        if v[uv]:
            continue
        vd = k + ud
        if d[uv] > vd:
            d[uv] = vd
            heapq.heappush(q, (vd, uv))

def dijkstra_search(e, s, n):
    inf = get_inf()
    d = init_d(n, inf, s)
    q = init_queue(s)
    v = init_visited()
    while len(q):
        k, u = heapq.heappop(q)
        if v[u]:
            continue
        v[u] = True
        process_neighbors(e, u, k, d, v, q)
    return d

def impossible_if_infinite(d, s):
    inf = get_inf()
    if d[s] == inf:
        return True
    return False

def build_matrix_A_and_vec_b(n, t, d, aa, p):
    A = [[0]*n for _ in range(n)]
    b = [0] * n
    for i in range(n):
        if i == t or d[i] == get_inf():
            A[i][i] = 1
            b[i] = 0
            continue
        mv, mk = get_matrix_counts(i, d, aa, p)
        set_row_A(A, i, n, aa[i], d, p, mv)
        A[i][i] = mv
        b[i] = mk
    return A, b

def get_matrix_counts(i, d, aa, p):
    mv = 0
    mk = 0
    di = d[i]
    ai = aa[i]
    n = len(ai)
    for j in range(n):
        if ai[j] < 1 or (p[i] == 1 and d[j] + ai[j] != di):
            continue
        mv += 1
        mk += ai[j]
    return mv, mk

def set_row_A(A, i, n, ai, d, p, mv):
    for j in range(n):
        if ai[j] < 1 or (p[i] == 1 and d[j] + ai[j] != d[i]):
            continue
        A[i][j] = -1

def format_result(r, s):
    return "{:0.9f}".format(r[s])

def f():
    n, s, t, p, aa = get_problem_inputs()
    if n is None:
        return None
    e = build_edges(n, aa)
    d = dijkstra_search(e, t, n)
    if impossible_if_infinite(d, s):
        return "impossible"
    A, b = build_matrix_A_and_vec_b(n, t, d, aa, p)
    r = gauss_jordan(A, b)
    if r is None:
        return "impossible"
    return format_result(r, s)

def main_loop():
    rr = []
    while True:
        r = f()
        if r is None:
            break
        rr.append(r)
    return JA(rr, "\n")

def main():
    set_sys_params()
    return main_loop()

print(main())