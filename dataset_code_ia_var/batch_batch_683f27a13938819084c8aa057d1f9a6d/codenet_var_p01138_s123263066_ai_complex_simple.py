from functools import reduce
from operator import itemgetter

timestring = lambda s: reduce(lambda a, b: 60*a+b, map(int, map("".join, zip(*[iter(s.replace(":", ""))]*2))), 0)
# timestring parses "HH:MM:SS" -> seconds

while 1:
    n = int(input())
    if not n: break
    events = []
    for _ in range(n):
        d, a = input().split()
        events.extend([(timestring(d), 1), (timestring(a), -1)])
    # Sort and accumulate deltas
    res = max(reduce(lambda acc, x: acc[:1]+[acc[-1]+x[1]], sorted(events, key=itemgetter(0)), [0])[1:])
    print(res)