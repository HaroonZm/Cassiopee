import sys
from copy import deepcopy
from functools import reduce

answer = ""
while True:
    line = raw_input()
    while line.isspace() or not line:
        line = raw_input()
    if line == "0":
        break

    P, S = map(int, line.split())
    data = []
    for _ in xrange(P + 1):
        row = raw_input().split()
        row2 = []
        for x in row:
            if x.replace("-", "").isdigit():
                row2.append(int(x))
            else:
                row2.append(x)
        data.append(row2)

    cdata = deepcopy(data)
    def flat_check(dd):
        cnt = 0
        for row in dd:
            for v in row:
                if v == "?":
                    cnt += 1
        return cnt

    lcnt = flat_check(cdata)
    for _ in xrange(lcnt):
        tdata = deepcopy(cdata)
        # rows
        for i in xrange(len(tdata)):
            seq = tdata[i]
            qcount = 0
            for v in seq:
                if v == "?":
                    qcount +=1
            if "?" not in seq or not(0 <= qcount <= 1):
                res = seq
            else:
                if seq[-1] == "?":
                    s = 0
                    for v in seq[:-1]:
                        if v != "?":
                            s += v
                    nv = s
                    res = seq[:-1] + [nv]
                else:
                    s = 0
                    for v in seq[:-1]:
                        if v != "?":
                            s += v
                    a = seq[-1] - s
                    res = []
                    for s2 in seq:
                        if s2 != "?":
                            res.append(s2)
                        else:
                            res.append(a)
            for j, d in enumerate(res):
                tdata[i][j] = d
        # columns
        z = []
        for col in xrange(len(tdata[0])):
            colitems = []
            for row in tdata:
                colitems.append(row[col])
            z.append(colitems)
        znew = []
        for seq in z:
            qcount = 0
            for v in seq:
                if v == "?":
                    qcount += 1
            if "?" not in seq or not(0 <= qcount <= 1):
                res = seq
            else:
                if seq[-1] == "?":
                    s = 0
                    for v in seq[:-1]:
                        if v != "?":
                            s += v
                    nv = s
                    res = seq[:-1] + [nv]
                else:
                    s = 0
                    for v in seq[:-1]:
                        if v != "?":
                            s += v
                    a = seq[-1] - s
                    res = []
                    for s2 in seq:
                        if s2 != "?":
                            res.append(s2)
                        else:
                            res.append(a)
            znew.append(res)
        # transpose back
        for i in xrange(len(tdata)):
            for j in xrange(len(tdata[0])):
                tdata[i][j] = znew[j][i]
        cdata = tdata

    ans = ""
    if flat_check(cdata) == 0:
        for r in xrange(len(data)):
            for c in xrange(len(data[0])):
                if data[r][c] == "?":
                    ans += "{}\n".format(cdata[r][c])
    else:
        ans += "NO\n"
    answer += ans + "\n"
print answer.strip("\n")