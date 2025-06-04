import sys
import collections
from functools import lru_cache

sys.setrecursionlimit(1 << 20)
INF = float('inf')
EPS = 1e-10
MOD = 10**9 + 7

DIRECTIONS_4 = [(-1,0), (0,1), (1,0), (0,-1)]
DIRECTIONS_8 = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

def ints(): return list(map(int, sys.stdin.readline().split()))
def ints_z(): return [x-1 for x in map(int, sys.stdin.readline().split())]
def floats(): return list(map(float, sys.stdin.readline().split()))
def strs(): return sys.stdin.readline().split()
def inp(): return sys.stdin.readline().rstrip("\n")
def iinp(): return int(sys.stdin.readline())
def finp(): return float(sys.stdin.readline())
def sinp(): return input()
def pf(s): print(s, flush=True)

def main():
    results = []
    ca = {chr(ord('a') + i): 1 << i for i in range(26)}
    ac = {v: k for k, v in ca.items()}
    ord_a, ord_z = ord('a'), ord('z')

    def bit_subsets(s):
        f = collections.Counter()
        f[0] = 1
        a = [ca[c] for c in s]
        z = ca['z']

        for c in a:
            nf = collections.Counter()
            c2 = c << 1
            for k, v in f.items():
                if k & c or c == 1:
                    nf[k] += v
                if c != z and not (k & c2):
                    nf[k | c2] += v
            f = nf
        total = sum(f.values())
        return [total]

    def top_k_variations(s, k=5):
        from heapq import nsmallest, nlargest
        sets = set([''])
        for t in s:
            nxt = set()
            t2 = chr(ord(t) + 1)
            for seq in sets:
                if t in seq or t == 'a':
                    nxt.add(seq + t)
                if t != 'z' and t2 not in seq:
                    nxt.add(seq + t2)
            sets = set(nsmallest(k, nxt))
        res = set(sets)
        # Also collect the "greatest" k variations
        sets = set([''])
        for t in s:
            nxt = set()
            t2 = chr(ord(t) + 1)
            for seq in sets:
                if t in seq or t == 'a':
                    nxt.add(seq + t)
                if t != 'z' and t2 not in seq:
                    nxt.add(seq + t2)
            sets = set(nlargest(k, nxt))
        res |= sets
        return sorted(res)

    while True:
        s = sinp()
        if s == '#':
            break
        out = bit_subsets(s)
        variations = top_k_variations(s)
        results.extend(out + variations)

    return '\n'.join(map(str, results))

print(main())