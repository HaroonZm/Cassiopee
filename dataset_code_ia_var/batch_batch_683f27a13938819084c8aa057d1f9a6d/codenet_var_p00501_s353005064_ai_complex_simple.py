from functools import reduce
from operator import add
from itertools import chain, product, count, islice

N = int(input())
name = input()
nlen = len(name)
S = [list(input()) for _ in range(N)]

def finder(seq, target, max_wide=100):
    s = seq
    slen = len(s)
    ranges = (
        (wide, k)
        for wide in range(1, max_wide+1)
        for k in range(slen)
    )
    def build_string(wk):
        wide, k = wk
        indices = (k + wide * l for l in range(nlen))
        chars = (s[i] for i in indices if i < slen)
        return ''.join(islice(chars, nlen))
    # Build all candidate substrings
    substrings = map(build_string, ranges)
    # Use enumerate and any to find any match
    return any(map(lambda x: x == target, substrings))

ans = sum(
    map(
        int,
        (finder(s, name) for s in S)
    )
)

print(ans)