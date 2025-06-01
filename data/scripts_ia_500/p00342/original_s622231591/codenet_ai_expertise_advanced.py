from sys import stdin
from operator import itemgetter

n, *a = map(int, stdin.read().split())
a.sort()
diffs = sorted(((a[i+1] - a[i], i) for i in range(n - 1)), key=itemgetter(0))

d0, i0 = diffs[0]
sum_cache = a[-1] + a[-2]
if i0 < n - 2:
    print(sum_cache / d0)
else:
    # Collect index flags for easier readability
    i1 = diffs[1][1]
    d1 = diffs[1][0]
    if i0 == n - 3:
        if i1 == n - 2:
            print(max(
                sum_cache / diffs[2][0],
                (a[-1] + a[-4]) / d0,
                (a[-3] + a[-4]) / d1
            ))
        else:
            print(max(
                sum_cache / d1,
                (a[-1] + a[-4]) / d0
            ))
    else:
        if i1 == n - 3:
            print(max(
                sum_cache / diffs[2][0],
                (a[-1] + a[-4]) / d1,
                (a[-3] + a[-4]) / d0
            ))
        else:
            print(max(
                sum_cache / d1,
                (a[-3] + a[-4]) / d0
            ))