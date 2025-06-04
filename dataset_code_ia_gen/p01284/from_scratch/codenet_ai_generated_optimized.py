def min_caffeine():
    import sys
    input = sys.stdin.readline
    while True:
        T = int(input())
        if T == 0:
            break
        sleep = list(map(int, input().split()))
        N = int(input())
        interviews = [tuple(map(int, input().split())) for _ in range(N)]

        # DP state: key=cycle_day (0-based), value = min caffeine count
        from math import inf
        dp = {0:0}  # start day 1 of cycle with 0 caffeine

        for d, m in interviews:
            new_dp = {}
            for cday, ccount in dp.items():
                # Calculate actual sleep day and wake-up hour
                # Peter sleeps at midnight, sleeps sleep[cday] hours, so wakes at (sleep + 0)%24
                sleep_time = sleep[cday]
                wake_hour = (sleep_time) % 24
                # Check if he wakes before interview hour
                # If wake_hour <= m, ok, else may need caffeine

                if wake_hour <= m:
                    # no caffeine needed, update cday advancing by days waited
                    diff = d - (0 if ccount==0 else 0) # will adjust below
                    # But need to consider current day in cycle
                    # We only move forward here

                    # Actually must track now day number; so we must also track day pointer
                    # Since days > 1, we must track current day count separately

                    # So we should track in dp: (cycle_day, actual_day) => min caffeine
                    # It is necessary to track actual day to know where we are in cycle

                    # We'll change approach for correctness

                    pass
            # The above approach incomplete, do a full DP with (cycle_pos, day) keys

        # Rebuild solution with corrected approach:
def min_caffeine():
    import sys
    input = sys.stdin.readline
    while True:
        T = int(input())
        if T == 0:
            break
        sleep = list(map(int, input().split()))
        N = int(input())
        interviews = [tuple(map(int, input().split())) for _ in range(N)]
        interviews.sort()
        from math import inf

        # We track for each interview the minimal caffeine count considering current cycle position
        # State: (cycle_pos) minimal caffeine count
        # Also track day of last interview processed

        # Initial
        dp = {0:0}
        last_day = 0

        for d, m in interviews:
            new_dp = {}
            day_gap = d - last_day
            for cpos, ccount in dp.items():
                # Advance cycle position by day_gap mod T
                new_pos = (cpos + day_gap) % T
                # Calculate wake hour
                wake_hour = sleep[new_pos] % 24
                if wake_hour <= m:
                    # no caffeine
                    if new_pos not in new_dp or new_dp[new_pos] > ccount:
                        new_dp[new_pos] = ccount
                # try caffeine reset before this interview
                # caffeine resets cycle to day 1 with wake hour 1
                # wake_hour after caffeine = 1
                if 1 <= m:
                    if 0 not in new_dp or new_dp[0] > ccount + 1:
                        new_dp[0] = ccount + 1
            dp = new_dp
            last_day = d

        print(min(dp.values()))
min_caffeine()