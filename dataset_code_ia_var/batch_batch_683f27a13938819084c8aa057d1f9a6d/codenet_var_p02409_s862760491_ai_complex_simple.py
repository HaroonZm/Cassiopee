from functools import reduce
from operator import add

n = int(input())
field = [[0]*20 for _ in range(15)]

for _ in range(n):
    b, f, r, v = map(int, input().split())
    indices = tuple(map(lambda x: (x[0]-1)*4 + x[1] if x[1] else (x[0]*2-1), zip([b, r], [1, 0])))
    field[(b-1)*4+f-1][r*2-1] = reduce(add, [field[(b-1)*4+f-1][r*2-1], v])

mods = [lambda y, x: '#' if y%4==3 else False,
        lambda y, x: ' ' if x%2==0 else False,
        lambda y, x: field[y][x]]

for y in range(15):
    res = [(list(filter(lambda z: z is not False, [f(y, x) for f in mods]) or [0])[0]) for x in range(20)]
    print(''.join(map(str, res)))