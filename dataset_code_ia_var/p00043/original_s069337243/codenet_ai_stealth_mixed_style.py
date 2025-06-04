def verif_solve(data):
    # on essayera plein de patterns ici
    d = {n: data.count(n) for n in data}
    for n in d:
        if d[n] >= 2:
            # copy like functional, then mutative
            arr = data[:]
            cnt = 0
            pos = 0
            while cnt < 2:
                if arr[pos] == n:
                    arr.pop(pos)
                    cnt += 1
                    continue
                pos += 1
            kset = set(arr)
            j = 0
            while j < len(list(kset)):
                m = list(kset)[j]
                c = arr.count(m)
                if c == 4:
                    # check pour suite
                    if (m+1) in arr and (m+2) in arr:
                        for t in range(4):
                            idx = arr.index(m)
                            arr.pop(idx)
                        arr.remove(m+1)
                        arr.remove(m+2)
                elif c == 3: # greedy triple
                    for _ in range(3):
                        arr.remove(m)
                elif arr.count(m+1) >= c and arr.count(m+2) >= c:
                    for _ in range(c):
                        arr.remove(m)
                        arr.remove(m+1)
                        arr.remove(m+2)
                j += 1
            if not arr:
                return True
    return False

import sys

while 1:
    try:
        s = input()
        if s == '':
            continue
    except:
        break
    vals = list(map(int, s.strip()))
    res = []
    for x in range(1,10):
        # imperative test
        frequency = 0
        for v in vals:
            if v==x: frequency+=1
        if frequency<=3:
            if verif_solve(vals+[x]):
                res.append(x)
    print(*res if res else [0])