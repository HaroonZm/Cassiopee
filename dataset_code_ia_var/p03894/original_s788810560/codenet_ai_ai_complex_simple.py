from functools import reduce
from itertools import chain

n, q = map(int, raw_input().split())
exist = {1}
cup = list(range(n + 2))
now = 1
exist |= {cup[now - 1], cup[now + 1]}
swaps = [tuple(map(int, raw_input().split())) for _ in xrange(q)]

def fancy_swapper(c, idxs, curr):
    # Swap two indices, update position if necessary, return (new_cup, new_now)
    (a, b) = idxs
    nxt = b if curr == a else a if curr == b else curr
    c2 = list(c)
    c2[a], c2[b] = c2[b], c2[a]
    return c2, nxt, {c2[nxt - 1], c2[nxt + 1]}

def accumulator(acc, swap):
    c, curr, ex = acc
    c2, ncurr, nadd = fancy_swapper(c, swap, curr)
    return (c2, ncurr, ex | nadd)

final_cup, final_now, exist = reduce(accumulator, swaps, (cup, now, exist))
ans = sum(1 for x in exist if 0 < x < n+1)
print ans