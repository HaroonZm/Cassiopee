from collections import Counter
import sys
readline = sys.stdin.readline
write = sys.stdout.write

def check(N, A):
    if N == 1:
        return A
    A.sort()

    C = Counter(A)
    c0 = C.get(0, 0)
    if c0 == N:
        return A
    c1 = C.get(1, 0)
    rest = A[c0+c1:]
    back = []
    if c0 > 0:
        if c0 % 2 == 0:
            back = [0]*c0 + [1]*c1
        else:
            if c1 > 0:
                x = 1
                c1 -= 1
            else:
                x, *rest = rest
            back = [0]*(c0 ^ 1) + [x] + [0] + [1]*c1
    else:
        back = [1]*c1
    if len(rest) >= 2 and rest[-1] == 3 and rest[-2] == 2:
        rest[-1], rest[-2] = rest[-2], rest[-1]
    return rest + back
def solve():
    N, *A = map(int, open(0).read().split())
    ans = check(N, A)
    write("\n".join(map(str, ans)))
    write("\n")
solve()