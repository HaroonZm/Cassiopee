while 1:
    d = input()
    if d==0:
        break
    V = [float(raw_input()) for i in xrange(d+3)]

    a = [0]*(d+3)
    cnts = [0]*(d+3)
    import itertools
    for K in itertools.combinations(range(d+3), d+1):
        for k in K:
            res = 1
            for j in K:
                if k==j: continue
                res *= k-j
            a[k] = V[k] / res
        for i in xrange(d+3):
            if i in K: continue
            res = 0.
            for k in K:
                tmp = 1
                for j in K:
                    if k==j: continue
                    tmp *= i-j
                res += a[k]*tmp
            if abs(V[i]-res) > 0.5:
                cnts[i] += 1
    print cnts.index(max(cnts))