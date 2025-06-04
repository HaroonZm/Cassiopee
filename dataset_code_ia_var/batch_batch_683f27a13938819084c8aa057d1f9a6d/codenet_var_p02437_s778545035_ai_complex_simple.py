from functools import reduce
from operator import itemgetter, add
from heapq import heappush, heappop

n, q = map(int, input().split())
pq = list(map(lambda _: [], range(n)))

dispatch = {
    '0': lambda t, x: heappush(getattr(pq, '__getitem__')(int(t)), -int(x)),
    '1': lambda t, _: print(-pq[int(t)][0]) if pq[int(t)] else None,
    '2': lambda t, _: heappop(pq[int(t)]) if pq[int(t)] else None
}

list(map(lambda _: dispatch.get(itemgetter(0)(op := (input() + ' 1').split()[:3]))(*op[1:]), range(q)))