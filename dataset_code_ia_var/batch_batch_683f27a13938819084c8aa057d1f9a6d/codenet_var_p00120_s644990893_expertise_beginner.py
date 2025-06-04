import math

while True:
    try:
        line = raw_input()
        values = line.split()
        l = int(values[0])
        r = []
        for v in values[1:]:
            r.append(int(v))
    except EOFError:
        break

    n = len(r)
    if 2 * sum(r) <= l:
        print "OK"
    else:
        s = []
        if n > 1:
            r.sort()
            for i in range(n // 2):
                s = [r[i]] + s[::-1] + [r[-i-1]]
            if n % 2 == 1:
                mid = r[n // 2]
                if abs(s[0] - mid) < abs(s[-1] - mid):
                    s.append(mid)
                else:
                    s = [mid] + s
        else:
            s = r[:]

        ans = s[0] + s[-1]
        for i in range(n - 1):
            ans = ans + 2 * math.sqrt(s[i] * s[i+1])

        if ans < l + 0.000000001:
            print "OK"
        else:
            print "NA"