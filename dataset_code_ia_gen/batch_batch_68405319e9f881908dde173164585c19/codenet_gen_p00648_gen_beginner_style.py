def parse_time(weekday, start):
    # Convert weekday and start time to absolute minutes from start Sunday 00:00
    # Apply day overflow if hour >= 24
    hour = start // 100
    minute = start % 100
    day = weekday
    if hour >= 24:
        hour -= 24
        day += 1
    total_minutes = day * 24 * 60 + hour * 60 + minute
    return total_minutes

def overlap(s1, e1, s2, e2):
    # Check if two intervals overlap (end exclusive)
    return not (e1 <= s2 or e2 <= s1)

while True:
    N_line = input()
    if N_line == '0':
        break
    N = int(N_line)
    programs = {}
    start_end_times = {}
    for _ in range(N):
        line = input()
        name, wd, st = line.split()
        wd = int(wd)
        st = int(st)
        s = parse_time(wd, st)
        e = s + 30
        programs[name] = (s, e)
        start_end_times[name] = (s, e)
    P = int(input())
    favs = [input() for _ in range(P)]
    # Check if any two fav programs overlap
    impossible = False
    for i in range(P):
        for j in range(i+1, P):
            s1, e1 = programs[favs[i]]
            s2, e2 = programs[favs[j]]
            if overlap(s1, e1, s2, e2):
                impossible = True
                break
        if impossible:
            break
    if impossible:
        print(-1)
        # Consume next input if any? no, go to next dataset
        continue
    # Now, find max number programs including all favs, with no overlap
    # Idea: backtracking or greedy
    # Approach: sort all programs by end time
    # We'll implement a simple O(N^2) dp
    # We'll assign indices to programs
    progs_list = []
    name_to_idx = {}
    idx = 0
    for name in programs:
        progs_list.append((name, programs[name][0], programs[name][1]))
        name_to_idx[name] = idx
        idx += 1
    progs_list.sort(key=lambda x: x[2])  # sort by end time
    n = len(progs_list)
    # dp[i] = max number of programs watched considering first i programs in sorted order, includes favs
    # We will store also whether we can include favs among chosen programs
    # Because must include all favs, let's mark favs in a set
    fav_set = set(favs)
    # We'll build for each program which can be chosen and also keep track selected programs to check fav coverage
    # Since we only need maximum count, we can store dp as a dictionary keyed by bitmask representing which favs are covered
    # But fav size <= N up to 500 - So bitmask dp not feasible for big P (up to N=500)
    # So will go for a simple approach:
    # Greedy:
    # 1. First pick all fav programs, they do not overlap.
    # 2. Then add as many non-fav programs as possible that do not overlap with favs or others.

    # Let's start by combining all fav intervals and see their union
    # We'll mark minutes used by favs

    occupied = []
    for f in favs:
        occupied.append(programs[f])
    # Mark occupied minutes
    occupied_minutes = set()
    for s,e in occupied:
        for m in range(s,e):
            occupied_minutes.add(m)
    # Now, from progs_list in order of end, pick as many non-fav programs that do not overlap occupied
    count = len(favs)
    for name,s,e in progs_list:
        if name in fav_set:
            continue
        # check if overlaps occupied
        conflict = False
        for m in range(s,e):
            if m in occupied_minutes:
                conflict = True
                break
        if not conflict:
            # add this program
            count += 1
            for m in range(s,e):
                occupied_minutes.add(m)
    print(count)