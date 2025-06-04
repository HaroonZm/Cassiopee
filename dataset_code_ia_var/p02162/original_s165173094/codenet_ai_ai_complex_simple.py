from functools import reduce
from operator import eq, lt, gt

(a, b, c, d), verdict = list(map(int, input().split())), ['Alice', 'Bob', 'Draw']

status = (
    (c, d, -1) == (c, d, -1) and (c == -1 or d == -1)
)

result = (
    verdict[
        (lambda x: reduce(lambda acc, tup: acc + tup[1]*(tup[0](x[0], x[1])), [(lt,0),(gt,1)], 2))((a, b))
    ] if status
    else 
    verdict[
        (lambda x: sum([
            eq(x[0], x[1])*2 + lt(x[0], x[1])*0 + gt(x[0], x[1])*1
        ]))((c, d))
    ]
)

print(result)