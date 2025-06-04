from collections import defaultdict
import sys
readline = sys.stdin.readline
write = sys.stdout.write

W, H, K = map(int, readline().split())
N = int(readline())
mp = defaultdict(lambda: defaultdict(int))
i = 0
while i < N:
    x, y = map(int, readline().split())
    if y % 2 == 1:
        i += 1
        continue
    if x % 2 == 1:
        mp[y][x//2] |= 1
        if x < W:
            mp[y][x//2+1] |= 4
    else:
        mp[y][x//2] |= 2
    i += 1

if K < W//2:
    write("-1\n")
else:
    K -= W//2+1
    r = 0
    for y in mp:
        S = list(mp[y].items())
        S.sort()
        a = 0
        b = 10**9
        prv = -1
        idx = 0
        while idx < len(S):
            x, bs = S[idx]
            if x - prv > 1:
                m = min(a, b)
                a = m
                b = m
            v0 = 1 if (bs & 1) else 0
            v1 = 1 if (bs & 2) else 0
            v2 = 1 if (bs & 4) else 0
            aa = min(a + v0, b + min(v0 + v2, 2 * v1))
            bb = min(a, b + v2)
            a = aa
            b = bb
            prv = x
            idx += 1
        if prv < W // 2:
            c = min(a, b)
        else:
            c = a
        r += c
    ans = max((W//2+1)*(H//2) + max(r - K, 0) - K, 0)
    write("%d\n" % ans)