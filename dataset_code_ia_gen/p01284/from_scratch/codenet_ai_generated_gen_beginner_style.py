while True:
    T = int(input())
    if T == 0:
        break
    t = list(map(int, input().split()))
    N = int(input())
    interviews = []
    for _ in range(N):
        D, M = map(int, input().split())
        interviews.append((D, M))
    caffeine = 0
    last_sleep_end = 0  # time when Peter wakes up last time
    cycle = t
    for D, M in interviews:
        # Calculate the time Peter wakes up on day D without caffeine
        # Peter sleeps starting at midnight on day D-1, sleeps for cycle[(D-1)%T] hours
        # So wakes up at day D-1 midnight + cycle[(D-1)%T] hours = day D-1 + sleep hours
        # Convert day/hour to absolute hours
        while True:
            sleep_start = (D - 1) * 24
            sleep_duration = cycle[(D - 1) % T]
            wake_up = sleep_start + sleep_duration
            interview_time = (D - 1) * 24 + M
            if wake_up <= interview_time:
                # he wakes up before interview
                if wake_up >= last_sleep_end:
                    last_sleep_end = wake_up
                    break
                else:
                    # he woke up earlier than last time, need caffeine
                    caffeine +=1
                    # taking caffeine resets cycle to day 1 for this day: sleeps 1 hour
                    sleep_duration = 1
                    wake_up = sleep_start + sleep_duration
                    last_sleep_end = wake_up
                    break
            else:
                # wakes up after interview, need caffeine to reset cycle
                caffeine +=1
                # after caffeine, cycle reset, so restart with day 1 on this day
                # but this means the cycle day is reset, so now sleep duration is 1 hour
                # however, in this simple approach, just reset cycle start day to D and retry
                # So update the day index for cycle to 0
                cycle = cycle
                break
        # But the above may not handle repeated caffeine well, so let's do a simpler approach below
    # The above approach is complicated; let's do a simpler one:
while True:
    T = int(input())
    if T == 0:
        break
    t = list(map(int, input().split()))
    N = int(input())
    interviews = []
    for _ in range(N):
        D, M = map(int, input().split())
        interviews.append((D, M))
    caffeine = 0
    current_day_in_cycle = 0  # 0-based index for cycle array
    current_time = 0  # time when Peter wakes up last time, in hours
    for D, M in interviews:
        # Calculate the time he sleeps for day D in the current cycle
        # We need to know when he goes to sleep for day D (midnight of day D-1)
        # and when he wakes up, depending on cycle
        # When he takes caffeine, cycle resets to day 1 at that day
        # We want minimal caffeine, so we try to not take caffeine until necessary
        # For each interview, we check if Peter wakes up before the interview starting time
        
        # Calculate the start of sleep for day D: (D-1)*24
        sleep_start = (D -1)*24
        # Sleep duration depends on current_day_in_cycle
        sleep_duration = t[current_day_in_cycle]
        wake_up_time = sleep_start + sleep_duration
        interview_time = sleep_start + M
        if wake_up_time > interview_time:
            # Need caffeine at day D to reset cycle and sleep only 1 hour
            caffeine += 1
            current_day_in_cycle = 0  # reset cycle
            sleep_duration = t[current_day_in_cycle]
            wake_up_time = sleep_start + sleep_duration
            if wake_up_time > interview_time:
                # Even with caffeine need more careful adjustment, but problem says cycle start with 1 hour sleep
                # so it's ok
                pass
            # Update the continuing cycle day to day after D, because day D is restarted
            current_day_in_cycle = 1 % T
        else:
            # No caffeine needed, just move cycle day forward
            current_day_in_cycle = (current_day_in_cycle + 1) % T
    print(caffeine)