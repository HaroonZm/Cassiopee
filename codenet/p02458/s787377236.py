import sys
import bisect
nq = int(input())
lines = sys.stdin.readlines()
ans = [None] * nq
arr = []
for i in range(nq):
    q, *arg = lines[i].split()
    x = int(arg[0])
    l_idx = bisect.bisect_left(arr, x)
    r_idx = bisect.bisect_right(arr, x)
    if q == '0':    # insert x
        arr.insert(l_idx, x)
        ans[i] = str(len(arr))
    elif q == '1':   # find x
        ans[i] = r_idx - l_idx
    elif q == '2':           # delete x
        arr[l_idx:r_idx] = []
    else:                   # dump L R
        r_idx = bisect.bisect_right(arr, int(arg[1]))
        ans[i] = '\n'.join(map(str, arr[l_idx:r_idx])) if l_idx != r_idx else None
    #print(q, *arg, '\t', arr, '\t', ans[i])

[print(x) for x in ans if x is not None]