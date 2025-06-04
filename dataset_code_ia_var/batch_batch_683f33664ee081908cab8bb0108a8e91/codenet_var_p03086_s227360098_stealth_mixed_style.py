from functools import reduce

def is_base(ch):
    return ch == 'A' or ch == 'T' or ch == 'C' or ch == 'G'

def indices(seq):
    for idx, x in enumerate(seq):
        yield idx, x

s = list(input())
BASES = set(['A', 'T', 'C', 'G'])
l, r = -1, -1
res = [0, -1]

flag = False
start = end = None

idx = 0
while idx < len(s):
    letter = s[idx]
    if (letter in BASES):
        if not flag:
            flag = True
            start = idx
        end = idx
    else:
        if flag:
            if start is not None and end is not None:
                res = max(res, [start, end], key=lambda p: p[1] - p[0])
            flag = False
            start = end = None
    idx += 1

if flag and start is not None and end is not None:
    res = max(res, [start, end], key=lambda p: p[1] - p[0])

print((lambda l, r: r - l + 1)(res[0], res[1]))