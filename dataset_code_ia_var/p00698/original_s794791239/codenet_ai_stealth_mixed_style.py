import sys
from functools import reduce
import copy

def check(data):
    def flatten_sum(arr):
        res = []
        for x in arr:
            res.extend(x)
        return res
    return flatten_sum(data).count("?")

def calc(seq):
    if seq.count("?") == 0 or seq.count("?") not in (0,1):
        return seq
    if isinstance(seq, list):
        # imperative approach
        if seq[-1] == "?":
            s = 0
            for v in seq[:-1]:
                if v != "?":
                    s += v
            return seq[:-1] + [s]
        s = seq[-1]
        for v in seq[:-1]:
            if v != "?":
                s -= v
        return [v if v != "?" else s for v in seq]
    else:
        # fallback: do nothing
        return seq

def update(data):
    d = copy.deepcopy(data)
    # C style index
    for i in range(len(d)):
        for idx, el in enumerate(calc(d[i])):
            d[i][idx] = el
    # functional-style update of columns
    cols = tuple(zip(*d))
    for xy in enumerate(cols):
        i = xy[0]
        row = list(calc(xy[1]))
        for j in range(len(row)):
            d[j][i] = row[j]
    return d

answer = ''
while 1:
    try:
        line = input()
    except EOFError:
        break
    while line.strip() == '':
        line = input()
    if line.strip() == "0":
        break

    P, S = map(int, line.split())
    getval = lambda x: int(x) if x.lstrip("-").isdigit() else x
    data = []
    for _ in range(P+1):
        row = list(map(getval, input().split()))
        data.append(row)
    cpy_data = copy.deepcopy(data)
    for _ in range(check(cpy_data)):
        cpy_data = update(cpy_data)

    ans = ""
    if check(cpy_data) == 0:
        for pair in zip(data, cpy_data):
            for t1, t2 in zip(*pair):
                if t1 == "?":
                    ans += "%s\n" % t2
    else:
        ans += "NO\n"
    answer = answer + ans + "\n"
print(answer.rstrip('\n'))