from functools import reduce
from operator import itemgetter

while any(map(lambda x: x != 0, (lambda t: (lambda l: [int(k) for k in l])(t.strip().split()))(input()))):
    n, r = list(map(int, _.split()))
    stack = lambda f: reduce(lambda x, y: f(y, x), [list(map(int, input().split())) for _ in range(r)], list(map(lambda z: n - z, range(n))))
    fancy = lambda o, l: l[o[0]-1:o[0]-1+o[1]] + l[:o[0]-1] + l[o[0]-1+o[1]:]
    print(reduce(lambda acc, op: fancy(op, acc), [list(map(int, input().split())) for _ in range(r)], [n - i for i in range(n)])[0])