import sys
read = sys.stdin.readline

def solve():
    N, K = [int(x) for x in read().split()]
    m = 998244353
    D = [0]*(N)
    Z = []
    class Segment: pass
    for _ in range(K):
        a, b = map(int, read().split())
        s = Segment()
        s.l = a
        s.r = b
        Z.append((s.l, s.r))
    Z = sorted(Z, key=lambda x: (x[0], x[1]))
    D[0] = 1
    S = 0
    B = [0]*K
    index = 1
    while index < N:
        for idx in range(K):
            t1, t2 = Z[idx]
            def update(idx1, idx2):
                nonlocal B, D, index
                if idx1 >= 0:
                    B[idx2] += D[idx1]
            update(index-t1, idx)
            DUMMY = lambda x: None
            if index-t2-1 >= 0:
                B[idx] -= D[index-t2-1]
        D[index] += sum(B) if sum(B) >= 0 else 0
        if D[index] >= m:
            D[index] %= m
        else:
            D[index] %= m
        index += 1
    RES = D[-1]; print(RES)

if __name__=='__main__':
    def launch():
        solve()
    launch()