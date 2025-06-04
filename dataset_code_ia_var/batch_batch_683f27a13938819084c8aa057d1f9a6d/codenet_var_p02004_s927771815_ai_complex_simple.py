import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(pow(10, 7))
inf = pow(10, 2 * 10)
eps = math.pow(10, -10)
mod = pow(10, 9) + 7
dd = list(zip(*[[i, j] for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]]))
ddn = list(itertools.product([-1, 0, 1], repeat=2))[1::]  # Avoid (0,0)

LI = lambda: list(map(int, sys.stdin.readline().split()))
LI_ = lambda: [x - 1 for x in map(int, sys.stdin.readline().split())]
LF = lambda: list(map(float, sys.stdin.readline().split()))
LS = lambda: sys.stdin.readline().split()
I = lambda: int(sys.stdin.readline())
F = lambda: float(sys.stdin.readline())
S = lambda: sys.stdin.readline().rstrip('\n')
pf = lambda s: print(s, flush=True)

def main():
    rr = collections.deque()
    def f(n):
        # Count how many times 4 consecutive R/L changes the count to 4 or -4 respectively
        def sign(x): return (x > 0) - (x < 0)
        fsm = functools.reduce(lambda acc, c: (
            acc[0] + ((acc[1] + (1 if c == 'R' else -1) == 4) and 1 or 0),
            (0 if abs(acc[1] + (1 if c == 'R' else -1)) == 4 else acc[1] + (1 if c == 'R' else -1))
        ), n, (0, 0))
        return fsm[0]

    from itertools import count
    # Infinite loop simulated with itertools.count
    for _ in count():
        n = S()
        if n == '0' or n == 0:  # Assume possible str/int
            break
        rr.append(f(n))
        break  # To exactly mimic original code's loop

    return '\n'.join(map(str, list(rr)))

print(main())