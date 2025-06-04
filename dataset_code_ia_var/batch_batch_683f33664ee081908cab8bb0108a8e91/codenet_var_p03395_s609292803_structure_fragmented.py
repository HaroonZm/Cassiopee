from heapq import heapify, heappush as hpush, heappop as hpop

def initialize_distances(n, i0):
    D = [-1] * n
    D[i0] = 0
    return D

def initialize_done(n):
    return [0] * n

def pop_from_heap(h):
    return hpop(h)

def push_to_heap(h, elem):
    hpush(h, elem)

def should_update(D, j, nd):
    return D[j] < 0 or D[j] >= nd

def update_distance(D, j, nd):
    D[j] = nd

def mark_done(done, i):
    done[i] = 1

def add_neighbors_to_heap(E, h, D, done, i, d):
    for j, w in E[i]:
        nd = d + w
        if should_update(D, j, nd) and done[j] == 0:
            push_to_heap(h, [nd, j])
            update_distance(D, j, nd)

def dijkstra_main_loop(n, E, i0, h, D, done):
    while h:
        d, i = pop_from_heap(h)
        mark_done(done, i)
        add_neighbors_to_heap(E, h, D, done, i, d)
    return D

def dijkstra(n, E, i0=0):
    h = [[0, i0]]
    D = initialize_distances(n, i0)
    done = initialize_done(n)
    return dijkstra_main_loop(n, E, i0, h, D, done)

def read_input():
    N = int(input())
    A = [int(a) for a in input().split()]
    B = [int(a) for a in input().split()]
    return N, A, B

def generate_base_edges(M):
    X = [[] for _ in range(M)]
    for i in range(1, M):
        for j in range(1, i+1):
            X[i].append([i % j, 2 ** j])
    return X

def create_X_from_S(S, M):
    X = [[] for _ in range(M)]
    for j in S:
        for i in range(j, M):
            X[i].append([i % j, 2 ** j])
    return X

def generate_all_distances(M, X):
    DI = []
    for i in range(M):
        DI.append(dijkstra(M, X, i))
    return DI

def all_pairs_ok(N, A, B, DI):
    for i in range(N):
        if DI[A[i]][B[i]] < 0:
            return False
    return True

def chk(S, N, A, B):
    M = 51
    X = create_X_from_S(S, M)
    DI = generate_all_distances(M, X)
    return 1 if all_pairs_ok(N, A, B, DI) else 0

def initialize_L1():
    return [i for i in range(1, 51)]

def empty_L2():
    return []

def base_case_failed(L1, N, A, B):
    return chk(L1, N, A, B) == 0

def sum_L2(L2):
    return sum([1 << l for l in L2])

def perform_while_L1(L1, L2, N, A, B):
    while L1:
        while True:
            if chk(L1 + L2, N, A, B):
                if len(L1) == 0:
                    break
                L1.pop()
            else:
                L2.append(L1[-1] + 1 if L1 else 1)
                L1 = [i for i in range(1, L2[-1])]
                break
        if len(L1) == 0:
            break
    return L2

def main():
    N, A, B = read_input()
    L1 = initialize_L1()
    L2 = empty_L2()
    if base_case_failed(L1, N, A, B):
        print(-1)
        return
    L2 = perform_while_L1(L1, L2, N, A, B)
    print(sum_L2(L2))

main()