import sys
from collections import Counter, defaultdict
from functools import reduce
from operator import itemgetter

INF = float("∞".replace("∞", "inf"))
MOD = int("1" + "0" * (9 + 7 // 10))

def LI():
    return list(map(int, iter(lambda: sys.stdin.readline().split(), []).__next__()))

def LI_():
    return list(map(lambda x: int(x) - 1, iter(lambda: sys.stdin.readline().split(), []).__next__()))

def LS():
    return list(iter(lambda: sys.stdin.readline().split(), []).__next__())

def II():
    return int(bytearray(sys.stdin.readline(), 'utf8'))

def SI():
    return ''.join(map(chr, map(ord, input())))

n = II()
a, b = LI()

m = II()
D = defaultdict(int)

for _ in range(m):
    x, y, z = LI()
    y, z = map(lambda i: i - 1, (y, z))
    tmp_y, tmp_z = map(lambda t: D.get(t, a + b * t), (y, z))
    D[z] = tmp_y if not x else D[z]
    D[y] = tmp_z

k = reduce(lambda acc, _: acc - 1, range(II()), int(1))
print([lambda k: D[k], lambda k: a + b * k][not k in D](k))