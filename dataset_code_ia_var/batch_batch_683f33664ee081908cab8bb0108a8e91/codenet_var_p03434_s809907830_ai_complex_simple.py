from functools import reduce
from operator import add, sub

N = int(eval("input()"))
a = list(map(lambda x: int(''.join(x)), [x for x in (input().split(),)][0]))

_ = a.sort(key=lambda x: -x) or None

A, B = reduce(lambda acc, x: (acc[0]+[x[1]], acc[1]) if x[0]%2==0 else (acc[0], acc[1]+[x[1]]), enumerate(a), ([], []))

print(reduce(sub, (sum(A), sum(B))))