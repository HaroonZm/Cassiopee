import bisect

n, l, t = map(int, input().split())
xw = [list(map(int, input().split())) for _ in range(n)]
clockwise = []
anticlockwise = []
for key in range(n):
    x, w = xw[key]
    if w == 1:
        clockwise.append((x, key))
    else:
        anticlockwise.append((x, key))
clockwise.sort()
anticlockwise.sort()
len_c = len(clockwise)
len_a = len(anticlockwise)
ans = [None] * n
for key in range(n):
    x, w = xw[key]
    if w == 1:
        # find number of anticlockwise circles this clockwise particle will cross
        p1 = bisect.bisect_right(anticlockwise, ((2*t + x) % l, 1000000))
        p2 = bisect.bisect_right(anticlockwise, (x, 0))
        tmp = p1 - p2
        lap = (x + 2*t) // l
        num = (key + tmp + lap * len_a) % n
        ans[num] = (x + t) % l
    else:
        # find number of clockwise circles this anticlockwise particle will cross
        p1 = bisect.bisect_left(clockwise, (x, -1))
        p2 = bisect.bisect_left(clockwise, ((x - 2*t) % l, -1))
        tmp = p1 - p2
        lap = (x - 2*t) // l
        num = (key - tmp + lap * len_c) % n
        ans[num] = (x - t) % l
i = 0
while i < n:
    print(ans[i])
    i += 1