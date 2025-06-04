def to_minutes(t):
    h, m = divmod(t, 100)
    return h * 60 + m

def from_minutes(m):
    h = m // 60
    r = m % 60
    return h * 100 + r

while True:
    n, p, q = map(int, input().split())
    if n == 0 and p == 0 and q == 0:
        break
    start = to_minutes(p)
    end = to_minutes(q)
    free_intervals = []
    for _ in range(n):
        k = int(input())
        commercials = list(map(int, input().split()))
        comm_intervals = [(to_minutes(commercials[2*i]), to_minutes(commercials[2*i+1])) for i in range(k)]
        free = []
        prev = start
        for c_start, c_end in comm_intervals:
            if c_start > prev:
                free.append((prev, c_start))
            prev = max(prev, c_end)
        if prev < end:
            free.append((prev, end))
        free_intervals.append(free)

    # Create events for line sweep: (time, channel, type=START/END)
    # But better: aggregate all intervals with channel info and then do DP

    # Collect all interval endpoints for coordinate compression
    points = set()
    for ch in range(n):
        for s,e in free_intervals[ch]:
            points.add(s)
            points.add(e)
    points.add(start)
    points.add(end)
    points = sorted(points)
    idx_map = {v:i for i,v in enumerate(points)}

    # Build for each channel a list of free intervals marked in points indices
    channel_masks = [ [False]*(len(points)-1) for _ in range(n)]
    for ch in range(n):
        for s,e in free_intervals[ch]:
            si = idx_map[s]
            ei = idx_map[e]
            for i in range(si, ei):
                channel_masks[ch][i] = True

    length = [points[i+1]-points[i] for i in range(len(points)-1)]

    # DP[i][ch] = max length finishing at interval i on channel ch
    # We want to find max total length shuffling between channels without commercials.
    # Transition from i-1 to i: can switch channels or stay same.

    # Initialize dp for interval 0
    dp = [0]*n
    for ch in range(n):
        if channel_masks[ch][0]:
            dp[ch] = length[0]

    for i in range(1, len(points)-1):
        ndp = [0]*n
        for ch in range(n):
            if channel_masks[ch][i]:
                max_prev = 0
                for ch2 in range(n):
                    if dp[ch2]:
                        max_prev = max(max_prev, dp[ch2])
                # If no previous dp >0, max_prev=0 but still can start here only if free at this interval
                # but that will be accounted by dp[ch]=length[i] if its the first interval for that ch
                # Actually, to allow start in the middle, add length[i] itself
                ndp[ch] = max_prev + length[i]
        dp = ndp

    print(max(dp))