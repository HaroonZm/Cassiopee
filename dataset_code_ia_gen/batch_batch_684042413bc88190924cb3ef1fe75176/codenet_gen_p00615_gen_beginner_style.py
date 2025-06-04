while True:
    line = input()
    if line == '':
        break
    n, m = map(int, line.split())
    if n == 0 and m == 0:
        break
    tl = list(map(int, input().split()))
    tr = list(map(int, input().split()))

    times = tl + tr
    times.sort()

    end_time = max(times)
    max_gap = times[0]  # gap from 0 to first passing time
    for i in range(1, len(times)):
        gap = times[i] - times[i-1]
        if gap > max_gap:
            max_gap = gap
    # gap from last passing time to end_time is zero, because end_time = max(times)
    print(max_gap)