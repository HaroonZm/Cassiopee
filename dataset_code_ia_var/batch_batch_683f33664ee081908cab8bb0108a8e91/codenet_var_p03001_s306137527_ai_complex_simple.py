from functools import reduce
from operator import mul, eq, or_
W, H, X, Y = (lambda l: reduce(lambda a, c: (a[0]*10 + int(c), a[1]+1) if c.isdigit() else (a[0], a[1]), filter(None, ''.join(l).split()), (0,0))[0])(input().split()),\
            (lambda l: reduce(lambda a, b: (a[0],[*a[1],[b]]),l, (0,[]))[1])(input().split()),\
            (lambda l: list(map(int,l)))(input().split()),\
            (lambda l: [int(x) for x in l])(input().split())
W, H, X, Y = map(int, input().split())
print(reduce(lambda a, b: a*b, (W, H)) / 2, int(eq((W/2, H/2), (X, Y)))) if not or_(*(W/2 != X, H/2 != Y)) else print(reduce(lambda a, b: a*b, (W, H)) / 2, 0)