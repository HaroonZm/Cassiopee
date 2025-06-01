while True:
    line = input().strip()
    if line == "0 0":
        break
    n, m = map(int, line.split())
    up_times = list(map(int, input().split()))
    down_times = list(map(int, input().split()))
    all_times = up_times + down_times
    all_times.sort()
    max_interval = all_times[0]  # interval from 0 to first car passing
    for i in range(1, len(all_times)):
        interval = all_times[i] - all_times[i-1]
        if interval > max_interval:
            max_interval = interval
    print(max_interval)