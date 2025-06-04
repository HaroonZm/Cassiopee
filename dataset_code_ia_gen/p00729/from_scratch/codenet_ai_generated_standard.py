import sys
import bisect

def merge_intervals(intervals):
    merged = []
    for start, end in sorted(intervals):
        if merged and merged[-1][1] >= start:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

def interval_overlap(interval, start, end):
    s, e = interval
    if e <= start or s >= end:
        return 0
    return min(e, end) - max(s, start)

input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    r = int(input())
    logins = {}  # (pc) -> (student, login_time)
    usage = {m: [] for m in range(1, M+1)}
    for _ in range(r):
        t, n, m, s = map(int, input().split())
        if s == 1:  # login
            logins[n] = (m, t)
        else:  # logout
            stu, tin = logins.pop(n)
            usage[stu].append([tin, t])
    # merge intervals per student
    for m in usage:
        usage[m] = merge_intervals(usage[m])
    q = int(input())
    for _ in range(q):
        ts, te, m = map(int, input().split())
        intervals = usage.get(m, [])
        total = 0
        # intervals sorted, can binary search for start
        idx = bisect.bisect_left(intervals, [ts, ts])
        # check previous interval as well
        if idx > 0:
            idx -= 1
        for i in range(idx, len(intervals)):
            s, e = intervals[i]
            if s >= te:
                break
            if e <= ts:
                continue
            total += interval_overlap([s,e], ts, te)
        print(total)