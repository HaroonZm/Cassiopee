from sys import stdin
from itertools import permutations

def ticks_to_time(h, m, s):
    hh = h // 5
    mm = m
    ss = s
    return hh % 12, mm, ss

def format_time(t):
    h = t // 3600
    m = (t % 3600) // 60
    s = t % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def hand_to_second(tick):
    return tick * 6 % 360

def all_candidate_times(s, t, u):
    # Each hand has 60 positions (ticks)
    # hour hand ticks every 12 min = every 720 sec = 12 ticks (because 6 degrees per tick, 360 deg / 60 = 6 deg per tick)
    # minute hand ticks every 60 sec = every 1 tick
    # second hand ticks every 1 sec = every 1 tick
    # watch circumference corresponds to 360 deg, i.e., 60 ticks, each tick 6 deg
    # The angle in degrees for a hand tick pos: tick*6
    
    res = set()
    ticks = [s, t, u]
    for perm in permutations([0,1,2]):  # assign hands indexes to h,m,s
        hi, mi, si = perm
        # For each rotation r: 0 to 59
        for r in range(60):
            H = (ticks[hi] - r) % 60
            M = (ticks[mi] - r) % 60
            S = (ticks[si] - r) % 60
            
            # Validate if these ticks can represent a valid time:
            # hour hand moves every 12 minutes = every 12 ticks (every tick=6 deg)
            # but hour hand must be consistent with minute hand
            # Minute hand ticks every 60 sec = 1 tick
            # Hour hand angle = (360/60)*H = 6*H = should match hour base on minute and second hand
            
            # The possible time can be computed as seconds from 00:00:00
            
            # Hour hand must be consistent with minute hand:
            # Hour hand position = (hour % 12) * 5 + (minute // 12)
            # Or simply hour in ticks = hour * 5 + minute //12
            # But since hours and minutes are on the scale of 60 ticks
            
            # The hour hand ticks every 12 minutes, so every 12 ticks correspond to 1 full hour tick
            # The hour hand position in ticks should equal to (hour * 5 + minute // 12)
            # hour = floor(H/5), but H can be off as the hour hand moves gradually
            
            # We try all possible seconds 0..35999 (12*3600-1) is too large. Instead, infer hour, minute, second
            # But we can calculate second as S
            ss = S
            mm = M
            # Hour hand should be (hour * 5 + mm//12) % 60 == H
            for hour in range(12):
                expected_H = (hour * 5 + mm // 12) % 60
                if expected_H == H:
                    t_sec = hour * 3600 + mm * 60 + ss
                    res.add(t_sec % 43200)
    return res

def intersect_intervals(sets):
    # sets: list of sets of candidate seconds mod 43200
    # find shortest interval covering at least one candidate time per set
    # 43200 seconds = 12 hours
    # We'll gather all candidate times, mapping which watches cover them
    # Then find shortest interval covering all watches
    
    n = len(sets)
    points = []
    for i, s in enumerate(sets):
        for v in s:
            points.append((v, i))
    points.sort()
    
    # Two pointers to find minimal range covering all watches
    count = [0]*n
    inside = 0
    left = 0
    res_len = 43201
    res_range = (0,0)
    for right in range(len(points)):
        idx = points[right][1]
        count[idx] +=1
        if count[idx] == 1:
            inside +=1
        while inside == n:
            start = points[left][0]
            end = points[right][0]
            length = (end - start) if end >= start else (end + 43200 - start)
            if length < res_len or (length == res_len and start < res_range[0]):
                res_len = length
                res_range = (start, end)
            idxl = points[left][1]
            count[idxl] -=1
            if count[idxl] == 0:
                inside -=1
            left +=1
    # Check interval including wrap around 0
    if res_range[0] <= res_range[1]:
        start, end = res_range
    else:
        start, end = res_range
    return start, end

def main():
    lines = stdin.read().splitlines()
    i = 0
    while True:
        if i >= len(lines):
            break
        n = int(lines[i])
        i +=1
        if n == 0:
            break
        watches = []
        for _ in range(n):
            s,t,u = map(int, lines[i].split())
            i+=1
            watches.append((s,t,u))
        candidates = []
        for s,t,u in watches:
            c = all_candidate_times(s,t,u)
            candidates.append(c)
        start, end = intersect_intervals(candidates)
        # adjust end to inclusive (end time inclusive)
        end = (end + 0) % 43200
        print(f"{format_time(start)} {format_time(end)}")

if __name__=="__main__":
    main()