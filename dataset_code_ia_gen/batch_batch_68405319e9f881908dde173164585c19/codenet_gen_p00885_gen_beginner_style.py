def can_capture_all(n, balloons):
    # vehicle starts at position 0 with no balloons, time 0, distance 0
    pos = 0
    time = 0
    dist = 0
    carrying = []
    carried = 0
    
    for i in range(n):
        pi, ti = balloons[i]
        # before going to catch balloon i, if carrying 3 balloons, must return to house first to drop
        while len(carrying) == 3:
            # return to house
            d = abs(pos - 0)
            # speed with 3 balloons is 4 units time per distance
            need_time = 4 * d
            time += need_time
            dist += d
            pos = 0
            carrying = []
        
        # now move to balloon position
        d = abs(pi - pos)
        speed = len(carrying) + 1
        need_time = d * speed
        available_time = ti - time
        if need_time > available_time:
            return False, i+1
        
        time += need_time
        dist += d
        pos = pi
        
        # catch balloon (no time)
        carrying.append((pi, ti))
    
    # after catching last balloon(s), return to house to store them (can be 1-3 balloons)
    while len(carrying) > 0:
        d = abs(pos - 0)
        speed = len(carrying) + 1
        need_time = d * speed
        time += need_time
        dist += d
        pos = 0
        carrying = []
    
    return True, dist


while True:
    n = int(input())
    if n == 0:
        break
    balloons = []
    for _ in range(n):
        p, t = map(int, input().split())
        balloons.append((p,t))
    can_capture, val = can_capture_all(n, balloons)
    if can_capture:
        print("OK", val)
    else:
        print("NG", val)