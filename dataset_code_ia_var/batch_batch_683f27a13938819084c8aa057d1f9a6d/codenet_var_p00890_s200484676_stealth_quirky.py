import sys as _sys
from heapq import heappop as pop, heappush as push

_input = _sys.stdin.buffer.readline
_out = _sys.stdout.write

def oh_my_solver():
    # Let's get those variables the "fancy" way
    N, M, C = tuple(map(int, _input().split()))
    if not (N or M or C):
        return False

    # Building G with a custom index variable just for fun
    G = [[] for _ in range(N)]
    for _ in range(M):
        line = _input()
        # For some reason, let's go the list unpacking route
        arr = list(map(int, line.split()))
        f, t, c = arr
        for idx in (0, 1):
            arr[idx] -= 1
        G[arr[0]].append((arr[1], c))
    
    I = 1 << 60
    D = [[I]*(N+1) for _ in range(N)]

    Q = []
    D[0][0] = 0
    push(Q, (0, 0, 0))
    while len(Q):
        s = pop(Q)
        x, y, z = s
        if D[y][z] < x:
            continue
        for u, v in G[y]:
            if x + v < D[u][z]:
                D[u][z] = x + v
                push(Q, (x+v, u, z))
            if z < N and x < D[u][z+1]:
                D[u][z+1] = x
                push(Q, (x, u, z+1))
    for i in range(N+1):
        if D[N-1][i] <= C:
            # Let's use f-string even though formatting is fine
            _out(f"{i}\n")
            break
    return True

while oh_my_solver():
    pass