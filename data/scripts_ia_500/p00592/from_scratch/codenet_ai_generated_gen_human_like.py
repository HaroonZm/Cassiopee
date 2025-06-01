def time_to_minutes(t):
    h = t // 100
    m = t % 100
    return h * 60 + m

while True:
    line = input().strip()
    if not line:
        continue
    n, p, q = map(int, line.split())
    if n == 0 and p == 0 and q == 0:
        break
    start = time_to_minutes(p)
    end = time_to_minutes(q)
    channel_free_intervals = []
    for _ in range(n):
        k = int(input())
        commercials = list(map(int, input().split()))
        # convert commercials intervals to minutes
        busy = []
        for i in range(k):
            c_start = time_to_minutes(commercials[2*i])
            c_end = time_to_minutes(commercials[2*i+1])
            busy.append((c_start, c_end))
        # complement intervals (free intervals) within [start, end]
        free = []
        current = start
        for b_start, b_end in busy:
            if b_start > current:
                free.append((current, b_start))
            current = max(current, b_end)
        if current < end:
            free.append((current, end))
        channel_free_intervals.append(free)

    max_watch = 0
    # We want the longest interval within [start,end] where
    # at every time instant, at least one channel is free.
    # Since student can shuffle channels at any time, the constraint is:
    # find the union of all free intervals across channels within [start,end]
    # and find the longest continuous interval in the union.
    # So first, combine all free intervals from all channels.
    all_free = []
    for free_list in channel_free_intervals:
        all_free.extend(free_list)
    # merge intervals
    all_free.sort()
    merged = []
    for interval in all_free:
        if not merged:
            merged.append(interval)
        else:
            last_start, last_end = merged[-1]
            curr_start, curr_end = interval
            if curr_start <= last_end:  # overlapping or contiguous
                merged[-1] = (last_start, max(last_end, curr_end))
            else:
                merged.append(interval)
    # find max interval length
    for s,e in merged:
        length = e - s
        if length > max_watch:
            max_watch = length
    print(max_watch)