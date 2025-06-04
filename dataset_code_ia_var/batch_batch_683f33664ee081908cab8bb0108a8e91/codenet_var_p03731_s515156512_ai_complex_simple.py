from functools import reduce
from operator import add, itemgetter

_, t = map(int, input().split())
l = list(map(int, input().split()))

def f(x, y):
    d = y - x
    return d if d < t else t

pairs = zip(l, l[1:])
s = reduce(add, map(lambda p: f(*p), pairs), 0)
s = (lambda u: u + t)(s)
print(s)