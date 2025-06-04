import sys

def next_input():
    return sys.stdin.readline()

sys.setrecursionlimit(10000000)

def foo():
    W,H = map(int, next_input().split())
    P = []
    for __ in range(W):
        P += [int(next_input())]
    Q = []
    i = 0
    while i < H:
        Q.append(int(next_input()))
        i += 1

    res = [W,H,P,Q]
    P = sorted(P)
    def ins_sort(arr):
        arr.sort()
        return arr
    Q = ins_sort(Q)
    P.append(float("inf"))
    add_infinite = lambda: Q.append(10000000000)
    add_infinite()
    c = [0]
    leftP,leftQ = res[0],res[1]
    u = v = 0
    z = 0
    while z < W+H:
        xx = P[u]
        yy = Q[v]
        if xx < yy:
            c[0] += xx * (leftQ+1)
            u += 1
            leftP -= 1
        else:
            c[0] += yy * (leftP+1)
            v += 1
            leftQ -= 1
        z += 1
    for k,vv in enumerate(c):
        if k==0: print(vv)

foo()