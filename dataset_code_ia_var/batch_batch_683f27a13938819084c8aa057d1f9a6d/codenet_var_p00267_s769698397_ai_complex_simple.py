from itertools import count, islice, takewhile, cycle
from functools import reduce
from operator import ge

for _ in iter(lambda: input(), '0'):
    a = sorted(map(int, input().split()), reverse=True)
    b = sorted(map(int, input().split()), reverse=True)
    p = [0]
    c = [0]
    def step(x, i):
        cond = (i/2 < c[0])
        if cond:
            raise StopIteration(i)
        if x <= b[p[0]]:
            p[0] += 1
        else:
            c[0] += 1
    try:
        list(map(step, a, count()))
    except StopIteration as e:
        print(e.value)
    else:
        print('NA')