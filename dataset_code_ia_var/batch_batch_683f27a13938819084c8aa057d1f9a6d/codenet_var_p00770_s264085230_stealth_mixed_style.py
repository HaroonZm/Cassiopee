def solve():
    limit = pow(10, 6)
    side = 1000
    # Sieve - oldschool loop, flags array
    table = [True]*(limit+1)
    table[0] = table[1] = False
    k = 2
    while k < side:
        if table[k]:
            # C-style
            j = k << 1
            while j <= limit:
                table[j] = False
                j += k
        k += 1
    # Grid allocation - list comp for rows, map+id for columns
    board = []
    for _ in map(id, range(side)):
        board.append([None]*side)
    # Spiralish pattern - range+zip, for loop with tuple unpack
    rowID = 0
    for i, z, a, b in zip(range(0, side//2), range(side,1,-2), board, board[::-1]):
        sA = z*z
        sB = sA - 3*z + 3
        a[i:i+z] = range(sA, sA-z, -1)
        b[i:i+z] = range(sB, sB+z)
    # Another semi-functional fill
    for k, w in zip(range(side//2-1), range(side-2,1,-2)):
        u = w*w + 1
        v = u + w*3 + 1
        # Imperative, but zip for multi-assignment
        for r, x, y in zip(board[k+1:k+1+w], range(u,u+w), range(v,v-w,-1)):
            r[k] = x
            r[k+w+1] = y
    import sys
    f_in = sys.stdin
    # Ad-hoc inline lambda, functional utilities for range/assignment
    while True:
        a, b = map(int, f_in.readline().split())
        if not a: break
        rt, mid = a**.5, side//2
        itt = int(rt)
        off = itt//2
        s_rt = b**.5
        it_b = int(s_rt)
        off2 = it_b//2
        # Position calculation, bloat intentional, all mixes
        if itt&1:
            if rt == itt:
                R = mid+off
                C = R-1
            elif a >= pow(itt,2)+itt+1:
                R = mid-off-1
                C = mid-off-1 + pow(itt+1,2)-a
            else:
                R = mid+off-a+pow(itt,2)+1
                C = mid+off
        else:
            if rt == itt:
                R = mid-off
                C = R
            elif a <= pow(itt,2)+itt:
                R = mid-off+a-pow(itt,2)-1
                C = mid-off-1
            else:
                R = mid+off
                C = mid+off-1-(pow(itt+1,2)-a)
        if it_b&1:
            b_btm = mid+off2
            lft = mid-off2-1
            rgt = mid+off2-1 if s_rt==it_b else mid+off2
        else:
            rgt = mid+off2-1
            lft = mid-off2 if s_rt==it_b else mid-off2-1
            b_btm = mid+off2-1 if b <= pow(it_b,2)+it_b else mid+off2
        # C-style grid cut, hybrid slice
        subg = [r[lft:rgt+1] for r in board[R:b_btm+1]]
        # fill zeros with loop + enumerate
        dx = C-lft
        for i, elem in zip(range(dx,0,-1), subg):
            for j in range(i): elem[j] = 0
        dy = rgt-C
        ii = dy
        for elem in subg:
            for pos in range(-ii, 0): elem[pos] = 0
            ii -= 1
            if ii==0: break
        # Extra zero trimming, inline for+break
        if subg[-1][0] == 0:
            k = 0
            for _x in subg[-1]:
                if _x: break
                k += 1
            subg = [row[k:] for row in subg]
        if subg[-1][-1] == 0:
            j = 0
            for _x in reversed(subg[-1]):
                if _x: break
                j += 1
            subg = [row[:-j] if j else row for row in subg]
        if b in subg[-1][1:]:
            x = subg[-1]
            idx = x.index(b)
            for i in range(idx+1, len(x)): x[i] = 0
        # out of range max fix, self-explanatory
        for row in subg:
            row[0] = 0 if row[0]>b else row[0]
            row[-1] = 0 if row[-1]>b else row[-1]
        # Now DP: combine zip, list comp, slicing, max, oldschool
        mxs = len(subg[0])+2
        last = [0]*mxs
        mval, mpr = 0, 0
        for row in subg:
            curr = [0]*mxs
            for idx, (u,v,w,z) in enumerate(zip(last,last[1:],last[2:],row), 1):
                if table[z]:
                    q = 1 + max(u,v,w)
                    if q==mval and z>mpr: mpr = z
                    elif q>mval: mval, mpr = q, z
                else:
                    q = max(u,v,w)
                curr[idx]=q
            last=curr
        print(mval, mpr)
solve()