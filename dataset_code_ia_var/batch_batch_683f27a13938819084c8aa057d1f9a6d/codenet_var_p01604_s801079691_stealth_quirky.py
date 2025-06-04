import heapq as HP
import collections as CTN

def __ipt(): return int(input())
_INPUT = __ipt()
_LINES = [input() for _n in range(_INPUT)]
_BEGIN = tuple("sssssssssss")
_THE_GOAL = tuple("ggggggggggg")
_LINES += ["ggggggggggg;"]
G = CTN.defaultdict(list)
__current = tuple(list(_BEGIN))
__idx = -1
for zz, _X in enumerate(_LINES):
    if _X[:4] == "goto":
        G[__current].append((tuple(_X[5:-1]), __idx+1))
        __idx += 1
    else:
        G[__current].append((tuple(_X[:-1]), __idx+1))
        __current = tuple(_X[:len(_X)-1])
        __idx = -1
_PRIOQ = []
HP.heappush(_PRIOQ, (0, _BEGIN))
_D = {}
for __ in G: _D[__] = float("inf")
_D[_BEGIN] = 0
while _PRIOQ:
    __delta, __node = HP.heappop(_PRIOQ)
    for _next, _cost in G[__node]:
        _val = __delta + _cost
        if _val < _D.get(_next, float("inf")):
            _D[_next] = _val
            HP.heappush(_PRIOQ, (_val, _next))
print(_D[_THE_GOAL])