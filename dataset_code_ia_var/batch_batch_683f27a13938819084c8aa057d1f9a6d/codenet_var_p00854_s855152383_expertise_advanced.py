import sys

from functools import partial

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
EPS = 1e-10
MOD = 998244353

def ints(): return list(map(int, sys.stdin.readline().split()))
def ints0(): return [x - 1 for x in map(int, sys.stdin.readline().split())]
def floats(): return list(map(float, sys.stdin.readline().split()))
def strs(): return sys.stdin.readline().split()
def int1(): return int(sys.stdin.readline())
def float1(): return float(sys.stdin.readline())
def str1(): return input()
pf = partial(print, flush=True)

def main():
    results = []
    for nkm in iter(ints, [0]):
        if len(nkm) < 3:
            continue
        n, k, m = nkm
        if n == 0:
            break
        idx = m - 1
        alive = list(range(1, n+1))
        for rem in range(n-1):
            alive.pop(idx)
            if alive:
                idx = (idx - 1 + k) % len(alive)
        results.append(str(alive[0]))
    return "\n".join(results)

print(main())