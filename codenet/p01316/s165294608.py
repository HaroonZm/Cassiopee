import sys
from itertools import product
input = sys.stdin.readline

def inpl():
    return list(map(int, input().split()))

def solve(N, M):
    C = [int(input()) for _ in range(M)]
    X = [int(input()) for _ in range(N)]

    ret = [float('inf')] * 256
    ret[128] = 0
    cor = set((max(min(i + c, 255), 0), i) for c, i in product(C, list(range(256))))
    xt = tuple(tuple((x - t)**2 for x in range(256)) for t in range(256))
    for x in X:
        tmp = [float('inf')] * 256
        xt_now = xt[x]
        for t, i in cor:
            v = ret[i]
            if v + xt_now[t] < tmp[t]:
                tmp[t] = v + xt_now[t]
        ret = tmp[:]

    return min(ret)

def main():
    ans = []
    while True:
        N, M = inpl()
        if N == M == 0:
            break
        ans.append(solve(N, M))
    for a in ans:
        print(a)
    return

main()