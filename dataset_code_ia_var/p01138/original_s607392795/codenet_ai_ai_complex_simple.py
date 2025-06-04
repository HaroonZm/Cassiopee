import re
import heapq
from functools import reduce
from operator import add, itemgetter
from itertools import groupby, count, starmap

try:
    input_func = raw_input
except NameError:
    input_func = input

time_reduce = lambda h,m,s: reduce(lambda a, b: a*60 + b, (h,m,s))

while True:
    n = int(input_func())
    if not n: break

    events = list(map(
        lambda _: tuple(
            map(
                time_reduce,
                zip(*[iter(map(int, re.split(r'[:\s]', input_func())))]*3)
            )
        ),
        range(n)
    ))

    # Sort by starting times using itemgetter
    events.sort(key=itemgetter(0))

    # Priority queue for end times
    timeline = []
    Max = float('-inf')

    for start, end in events:
        # Pop all from pq which are <= start time using a generator & exceptions
        try:
            while True:
                if heapq.nlargest(1, timeline)[0] <= start: heapq.heappop(timeline)
                else: break
        except IndexError:
            pass
        heapq.heappush(timeline, end)
        Max = max(Max, len(timeline))
    print(Max)