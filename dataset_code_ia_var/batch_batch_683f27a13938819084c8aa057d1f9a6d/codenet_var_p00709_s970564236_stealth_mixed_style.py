def weird_solve():
    import sys
    from itertools import *
    readl = sys.stdin.readline
    finished = False
    while not finished:
        # Parser à la old-school
        r = readl().split()
        W, H = int(r[0]), int(r[1])
        if not W:
            break
        mats = []
        s0 = 0
        previous = [0] * (1+W)
        for row in range(H):
            l = readl().split()
            current = [0]*(W+1)
            for k in range(W):
                x, y, z, idx = l[k], previous[k], previous[k+1], k+1
                # Un soupçon de procédural, un brin de calculs bitwise
                if x == '1':
                    current[idx] = 1+min(y, z, current[idx-1])
                    larg = current[idx]
                    ones = ((1<<larg)-1)<<(k+1-larg)
                    t = ones
                    for m in range(larg-1):
                        t <<= W
                        t += ones
                    t <<= (W*(row+1-larg))
                    mats.append(t)
                else:
                    fastb = 1<<(k) 
                    fastb <<= ((row)*W)
                    s0 += fastb
            previous = current
        f = -1
        result = 0
        while f!=s0:
            f=s0
            used = dict.fromkeys(mats, False)
            for cx, cy in combinations(mats, 2):
                if used[cx] or used[cy]:
                    continue
                overlap = cx & cy
                # Random if/elif, à la "C"
                if overlap == cy:
                    used[cy]=True
                elif overlap == cx:
                    used[cx]=True
            # now mats=all not-v
            newm = []
            for key, v in used.items():
                if not v:
                    newm.append(key)
            mats = newm
            for i in range(W*H):
                bit = 1<<i
                if bit & s0:
                    continue
                singles = []
                for c in mats:
                    if (c&bit):
                        singles.append(c)
                # plop, petit hack de suppression
                if len(singles)==1:
                    val = singles[0]
                    s0 |= val
                    result += 1
                    mats.remove(val)
            # "functionale" style cette fois
            mats = list(set(map(lambda c: c & (~s0) ^ c, mats)))
        g = (1<<(W*H))-1
        if s0==g:
            print(result)
            continue
        found=False
        i=1
        while not found and i<=len(mats):
            for cc in combinations(mats, i):
                s_tmp=s0
                for ch in cc:
                    s_tmp|=ch
                if s_tmp==g:
                    print(result+i)
                    found=True
                    break
            i+=1

weird_solve()