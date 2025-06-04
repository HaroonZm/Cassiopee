import sys

def read_input():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(read_input())

def read_int_list():
    return list(map(int, read_input().split()))

def adjust_colors(raw_colors):
    return [a - 1 for a in raw_colors]

def init_adjacency_list(size):
    return [[] for _ in range(size)]

def read_edges(N, X):
    for _ in range(N - 1):
        add_edge(X, read_edge())

def read_edge():
    x, y = map(int, read_input().split())
    return x - 1, y - 1

def add_edge(X, edge):
    x, y = edge
    X[x].append(y)
    X[y].append(x)

def make_function_f():
    return lambda k: k * (k + 1) // 2

def make_USED(n):
    return [0] * n

def make_ORG(n):
    return [0] * n

def make_TMP(n):
    return [0] * n

def make_P(n):
    return [-1] * n

def make_ET1(n):
    return [0] * n

def make_ET2(n):
    return [0] * n

def make_ANS(n, f):
    return [f(n)] * n

def make_Q(i0):
    return [~i0, i0]

def should_skip_parent(a, parent):
    return a != parent

def remove_back_edge(X, a, parent):
    for k in range(len(X[a])):
        if X[a][k] == parent:
            del X[a][k]
            break

def visit_first_time(i, ET1, ct, ORG, USED, C, P):
    if i:
        ORG[i] = USED[C[P[i]]]
    ct[0] += 1  # list allows pass by reference
    if ET1[i] == 0:
        ET1[i] = ct[0]

def visit_second_time(i, ET2, ct, USED, TMP, C, P, ORG, ANS, f):
    ET2[i] = ct[0]
    USED[C[i]] += 1 + TMP[i]
    if i:
        p = P[i]
        k = ET2[i] - ET1[i] + 1 - USED[C[p]] + ORG[i]
        ANS[C[p]] -= f(k)
        TMP[p] += k

def process_child(X, i, P, Q):
    for a in X[i][::-1]:
        if a != P[i]:
            P[a] = i
            remove_back_edge(X, a, i)
            Q.append(~a)
            Q.append(a)

def finalize_ANS(n, ANS, USED, f):
    for i in range(n):
        ANS[i] -= f(n - USED[i])

def EulerTour(n, X, i0):
    f = make_function_f()
    USED = make_USED(n)
    ORG = make_ORG(n)
    TMP = make_TMP(n)
    P = make_P(n)
    Q = make_Q(i0)
    ct = [-1] # to allow pass by reference
    ET1 = make_ET1(n)
    ET2 = make_ET2(n)
    ANS = make_ANS(n, f)
    while Q:
        i = Q.pop()
        if i < 0:
            visit_second_time(~i, ET2, ct, USED, TMP, C, P, ORG, ANS, f)
            continue
        if i >= 0:
            visit_first_time(i, ET1, ct, ORG, USED, C, P)
        process_child(X, i, P, Q)
    finalize_ANS(n, ANS, USED, f)
    return ANS

def main():
    N = read_int()
    C_raw = read_int_list()
    global C
    C = adjust_colors(C_raw)
    X = init_adjacency_list(N)
    read_edges(N, X)
    ans = EulerTour(N, X, 0)
    print_result(ans)

def print_result(ans):
    for v in ans:
        print(v)

main()