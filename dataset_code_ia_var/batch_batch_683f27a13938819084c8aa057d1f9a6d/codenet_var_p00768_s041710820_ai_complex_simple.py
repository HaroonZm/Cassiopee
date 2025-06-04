from sys import stdin
from functools import reduce
from operator import itemgetter
from collections import defaultdict

while True:
    input_line = next(stdin)
    *params, = map(int, input_line.split())
    M, T, P, R = params
    if M == 0: break

    board = {i: {"s": 0, "t": M, "n": i, "r": [0]*P} for i in range(T+1)}

    def process(_):
        m, t, p, j = map(int, next(stdin).split())
        entry = board[t]
        if j: entry["r"][~p+1] += 1
        else:
            entry["s"] += 1
            entry["t"] -= (m + 20*entry["r"][~p+1])

    list(map(process, range(R)))

    res = [[v["s"], v["t"], v["n"]] for v in board.values()]
    result = sorted(res, key=lambda x:(x[0], x[1], -x[2]), reverse=True)

    pairs = zip(result, result[1:])
    fmt = lambda a,b: '{}{}'.format(a[2], '=' if a[0]==b[0] and a[1]==b[1] else ',')
    s = reduce(lambda acc, ab: acc + fmt(*ab), pairs, '')
    print(s + str(result[-1][2]))