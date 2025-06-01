import sys

def time_to_min(t):
    return (t // 100) * 60 + (t % 100)

def merge_intervals(intervals):
    intervals.sort()
    merged = []
    for start, end in intervals:
        if merged and merged[-1][1] >= start:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

for line in sys.stdin:
    if not line.strip():
        continue
    n, p, q = map(int, line.split())
    if n == 0 and p == 0 and q == 0:
        break
    p_min = time_to_min(p)
    q_min = time_to_min(q)
    free_intervals_all = []
    for _ in range(n):
        k = int(sys.stdin.readline())
        commercials = list(map(int, sys.stdin.readline().split()))
        intervals = []
        for i in range(0, 2*k, 2):
            start = time_to_min(commercials[i])
            end = time_to_min(commercials[i+1])
            # clip commercials inside p and q
            if end <= p_min or start >= q_min:
                continue
            intervals.append([max(start, p_min), min(end, q_min)])
        merged = merge_intervals(intervals)
        free_intervals = []
        prev = p_min
        for s,e in merged:
            if s > prev:
                free_intervals.append([prev, s])
            prev = max(prev, e)
        if prev < q_min:
            free_intervals.append([prev, q_min])
        free_intervals_all.append(free_intervals)

    import heapq

    # For each channel i, free_intervals_all[i] is list of free intervals sorted, non-overlapping
    # We want to find the longest chain starting at p_min and ending at or before q_min,
    # where intervals are contiguous in time by jumping channels between intervals.

    # We'll use a priority queue for Dijkstra-like process:
    # state: (neg_length, channel_index, interval_index)
    # length is current watched time

    # Initialize: from p_min, for each channel's first interval that starts at p_min
    # or before p_min, we can start watching from max(p_min, interval_start)
    # but interval must cover p_min
    heap = []
    dist = dict()
    for i, intervals in enumerate(free_intervals_all):
        for j, (s, e) in enumerate(intervals):
            if s <= p_min < e:
                length = e - p_min
                state = (i,j)
                dist[state] = length
                heapq.heappush(heap, (-length, i, j))
                break

    max_length = 0

    while heap:
        neg_len, i, j = heapq.heappop(heap)
        length = -neg_len
        state = (i,j)
        if dist[state] != length:
            continue
        max_length = max(max_length, length)
        _, end_i_j = free_intervals_all[i][j]
        # try to jump to any channel at time end_i_j
        t = end_i_j
        if t >= q_min:
            continue
        for c, intervals_c in enumerate(free_intervals_all):
            # binary search for interval in intervals_c starting at or before t and covering t
            lo, hi = 0, len(intervals_c)-1
            idx = -1
            while lo <= hi:
                mid = (lo+hi)//2
                s,e = intervals_c[mid]
                if s <= t < e:
                    idx = mid
                    break
                elif s > t:
                    hi = mid-1
                else:
                    lo = mid+1
            if idx == -1:
                continue
            s,e = intervals_c[idx]
            new_length = length + (e - t)
            new_state = (c, idx)
            if new_state not in dist or dist[new_state] < new_length:
                dist[new_state] = new_length
                heapq.heappush(heap, (-new_length, c, idx))

    print(max_length)