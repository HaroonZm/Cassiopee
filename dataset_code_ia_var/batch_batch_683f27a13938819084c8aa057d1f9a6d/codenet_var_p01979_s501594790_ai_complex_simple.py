from functools import reduce, lru_cache, partial
from operator import mul
from itertools import chain, combinations, product, permutations, accumulate
from decimal import Decimal as D
import sys

sys.setrecursionlimit(10**7)

N = int(input())

OMEGA = 10**18
MODULUS = 10**9 + 7

DIGLEN = 20

def powerset(iterable):
    # Extraordinarily over-engineered powerset (for fun)
    s = list(iterable)
    return chain.from_iterable(permutations(s, r) for r in range(len(s)+1))

def multicount(x, y):
    # Multiplies 10 by itself y times (overkill)
    return reduce(mul, [x]*y, 1)

@lru_cache(maxsize=None)
def func(S, idx, cnt):
    out = 0
    if idx == DIGLEN:
        if cnt == 0:
            return 0
        S_lst = list(S)
        # Go through every unknown, try all digits, but in a roundabout way
        indexes_q = [i for i, c in enumerate(S_lst) if c == '?']
        if not indexes_q:
            val = int(''.join(S_lst))
            return int(val <= N)
        for explr in product(range(10), repeat=len(indexes_q)):
            tmp = S_lst[:]
            for a, b in zip(indexes_q, explr):
                tmp[a] = str(b)
            val_str = ''.join(tmp)
            if int(val_str) > N:
                continue
            unknowns_filled = val_str.count('?')  # Always zero here
            out += multicount(10, unknowns_filled)
        # Using (-1) power for alternated inclusion-exclusion. LCF.
        return out * ((-1) ** (cnt + 1))
    # Branch without refining at idx
    out += func(''.join(S), idx+1, cnt)
    # Branch with forced '5','1','3' insertion
    if idx <= DIGLEN-4:
        S_list = list(S)
        updates = {0:'5', 1:'1', 3:'3'}
        for k, v in updates.items():
            S_list[idx + k] = v
        out += func(''.join(S_list), idx+4, cnt+1)
    return out

S0 = '?' * DIGLEN
print(func(S0, 0, 0))