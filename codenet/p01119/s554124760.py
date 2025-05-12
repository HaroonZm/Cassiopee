from collections import defaultdict
def solve(N, M, A, W):
    S = set([0])
    for w in W:
        T = set()
        for s in S:
            T.add(s); T.add(s + w); T.add(s - w)
        S = T
    C = defaultdict(int)
    L = None
    for a in A:
        if a not in S:
            if L is None:
                L = [abs(s - a) for s in S]
            else:
                L = [l for l in L if a+l in S or a-l in S]
    if L is None:
        print(0)
    elif L:
        print(min(L))
    else:
        print(-1)

while 1:
    N, M = map(int, input().split())
    if N == 0:
        break
    *A, = map(int, input().split())
    *W, = map(int, input().split())
    solve(N, M, A, W)