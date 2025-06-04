def parse_time(t):
    h = t // 100
    m = t % 100
    return h * 60 + m

def format_time(m):
    h = m // 60
    mm = m % 60
    return h * 100 + mm

while True:
    parts = input().split()
    if len(parts) < 3:
        break
    n, p, q = parts
    n = int(n)
    p = int(p)
    q = int(q)
    if n == 0 and p == 0 and q == 0:
        break

    start = parse_time(p)
    end = parse_time(q)

    # For each channel, we will store a list of commercials as (start,end) in minutes
    channels = []
    for _ in range(n):
        k = int(input())
        commercials_times = list(map(int, input().split()))
        commercials = []
        for i in range(k):
            c_start = parse_time(commercials_times[2*i])
            c_end = parse_time(commercials_times[2*i+1])
            commercials.append((c_start, c_end))
        channels.append(commercials)

    # For each channel, create a list of free intervals (no commercial) within [start,end]
    free_intervals = []
    for comms in channels:
        free = []
        current_start = start
        for c_start, c_end in comms:
            if c_start > current_start:
                free.append((current_start, min(c_start, end)))
            current_start = max(current_start, c_end)
        if current_start < end:
            free.append((current_start, end))
        free_intervals.append(free)

    # We want to find the longest interval [T1, T2] with start <= T1 < T2 <= end,
    # where at any time t in [T1,T2), there is a channel with no commercial there,
    # AND we can switch channels only at times when intervals end/start (no mid interval switching)
    # So we consider all time points where intervals start and end
    points = set([start,end])
    for frees in free_intervals:
        for s,e in frees:
            points.add(s)
            points.add(e)
    points = sorted(points)

    # For each channel and each time point, build a list to know if channel is free at time interval points[i] to points[i+1]
    # Mark dp array: dp[i][c] will store the max length of continuous watching till points[i], ending on channel c
    # He can switch channel only at points[i] time instant and only if both intervals share that instant (no commercial)
    dp = [ [0]*n for _ in range(len(points))]

    # Initialize dp at start time: if channel free at start interval, dp=0 else -1 (means no watching)
    for c in range(n):
        # Check if channel c is free starting at points[0]
        is_free = False
        for (fs,fe) in free_intervals[c]:
            if fs <= points[0] < fe:
                is_free = True
                break
        if is_free:
            dp[0][c] = 0
        else:
            dp[0][c] = -1

    max_duration = 0

    for i in range(len(points)-1):
        length = points[i+1] - points[i]
        for c in range(n):
            if dp[i][c] < 0:
                continue
            # Check if channel c is free in interval [points[i], points[i+1])
            can_continue_same = False
            for (fs,fe) in free_intervals[c]:
                if fs <= points[i] and points[i+1] <= fe:
                    can_continue_same = True
                    break
            if not can_continue_same:
                # Can't continue on same channel
                dp[i+1][c] = max(dp[i+1][c], -1)
            else:
                # Continue on same channel
                dp[i+1][c] = max(dp[i+1][c], dp[i][c] + length)
            # Try switch from other channels
            for cc in range(n):
                if cc == c:
                    continue
                if dp[i][cc] < 0:
                    continue
                # can switch only if channel c is free at [points[i], points[i+1]) and channel cc was free at points[i]
                can_switch = False
                for (fs,fe) in free_intervals[c]:
                    if fs <= points[i] and points[i+1] <= fe:
                        can_switch = True
                        break
                if can_switch:
                    dp[i+1][c] = max(dp[i+1][c], dp[i][cc] + length)
        # Update max duration at i+1
        for c in range(n):
            if dp[i+1][c] > max_duration:
                max_duration = dp[i+1][c]

    print(max_duration)