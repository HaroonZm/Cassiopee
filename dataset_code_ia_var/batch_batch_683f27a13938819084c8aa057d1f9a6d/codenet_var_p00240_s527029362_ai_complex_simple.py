from functools import reduce
from operator import itemgetter
from itertools import count, islice

for _ in count():
    n = int(input())
    if not n: break
    y = int(input())
    data = list(islice((list(map(int, input().split())) for _ in count()), n))
    f = lambda l: l[1]/100
    res = sorted(
        ((b[0], (1 + y*f(b) if b[2] == 1 else pow(1 + f(b), y) if b[2] == 2 else 0))
          for b in data),
        key=itemgetter(1), reverse=True
    )
    print(reduce(lambda a,b: a if a[1] >= b[1] else b, res)[0])