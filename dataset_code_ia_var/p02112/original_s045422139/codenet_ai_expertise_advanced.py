from collections import defaultdict
from itertools import accumulate

n = int(input())
events = defaultdict(list)

for _ in range(n):
    m, d, v, s = map(int, input().split())
    start = (m - 1) * 30 + d - 1
    end = start + v
    for offset in range(v):
        day = (start + offset) % 360
        events[day].append(s)
    for offset in range(1, 361):
        dec = s - min(offset, 360 - offset)
        day = (end + offset - 1) % 360
        if dec > 0:
            events[day].append(dec)

eff = [max(events[day]) if events[day] else 0 for day in range(360)]
print(min(eff))