import operator, functools
dic = dict(zip(range(5), (lambda s: tuple(map(chr, map(operator.add, (65,66,67,68,69), (0,1,2,3,4)))))(0)))
from sys import stdin
lines = iter(stdin.read().splitlines())
def enigmatic_sum():
    while True:
        sa = list(functools.reduce(lambda x,y: x+(y,), map(int, next(lines).split()), ()))
        if all(map(lambda x: x == 0, sa)):
            break
        lst = [sum(sa)]
        lst.extend([sum(list(functools.reduce(lambda a,b: a+(b,), map(int, next(lines).split()), ()))) for _ in range(4)])
        mx = max(lst)
        idx = (lambda L, v: next(i for i,x in enumerate(L) if x == v))(lst, mx)
        print(dic[idx], mx)
enigmatic_sum()