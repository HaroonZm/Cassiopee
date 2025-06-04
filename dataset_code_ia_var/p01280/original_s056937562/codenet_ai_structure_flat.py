from itertools import cycle

while True:
    n = int(input())
    if not n:
        break
    qs = {}
    i = 0
    while i < n:
        parts = input().split()
        d = int(parts[0])
        t = int(parts[1])
        q = [int(x) for x in parts[2:]]
        q = q[t:] + q[:t]
        if d not in qs:
            qs[d] = q
        else:
            q2 = qs[d]
            q3 = []
            j = 0
            while j < len(q):
                q3.append(q2[j] + q[j])
                j += 1
            qs[d] = q3
        i += 1
    L = 16 * 9 * 5 * 7 * 11
    ps = [13, 17, 19, 23, 1]
    psum = 0
    k = 0
    temp_ps = ps[:]
    while k < len(temp_ps):
        x = temp_ps[k]
        if x in qs:
            psum += max(qs[x])
            del qs[x]
        else:
            psum += max([0])
        k += 1
    vals = list(qs.values())
    if not vals:
        qmax = 0
    else:
        length = len(vals[0])
        m = len(vals)
        arr = []
        p = 0
        while p < L - 1:
            s = 0
            idx = 0
            while idx < m:
                s += vals[idx][p % length]
                idx += 1
            arr.append(s)
            p += 1
        qmax = max(arr)
    print(psum + qmax)