def swimming_jam():
    import sys
    for line in sys.stdin:
        n = int(line)
        if n == 0:
            break
        swimmers = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
        # Sort by pace ascending (faster first)
        swimmers.sort(key=lambda x: x[0])
        # Each swimmer's total swimming time = natural pace * 2 * laps
        # Due to blocking, the pace of a swimmer can't be faster than all swimmers in front.
        # So we propagate the max pace from front to back.
        max_pace = swimmers[0][0]
        total_time = 0
        for t, c in swimmers:
            if t > max_pace:
                t = max_pace
            else:
                max_pace = t
            total_time = max(total_time, t * 2 * c)
        print(total_time)
swimming_jam()