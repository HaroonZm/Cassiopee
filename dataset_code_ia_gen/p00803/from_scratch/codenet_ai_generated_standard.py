MAX = 151200

cubes = [i**3 for i in range(54)]  # 53^3=148877 < 151200 < 54^3
tetra = [n*(n+1)*(n+2)//6 for n in range(97)]  # 96*97*98/6=151096 < 151200 < 97*98*99/6

sums = set()
for c in cubes:
    for t in tetra:
        s = c + t
        if s > MAX:
            break
        sums.add(s)

sums = sorted(sums)

import sys
for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    # binary search for largest value <= n
    l, r = 0, len(sums)-1
    ans = 0
    while l <= r:
        m = (l + r) // 2
        if sums[m] <= n:
            ans = sums[m]
            l = m + 1
        else:
            r = m -1
    print(ans)