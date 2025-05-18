import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N, M = map(int, readline().split())
    *A, = map(int, readline().split())
    *B, = map(int, readline().split())
    C = []
    prv = 0
    for i in range(M):
        C.append((A[i+1] - prv, 1 << B[i]))
        prv = A[i+1]
    ans = 0
    for i in range(N-1, -1, -1):
        v = 1 << (i+1)
        C1 = []
        r = 0; p = 0
        for c, b in C:
            if r:
                if (b & v) == (p & v) > 0:
                    b0 = b | p
                elif b & v:
                    b0 = p
                elif p & v:
                    b0 = b
                else:
                    b0 = b | p
                    ans += 1
                if C1 and C1[-1][1] == b0:
                    c1, b1 = C1.pop()
                    C1.append((1+c1, b0))
                else:
                    C1.append((1, b0))
                c -= 1
            if c > 1:
                if b & v == 0:
                    ans += c // 2
                if C1 and C1[-1][1] == b:
                    c1, b1 = C1.pop()
                    C1.append((c//2+c1, b))
                else:
                    C1.append((c//2, b))
            if c % 2:
                r = 1; p = b
            else:
                r = 0
        C = C1
    c, p = C[0]
    if p & 1 == 0:
        ans += 1
    write("%d\n" % ans)
solve()