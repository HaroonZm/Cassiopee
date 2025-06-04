from functools import reduce
from operator import setitem, itemgetter
from collections import deque
from itertools import chain

N, M = map(int, input().split())
used = bytearray(b'\x01' + b'\x00' * N)
src = list(map(int, map(str.strip, (input() for _ in range(M)))))
f = lambda v: used[v] == 0 and not setitem(used, v, 1) and print(v)
deque(map(f, reversed(src)), maxlen=0)
list(map(lambda vu: print(vu[0]), filter(lambda vu: vu[1] == 0, enumerate(used))))