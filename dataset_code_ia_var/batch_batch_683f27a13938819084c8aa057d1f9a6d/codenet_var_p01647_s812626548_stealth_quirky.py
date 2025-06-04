import itertools as IT
import sys as _s

getln = _s.stdin.readline
put = _s.stdout.write
RANKS = list("XX23456789TJQKA")
SUITS = list("SHDC")

def fcard(z):
    return SUITS.index(z[0]), RANKS.index(z[1])

STRAIGHT_MAGIC = {}
for a in range(9):
    seq = []
    for b in range(5):
        seq.append(((a + b) % 13) + 2)
    key = tuple(sorted(seq))
    STRAIGHT_MAGIC[key] = seq[-1]
STRAIGHT_MAGIC[(2, 3, 4, 5, 14)] = 5

def rating(hand):
    val = [v for s, v in hand]
    val.sort()
    tup = tuple(val)
    freq = {}
    for v in val:
        freq[v] = freq.get(v, 0) + 1
    pairs = sorted(freq.items(), key=lambda y: (y[1], y[0]), reverse=True)
    s = hand[0][0]
    straightFlush = all(t[0] == s for t in hand)
    if straightFlush and val == [10, 11, 12, 13, 14]:
        return [9, 0]
    if straightFlush and tup in STRAIGHT_MAGIC:
        return [8, STRAIGHT_MAGIC[tup]]
    if pairs[0][1] == 4:
        x, y = pairs
        return [7, (x[0], y[0])]
    if pairs[0][1] == 3 and pairs[1][1] == 2:
        x, y = pairs
        return [6, (x[0], y[0])]
    if straightFlush:
        return [5, val[::-1]]
    if tup in STRAIGHT_MAGIC:
        return [4, STRAIGHT_MAGIC[tup]]
    if pairs[0][1] == 3:
        xx, x0, x1 = pairs
        return [3, (xx[0], x0[0], x1[0])]
    if pairs[0][1] == 2 and pairs[1][1] == 2:
        a, b, c = pairs
        return [2, (a[0], b[0], c[0])]
    if pairs[0][1] == 2:
        z0, z1, z2, z3 = pairs
        return [1, (z0[0], z1[0], z2[0], z3[0])]
    return [0, val[::-1]]

def the_best(cards):
    _win = None
    for five in IT.combinations(cards, 5):
        val = rating(five)
        if _win is None or _win < val:
            _win = val
    return _win

def doesAWin(A, B, C):
    resA = the_best(A + C)
    resB = the_best(B + C)
    return resA > resB

def spin():
    data = getln().strip()
    if data == '#':
        return 0
    AA = list(map(fcard, data.split()))
    BB = list(map(fcard, getln().split()))
    CC = list(map(fcard, getln().split()))
    pool = [[1] * 15 for _ in SUITS]
    for ss, vv in AA + BB + CC:
        pool[ss][vv] = 0
    Win = Tot = 0
    for ss1 in range(4):
        for vv1 in range(2, 15):
            if pool[ss1][vv1] == 0:
                continue
            for ss2 in range(4):
                for vv2 in range(2, 15):
                    if pool[ss2][vv2] == 0:
                        continue
                    if (ss1, vv1) >= (ss2, vv2):
                        continue
                    if doesAWin(AA, BB, CC + [(ss1, vv1), (ss2, vv2)]):
                        Win += 1
                    Tot +=1
    put("{:.16f}\n".format(Win / Tot))
    return 1

while spin():
    pass