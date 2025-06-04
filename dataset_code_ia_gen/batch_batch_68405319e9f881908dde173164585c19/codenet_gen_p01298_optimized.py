import sys

for line in sys.stdin:
    N, L = map(int, line.split())
    if N == 0 and L == 0:
        break
    schedules = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    # We want to find minimal pump speed P so that tank never empties
    # Tank capacity = L, initially full
    # Water consumption is piecewise constant, no overlap between schedules
    # Between schedules consumption is zero
    # Define function to check if given pump speed is sufficient
    # The tank volume changes by (P - consumption) * duration in each period
    # We track minimum tank volume during the day; it must never go below 0
    
    def can(pump):
        volume = L
        min_volume = L
        prev_t = 0
        for s, t, u in schedules:
            # no consumption between prev_t and s
            # volume increases at rate pump for s - prev_t time
            volume = min(L, volume + (s - prev_t) * pump)
            # consumption period
            volume += (t - s) * (pump - u)
            if volume < 0:
                return False
            prev_t = t
        # after last schedule to end of day
        volume = min(L, volume + (86400 - prev_t) * pump)
        return volume >= 0
    
    left, right = 0.0, 1e7
    for _ in range(100):
        mid = (left + right) / 2
        if can(mid):
            right = mid
        else:
            left = mid
    print("%.6f" % right)