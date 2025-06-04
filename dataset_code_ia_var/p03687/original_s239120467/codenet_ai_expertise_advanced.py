from functools import lru_cache

s = input()

@lru_cache(maxsize=None)
def convert(st, toS):
    if all(ch == toS for ch in st):
        return 0
    min_ops = float('inf')
    for i in range(len(st) - 1):
        if st[i + 1] == toS and st[i] != toS:
            new_st = list(st)
            new_st[i] = toS
            ops = 1 + convert(''.join(new_st[:-1]), toS)
            min_ops = min(min_ops, ops)
    # If no change above, shrink the string
    if min_ops == float('inf'):
        min_ops = 1 + convert(st[:-1], toS)
    return min_ops

print(min(convert(s, c) for c in set(s)))