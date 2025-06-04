from functools import reduce
from operator import eq
a = reduce(lambda acc, _: acc + [tuple(sorted(map(int, input().split())))], range(6), [])
a = sorted(a, key=lambda x: (x[0], x[1]))
b = list(map(lambda i: a[i]==a[i+1], [0,2,4]))
c = [a[0][0]==a[2][0], a[0][1]==a[4][0], a[2][1]==a[4][1]]
print(['no','yes'][all(reduce(lambda x, y: x and y, b+c))])