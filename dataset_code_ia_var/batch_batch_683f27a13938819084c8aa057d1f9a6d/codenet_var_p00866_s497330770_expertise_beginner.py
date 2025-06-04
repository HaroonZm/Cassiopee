import sys
import collections
import bisect

sys.setrecursionlimit(10000000)
inf = 10 ** 20

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def I():
    return int(sys.stdin.readline())

def to_time(i):
    h = i // 3600
    m = (i // 60) % 60
    s = i % 60
    return "%02d:%02d:%02d" % (h, m, s)

def kf(e):
    alist = []
    for i in range(3):
        lst = []
        for j in range(3):
            diff = (e[j] - e[i]) % 60
            lst.append(diff)
        lst.sort()
        alist.append(lst)
    return tuple(min(alist))

def main():
    rr = []
    d = collections.defaultdict(list)

    # Precompute all times mapping
    for h in range(24):
        for m in range(60):
            for s in range(60):
                a = h * 5 + m // 12
                k = kf([a, m, s])
                seconds = h * 3600 + m * 60 + s
                d[k].append(seconds)

    while True:
        n = I()
        if n == 0:
            break
        times = []
        for _ in range(n):
            times.append(LI())
        cs = []
        for i in range(n):
            k = kf(times[i])
            arr = d[k][:]
            arr.append(inf)
            cs.append(arr)
        mr = inf
        mi = -1
        for i in range(24*60*60):
            t = i
            for j in range(n):
                idx = bisect.bisect_left(cs[j], i)
                c = cs[j][idx]
                if t < c:
                    t = c
            tr = t - i
            if mr > tr:
                mr = tr
                mi = i
        ans = to_time(mi) + " " + to_time(mi + mr)
        rr.append(ans)
    return "\n".join(rr)

print(main())