import math
while True:
    l = 0; r = []
    try:
        inp = map(int, raw_input().split())
        l = inp[0]
        r = inp[1:]
    except EOFError:
        break
    n = len(r)
    if 2*sum(r) <= l:
        print "OK"
    else:
        s = []
        if n>1:
            r.sort()
            for i in xrange(n/2):
                s = [r[i]] + s[::-1] + [r[-i-1]]
            if n&1:
                if abs(s[0]-r[n/2]) < abs(s[-1]-r[n/2]):
                    s.append(r[n/2])
                else:
                    s = [r[n/2]] + s
        else:
            s = r
        ans = s[0] + s[-1]
        for i in xrange(n-1):
            ans += 2*math.sqrt(s[i]*s[i+1])
        print "OK" if ans < 0.000000001+l else "NA"