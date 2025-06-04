import sys
import itertools
from collections import defaultdict
from functools import partial

# Optimized recursion handling and some constants as immutables
sys.setrecursionlimit(10 ** 7)
INF = float('inf')
EPS = 1e-10
MOD = 10 ** 9 + 7

DD = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DDN = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def _ints(): return list(map(int, sys.stdin.readline().split()))
def _ints0(): return [x-1 for x in map(int, sys.stdin.readline().split())]
def _floats(): return list(map(float, sys.stdin.readline().split()))
def _strs(): return sys.stdin.readline().split()
def _int(): return int(sys.stdin.readline())
def _float(): return float(sys.stdin.readline())
def _raw(): return sys.stdin.readline().rstrip()
def _flush_print(s): print(s, flush=True)

def main():
    results = []

    def solve(n):
        words = [_raw() for _ in range(n)]
        chars = set().union(*words)
        non_zero = {w[0] for w in words if len(w) > 1}
        
        char2idx = {}
        idx2char = []
        for i, c in enumerate(sorted(chars, key=lambda x: (x in non_zero, x))):
            char2idx[c] = i
            idx2char.append(c)
        
        l = len(chars)
        weights = [0] * l
        for w in words[:-1]:
            mult = 1
            for c in reversed(w):
                weights[char2idx[c]] += mult
                mult *= 10
        mult = 1
        for c in reversed(words[-1]):
            weights[char2idx[c]] -= mult
            mult *= 10

        answer = 0
        half = l // 2
        rem = l - half
        weights_a, weights_b = weights[:half], weights[half:]

        # Small utility optimizations
        range9 = tuple(range(1, 10))
        perms = lambda items, n=None: itertools.permutations(items, n or len(items))
        combs = itertools.combinations

        def partitioned_search(wa, wb, na, nb):
            result = 0
            domain = set(range9)
            for aset in combs(range9, na):
                avals = set(aset)
                bvals = domain - avals
                adict = defaultdict(int)
                bdict = defaultdict(int)

                for a in perms(aset):
                    adict[sum(w * d for w, d in zip(wa, a))] += 1
                for b in perms(bvals, nb):
                    bdict[sum(w * d for w, d in zip(wb, b))] += 1
                    
                # Simultaneously walk sorted keys (like merge)
                ad, bd = sorted(adict.items()), sorted(bdict.items(), reverse=True)
                ai = bi = 0
                while ai < len(ad) and bi < len(bd):
                    total = ad[ai][0] + bd[bi][0]
                    if total == 0:
                        result += ad[ai][1] * bd[bi][1]
                        ai += 1
                        bi += 1
                    elif total < 0:
                        ai += 1
                    else:
                        bi += 1

            return result

        zero_pos = [i for i, c in enumerate(idx2char) if c not in non_zero][::-1]
        na = l - len(zero_pos)
        nb = l - na
        # Special edge case shortcut
        if na == 0 or nb < 2:
            cws = [weights[i+1] - weights[i] for i in range(l-1)]
            for a in perms(range9, l-1):
                tw = sum(weights[i] * a[i] for i in range(l-1))
                zz = l - 1
                for zi in zero_pos:
                    while zz > zi:
                        zz -= 1
                        tw += cws[zz] * a[zz]
                    if tw == 0:
                        answer += 1
        else:
            wa, wb = weights[:na], weights[na:]
            zpos = [z - na for z in zero_pos]
            for aset in combs(range9, na):
                adict = defaultdict(int)
                bdict = defaultdict(int)

                for a in perms(aset):
                    adict[sum(w * d for w, d in zip(wa, a))] += 1
                bvals = set(range9) - set(aset)
                cws = [wb[i+1] - wb[i] for i in range(nb-1)]
                for b in perms(bvals, nb-1):
                    tw = sum(wb[i] * b[i] for i in range(nb-1))
                    zz = nb - 1
                    for zi in zpos:
                        while zz > zi:
                            zz -= 1
                            tw += cws[zz] * b[zz]
                        bdict[tw] += 1
                ad, bd = sorted(adict.items()), sorted(bdict.items(), reverse=True)
                ai = bi = 0
                while ai < len(ad) and bi < len(bd):
                    total = ad[ai][0] + bd[bi][0]
                    if total == 0:
                        answer += ad[ai][1] * bd[bi][1]
                        ai += 1
                        bi += 1
                    elif total < 0:
                        ai += 1
                    else:
                        bi += 1

        return answer

    while True:
        n = _int()
        if n == 0:
            break
        results.append(solve(n))

    return '\n'.join(map(str, results))

if __name__ == "__main__":
    print(main())