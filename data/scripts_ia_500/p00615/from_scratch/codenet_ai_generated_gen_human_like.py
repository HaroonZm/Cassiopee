while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    if n > 0:
        tl = list(map(int, input().split()))
    else:
        tl = []
    if m > 0:
        tr = list(map(int, input().split()))
    else:
        tr = []
    times = sorted(tl + tr)
    if not times:
        print(0)
        continue
    max_gap = times[0] - 0
    for i in range(1, len(times)):
        gap = times[i] - times[i-1]
        if gap > max_gap:
            max_gap = gap
    print(max_gap)