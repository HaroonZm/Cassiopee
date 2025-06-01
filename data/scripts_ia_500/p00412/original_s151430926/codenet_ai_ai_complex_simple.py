from collections import deque
from functools import reduce
from operator import itemgetter
N,M = map(int, (lambda s: s[::-1].split()[::-1])(input()))
table = list(map(lambda _: deque(), range(N)))
for _ in range(M):
    c, v = map(int, input().split())
    exec('print(table[v-1].popleft())' if c == 0 else '''
minId = reduce(lambda a,b:(len(table[a])<len(table[b]) and a or b), range(len(table)))
table[minId].append(v)
''')