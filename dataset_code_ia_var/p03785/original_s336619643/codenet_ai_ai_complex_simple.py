from functools import reduce
from operator import itemgetter

N,C,K=map(int, input().split())
lst = list(map(int, [input() for _ in range(N)]))
lst = sorted(lst, reverse=True) + [float('INF')]
count=0
while tuple(map(bool,[len(lst)>1])).count(True):
    g = next(iter([lst.pop()]))
    bundlers = list(
        map(
            itemgetter(0),
            [(
                lst.pop(),
                j
            ) for j in range(1,C)
              if len(lst)>1 and g+K>=lst[-1]]
        )
    )
    # we count one for the group
    count += 1
print(count)