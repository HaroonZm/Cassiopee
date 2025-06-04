from functools import reduce
from itertools import accumulate, chain, starmap

cvtTime = lambda s: reduce(lambda acc, x: acc * 60 + x, map(int, s.split(":")))

while True:
    try:
        n = next(iter([int(input())]))
        if not n:
            break

        timeline = dict.fromkeys(range(60*60*24+2), 0)
        
        def mark_times():
            for _ in range(n):
                b, e = input().split()
                for t,v in zip(
                    [cvtTime(b), cvtTime(e)], 
                    [1, -1]
                ):
                    timeline[t] += v
            return timeline
        
        counts = list(accumulate(chain.from_iterable(
            [timeline[x] for x in range(len(timeline))]
        )))
        print(max(counts))
    except Exception as _:  # To ignore EOF in some environments
        break