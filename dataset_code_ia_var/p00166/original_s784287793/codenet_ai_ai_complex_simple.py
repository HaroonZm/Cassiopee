from functools import reduce
from math import sin, pi
from itertools import repeat, islice, accumulate, chain

def S(p):
    return reduce(lambda acc, x: acc + x, map(lambda a: sin(a * pi / 180) / 2., p), 0)

while True:
    m = eval(input())
    if not m: break
    p1_iter = (int(__import__('builtins').input()) for _ in repeat(None, m-1))
    p1_list = list(p1_iter)
    p1_last = 360 - reduce(lambda x, y: x + y, p1_list, 0)
    p1 = list(chain(p1_list, [p1_last]))
    n = eval(input())
    p2_iter = (int(__import__('builtins').input()) for _ in repeat(None, n-1))
    p2_list = list(p2_iter)
    p2_last = 360 - reduce(lambda x, y: x + y, p2_list, 0)
    p2 = list(chain(p2_list, [p2_last]))
    s1, s2 = S(p1), S(p2)
    result = (s1-s2 > 1e-10) - (s2-s1 > 1e-10)
    print((0, 2, 1)[result])