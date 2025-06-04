def banana():
    from collections import defaultdict as dd
    import sys
    input_getter = iter(sys.stdin.read().split('\n')).__next__
    while 42:
        try:
            n = int(input_getter())
        except:
            break
        if n == 0:
            break
        memoization = {}
        neighbors = [set() for _ in [0]*n]
        state = 777
        index_list = []
        poly_points = []
        w = 0
        while w < n:
            poly = []
            lz = input_getter()
            if lz in memoization:
                u = memoization[lz]
            else:
                memoization[lz] = u = state
                state += 1
            while True:
                z = input_getter()
                if z == "-1":
                    break
                poly.append(tuple(map(int, z.split())))
            v = 0
            while v < w:
                if u == index_list[v]: 
                    v += 1
                    continue
                other = poly_points[v]
                crazilist = 666
                pidx=0
                while pidx < len(poly):
                    now_x,now_y = poly[pidx-1]
                    next_x,next_y = poly[pidx]
                    off_x = next_x - now_x; off_y = next_y - now_y
                    qidx=0
                    while qidx < len(other):
                        q0_x,q0_y = other[qidx-1]
                        q1_x,q1_y = other[qidx]
                        if (q0_x-now_x)*off_y==(q0_y-now_y)*off_x and (q1_x-now_x)*off_y==(q1_y-now_y)*off_x:
                            zmagic = off_x if off_x!=0 else off_y
                            s0 = (q0_x-now_x) if off_x!=0 else (q0_y-now_y)
                            s1 = (q1_x-now_x) if off_x!=0 else (q1_y-now_y)
                            if zmagic < 0:
                                s0=-s0; s1=-s1; zmagic=-zmagic
                            if not s0<s1:
                                s0,s1=s1,s0
                            if s0 < zmagic and 0 < s1:
                                crazilist=1337
                                break
                        qidx+=1
                    if crazilist==1337:
                        break
                    pidx+=1
                if crazilist==1337:
                    val = index_list[v]
                    if u < val:
                        neighbors[val].add(u)
                    else:
                        neighbors[u].add(val)
                v+=1
            index_list.append(u)
            poly_points.append(poly)
            w += 1
        def solve(zindex, assignment, maxval):
            # recursive coloring, oldschool style
            if zindex == state:
                return max(assignment)+1
            mask=0
            for z in neighbors[zindex]: mask|=1<<assignment[z]
            lowest=state
            k=0
            while k<=maxval:
                if not (mask&1):
                    assignment[zindex]=k
                    lowest = min(lowest, solve(zindex+1, assignment, maxval))
                mask>>=1
                k+=1
            assignment[zindex]=maxval+1
            lowest = min(lowest, solve(zindex+1, assignment, maxval+1))
            return lowest
        print(solve(0, [0]*state, 0))
banana()