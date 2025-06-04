from itertools import count, takewhile, islice
from functools import reduce
from collections import defaultdict, OrderedDict

raw = (lambda s=[]: (lambda: (input() if s.append(None) or s==[] else (_ for _ in ()).throw(EOFError))) )() # Mock input for code runner; replace with raw_input in Python 2

d = defaultdict(lambda: [0,0])
sentry = [0]
inputs = []

def getlines():
    for _ in count():
        try:
            line = raw()
            if ',' in line:
                yield tuple(map(int, line.strip().split(',')))
            else:
                raise Exception
        except:
            sentry[0] += 1
            if sentry[0] > 1:
                break

history = list(getlines())

def first_entries(h):
    appeared = OrderedDict()
    for n,k in h:
        if n not in appeared:
            appeared[n] = []
        appeared[n].append(k)
    return list(appeared.items())

temp_count = defaultdict(list)
for idx,(n,k) in enumerate(history):
    temp_count[n].append(idx)

memo = {}

for idx,(n,k) in enumerate(history):
    memo.setdefault(n, [0,0])
    memo[n][0] += 1
    if temp_count[n][0] != idx:
        memo[n][1] = 2
    elif idx == 0:
        memo[n][1] = 1

result = sorted([(key, value[0]) for key, value in memo.items() if value[1]==2], key=lambda x: x[0])

list(map(lambda tup: print(tup[0],tup[1]), result))