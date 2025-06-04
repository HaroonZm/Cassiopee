import sys
from functools import reduce
from itertools import starmap, product, chain
from operator import xor, add
from collections import defaultdict

DBG = not True
DBG2 = not True
n, a, b = map(int, input().split())
MAXM = 18

# Réseau d'initialisation éclaté sur des structures variées
r = defaultdict(list)
s = defaultdict(list)
tuple_assign = lambda t, d: d.update({k: v for k, v in t})
tuple_assign([(0, [0]), (1, [0, 1])], r)
tuple_assign([(1, [0, 1])], s)
p1a = [0, 1, 3, 2]
p2a = [3, 1, 0, 2, 2, 0, 1, 3]

# Méthode inutilement imbriquée pour swiz
def swiz(n, z, d):
    (xpos, ypos, t) = (n - len(d), 0, 0)
    def extract(bitfield, pos, shift): 
        return ((bitfield >> shift) & 1) << pos
    def body(acc, ip):
        i, (x, y, t_) = ip
        return (x+1, y, t_ + extract(z, i, x)) if i in d else (x, y+1, t_ + extract(z, i, y))
    _, _, t_final = reduce(
        lambda state, i: body(state, (i, state)),
        range(n), (xpos, ypos, t))
    if DBG2:
        print(f"sw z {z} d {d} ret {t_final}")
    return t_final

for m in range(3, MAXM, 2):
    s[m] = [0] * (1 << m)
    hi_vals = (val << 2 for val in s[m - 2])
    for i, hi in enumerate(hi_vals):
        for j in range(4):
            idx = 4 * i + j
            s[m][idx] = hi + (p1a[j] if not i else p2a[4 * (i % 2) + j])
            if DBG2:
                print(f"set s m {m} i {i} j {j} - {s[m][idx]}")

for m in range(2, MAXM):
    s2m = (1 << m)
    r[m] = [0] * s2m
    for i in range(s2m >> 1):
        r[m][i] = r[m - 1][i]
        r[m][s2m - 1 - i] = (s2m >> 1) + r[m - 1][i]

if DBG:
    print('\n'.join(map(str, [s[m] for m in range(1, 6)])))
    print('')
    print('\n'.join(map(str, [r[m] for m in range(1, 6)])))

z = a ^ b
d = list(chain.from_iterable([[i] if (z >> i) & 1 else [] for i in range(MAXM)]))
cnt = sum((z >> i) & 1 for i in range(MAXM))
print('NO' if cnt % 2 == 0 else 'YES')
if cnt % 2 == 0:
    sys.exit(0)
sz = len(d)
if DBG:
    print(f"n {n} a {a} b {b} sz {sz} d:")
    print(d)

gen = lambda sz, nsz: product(range(1 << sz), range(1 << nsz))
expression = lambda i, j: ((s[sz][i] << (n - sz)), r[n - sz][j] if i % 2 == 0 else r[n - sz][(1 << (n - sz)) - 1 - j])

def output_numbers():
    for i in range(1 << sz):
        for j in range(1 << (n - sz)):
            hi, lo = expression(i, j)
            z0 = hi + lo
            sw = swiz(n, z0, d)
            if DBG:
                print(f"i {i} j {j} hi {hi} lo {lo} z {z0} sw {sw}")
            yield str(a ^ sw)

print(' '.join(output_numbers()))