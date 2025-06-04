from functools import reduce
from operator import itemgetter
from itertools import starmap, chain
from collections import deque

INF = float('9' * 18)

reader = lambda: list(map(int, __import__('sys').stdin.readline().split()))
z = [reader(), reader()]

roll = lambda arr: zip(*(iter(arr[1:]),) * 2)
P = set(chain.from_iterable(map(roll, z)))
P = sorted(P, key=lambda x: x[0]*60 + x[1])
fmt = lambda t: f"{t[0]}:{str(t[1]).zfill(2)}"
craft = deque(starmap(fmt, P))
print(' '.join(craft))