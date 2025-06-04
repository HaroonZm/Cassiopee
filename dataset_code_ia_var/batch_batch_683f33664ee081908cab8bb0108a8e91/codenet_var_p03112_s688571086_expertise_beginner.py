import sys
import bisect

input = sys.stdin.readline

a, b, q = map(int, input().split())
s = []
for i in range(a):
    s.append(int(input()))
t = []
for i in range(b):
    t.append(int(input()))

for i in range(q):
    x = int(input())

    sr = bisect.bisect_left(s, x)
    if sr == len(s):
        sr = sr - 1
    sl = sr - 1
    if sl < 0:
        sl = 0

    tr = bisect.bisect_left(t, x)
    if tr == len(t):
        tr = tr - 1
    tl = tr - 1
    if tl < 0:
        tl = 0

    def f(i, j):
        d1 = abs(x - s[i])
        d2 = abs(x - t[j])
        return min(d1, d2) + abs(t[j] - s[i])

    ans1 = f(sl, tl)
    ans2 = f(sl, tr)
    ans3 = f(sr, tl)
    ans4 = f(sr, tr)
    ans = min(ans1, ans2, ans3, ans4)
    print(ans)