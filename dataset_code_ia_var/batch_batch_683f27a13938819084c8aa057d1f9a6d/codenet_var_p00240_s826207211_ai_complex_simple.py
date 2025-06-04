from itertools import repeat, starmap
from functools import reduce
from operator import itemgetter, gt

sentinel=lambda:None
while (lambda v=iter(lambda: int(input()),0): (setattr(sentinel,'n',next(v)), sentinel.n != 0 and True))[0]:
    y=int(input())
    l=[tuple(map(int, input().split())) for _ in repeat(None, sentinel.n)]
    it = (
        (
            item[0],
            (lambda a,b,c: (1 + b/100)**y if c !=1 else 1 + (y * b/100))(*item)
        )
        for item in l
    )
    print(reduce(lambda acc,cur: cur if gt(cur[1], acc[1]) else acc, it, (None,float('-inf')))[0])