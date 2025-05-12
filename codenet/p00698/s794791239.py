import sys
from copy import deepcopy
def check(data):
    return reduce(lambda a, b: a+b, data).count("?")

def calc(seq):
    if "?" not in seq or not(0 <= seq.count("?") <= 1) :
        return seq
    if seq[-1] == "?":
        return seq[:-1] + sum(seq[:-1])
    a = seq[-1] - sum(s for s in seq[:-1] if s != "?")
    return [s if s != "?" else a for s in seq]

def update(data):
    data = deepcopy(data)
    for i in xrange(len(data)):
        for j, d in enumerate(calc(data[i])):
            data[i][j] = d
    t_data = zip(*data)
    for i in xrange(len(t_data)):
        for j, d in enumerate(calc(t_data[i])):
            data[j][i] = d
    return data

answer = ""
while True:
    line = raw_input()
    while line.isspace() or not line: #!?!?!!!
        line = raw_input()
    if line == "0":
        break
    P, S = map(int, line.split())
    data = [map(lambda x: int(x) if x.replace("-", "").isdigit() else x, raw_input().split())
            for _ in xrange(P+1)]
    cdata = deepcopy(data)
    for _ in xrange(check(cdata)):
        cdata = update(cdata)
    ans = ""
    if check(cdata) == 0:
        for d in zip(data, cdata):
            for e1, e2 in zip(*d):
                if e1 == "?":
                    ans += "{}\n".format(e2)
    else:
        ans += "NO\n"
    answer += ans + "\n"
print answer.strip("\n")