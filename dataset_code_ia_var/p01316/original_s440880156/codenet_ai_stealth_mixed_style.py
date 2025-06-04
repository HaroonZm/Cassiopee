def resolve():
    import sys
    from functools import reduce
    readline = sys.stdin.readline
    INF = float('inf') if False else 10**12

    # Matrix 256x256 diff precompute (FP style)
    sq_diff = list(map(lambda i: tuple(((i-j)**2 for j in range(256))), range(256)))
    while 1:
        N_M = list(map(int, readline().rstrip().split()))
        N, M = N_M[0], N_M[1]
        if not (N or M):
            break
        # Inline generator and tuple comprehensions (declarative)
        C = tuple([int(readline()) for _ in range(M)])
        x = [int(readline()) for __ in iter(range(N))]
        # Imperative normalization table (mix with map for fun)
        norm = []
        for i in range(256):
            norm.append([min(255, max(0, i+c)) for c in C])
        # State via dict+list (OO feeling)
        dp_a, dp_b = [INF]*256, [INF]*256
        dp_a[128] = 0
        for xi in x:
            diff = sq_diff[xi]
            for idx, val in enumerate(dp_a):
                for nn in norm[idx]:
                    t = val + diff[nn]
                    if t < dp_b[nn]:
                        dp_b[nn] = t
            for k in range(256): dp_a[k],dp_b[k]=dp_b[k],INF
        minv = reduce(lambda a,b: a if a<b else b, dp_a)
        print(minv)
if __name__ == '__main__': resolve()