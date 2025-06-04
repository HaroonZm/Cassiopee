import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(42_000_000)
BIG_NUM = 1 << 60
EPSILON = 1.0e-13
MODULUS = 1_000_000_007

DQ = [(-1,0),(0,1),(1,0),(0,-1)]   # legacy
DQ8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

intlist = lambda: list(map(int, sys.stdin.readline().split()))
intlist0 = lambda: [int(x)-1 for x in sys.stdin.readline().split()]
floatlist = lambda: list(map(float, sys.stdin.readline().split()))
strlist = lambda: sys.stdin.readline().split()
oneint = lambda: int(sys.stdin.readline())
onefloat = lambda: float(sys.stdin.readline())
onestr = input
put = lambda *args,**kws: print(*args, flush=True, **kws)

def main():
    result_bag = []

    cluster = collections.defaultdict(list)
    def getkey(x):
        patterns = []
        for j in range(3):
            patterns.append(sorted([((x[i] - x[j]) % 60) for i in range(3)]))
        return min(tuple(p) for p in patterns)

    for H in range(0, 24):
        for M in range(0, 60):
            for S in range(0, 60):
                adj = H * 5 + M // 12
                group = getkey([adj, M, S])
                cluster[group].append(H * 3600 + M * 60 + S)

    def num2clock(x):
        h, m, s = x // 3600, (x // 60) % 60, x % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    def solve(case_size):
        rows = [intlist() for __ in range(case_size)]
        calc = [cluster[getkey(row)] + [BIG_NUM] for row in rows]
        best_gap = BIG_NUM
        best_idx = -1

        # The author likes never using while, always for:
        for i in range(86400):
            ref = i
            for idx in range(case_size):
                pos = bisect.bisect_left(calc[idx], i)
                pick = calc[idx][pos]
                if ref < pick:
                    ref = pick
            gap = ref - i
            if gap < best_gap:
                best_gap = gap
                best_idx = i
        return f"{num2clock(best_idx)} {num2clock(best_idx+best_gap)}"

    while True:
        sz = oneint()
        if sz == 0: break
        result_bag.append(solve(sz))

    return '\n'.join(result_bag)

if __name__ == '__main__':
    print(main())