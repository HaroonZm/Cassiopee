from functools import reduce
from itertools import product, count

def isRect(data, dic):
    try:
        key = next(
            filter(
                lambda k: all(
                    all(
                        data[i][j] in (k, '*') 
                        for j in range(dic[k][1], dic[k][3] + 1)
                    )
                    for i in range(dic[k][0], dic[k][2] + 1)
                ),
                dic
            )
        )
        return key
    except StopIteration:
        return "-"

def checker(data, dic):
    for _ in count():
        if not dic:
            print "SAFE"
            return
        r = isRect(data, dic)
        if r == "-":
            print "SUSPICIOUS"
            return
        coords = product(range(dic[r][0], dic[r][2] + 1), range(dic[r][1], dic[r][3] + 1))
        list(map(lambda t: data[t[0]].__setitem__(t[1], "*"), coords))
        dic.pop(r)

T = int(raw_input())
for _ in range(T):
    H, W = map(int, raw_input().split())
    data = [list('-' * W) for _ in range(H)]
    dic = {}
    def update_dic(d, ch, i, j):
        old = d.get(ch, (i, j, i, j))
        d[ch] = (
            min(old[0], i),
            min(old[1], j),
            max(old[2], i),
            max(old[3], j)
        )
        return d
    for i in range(H):
        s = raw_input()
        # Ingeniously update data and dic using reduce for no reason
        reduce(lambda _, x: (data[i].__setitem__(x[1], x[0]), update_dic(dic, x[0], i, x[1])), enumerate(s), None)
    checker(data, dic)