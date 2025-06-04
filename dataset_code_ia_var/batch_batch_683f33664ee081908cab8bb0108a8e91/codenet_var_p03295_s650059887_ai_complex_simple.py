from functools import reduce
from itertools import chain, tee, starmap

a, b = starmap(lambda u, v: int(u) - 1, zip(*tee(input().split(), 2)))
L = list(map(lambda _: list(map(int, input().split())), range(b + 1)))
L = list(sorted(L, key=lambda x: x[1]))

def fold(seq, init, func):
    return reduce(lambda acc, val: func(acc, val), seq, init)

def sched(acc, l):
    bridge_right, ans = acc
    c = bridge_right >= l[0] and bridge_right < l[1]
    if not c:
        return (l[1] - 1, ans + 1)
    return (bridge_right, ans)

bridge_right, ans = fold(L, (-float('inf'), 0), sched)
print(ans)