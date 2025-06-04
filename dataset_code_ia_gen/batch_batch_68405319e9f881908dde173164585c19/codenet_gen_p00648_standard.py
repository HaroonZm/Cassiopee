import sys

def to_minutes(weekday, start):
    h = start // 100
    m = start % 100
    day = weekday
    if h >= 24:
        h -= 24
        day += 1
    return day * 1440 + h * 60 + m

def overlap(a_start, a_end, b_start, b_end):
    return not (a_end <= b_start or b_end <= a_start)

for line in sys.stdin:
    line=line.strip()
    if line=='0':
        break
    N = int(line)
    programs = {}
    times = []
    for _ in range(N):
        name, wd, st = sys.stdin.readline().split()
        wd=int(wd)
        st=int(st)
        start = to_minutes(wd, st)
        end = start + 30
        programs[name] = (start, end)
        times.append((start,end,name))
    P = int(sys.stdin.readline())
    favs = [sys.stdin.readline().strip() for _ in range(P)]
    # check if favs overlap
    fav_intervals = [programs[f] for f in favs]
    conflict = False
    fav_intervals.sort()
    for i in range(len(fav_intervals)-1):
        if overlap(fav_intervals[i][0], fav_intervals[i][1], fav_intervals[i+1][0], fav_intervals[i+1][1]):
            conflict = True
            break
    if conflict:
        print(-1)
        continue
    # filter compatible programs (no overlaps with favs)
    # also fix all program list
    fav_set = set(favs)
    fav_min = min(i[0] for i in fav_intervals)
    fav_max = max(i[1] for i in fav_intervals)
    # if favs overlap with each other no answer -> done above
    # For max number including favs:
    # We must select all favs, and we can add other programs that don't overlap with each other and with favs.
    # So first exclude programs overlapping with any fav fav_program
    def conflict_with_favs(p):
        for fs,fe in fav_intervals:
            if overlap(p[0],p[1],fs,fe):
                return True
        return False
    candidates = []
    for st,en,name in times:
        if name in fav_set:
            candidates.append((st,en,name,True))
        elif not conflict_with_favs((st,en)):
            candidates.append((st,en,name,False))
    # check if fav programs among candidates don't conflict anymore
    # now we want max set including all fav (marked True), from candidates without overlap
    # classic interval scheduling with forced intervals:
    # First sort by end time
    candidates.sort(key=lambda x:x[1])
    # We do dp indexed by sorted candidates:
    # For each candidate i, dp[i] = maximum number of programs watchable <= i including all favs
    # But forced to include all favs, so dp state must track which favs are included so far
    # Since P can be up to 500, tracking subset is impossible
    # Better approach:
    # Since fav programs do not overlap each other (already checked),
    # merge them into one single set, intervals fixed
    # Let's do interval scheduling on candidates including favs:
    # First remove non-fav programs conflicting with favs (done),
    # Then try to select all favs plus as many non-favs as possible avoiding overlap
    # Because favs don't overlap, schedule them first, then add non-favs in gaps
    # We can solve as follows:
    # Collect all fav intervals in sorted order by end time
    fav_sorted = sorted(fav_intervals,key=lambda x:x[1])
    # Now intervals: cover the line with fav intervals, between fav intervals we can add others if no conflicts
    # Extract the overall covered time by favs, and intervals between favs:
    # We'll do interval scheduling in each gap between fav intervals including left and right segments
    # plus count favs:
    total = len(fav_sorted)
    # get all candidates intervals which do not overlap any fav intervals (already filtered)
    non_fav_cands = [c for c in candidates if not c[3]]
    # add sentinel fav intervals at start and end
    starts = [-10**9]+[f[1] for f in fav_sorted]
    ends = [f[0] for f in fav_sorted]+[10**9]
    # for intervals between favs i and i+1, collect non-fav candidates fully inside (start>=ends[i], end<=starts[i+1])
    # then do interval scheduling in each gap
    for i in range(len(fav_sorted)+1):
        gap_candidates = []
        L = starts[i]
        R = ends[i]
        for st,en,name,_ in non_fav_cands:
            if st>=R and en<=L:
                # This never happens, since R > L for i in [0,len]
                # Actually intervals between favs are (fav_sorted[i-1].end, fav_sorted[i].start)
                # Correction: starts = [f[1]], ends=[f[0]], saved in order, possibly starts[i] < ends[i]
                # We fix swapped:
                # Actually starts[i]=fav end times, ends[i]=fav start times, so starts[i] > ends[i] which is reversed
                # fix: swap starts and ends usage
                pass
        # Instead:
        # Between fav intervals i-1 and i:
        # We define prev_end = fav_sorted[i-1].end if i>0 else -inf
        # next_start = fav_sorted[i].start if i<len(fav_sorted) else +inf
        # so valid intervals are [prev_end, next_start)
    gaps = []
    for i in range(len(fav_sorted)+1):
        prev_end = fav_sorted[i-1][1] if i>0 else -10**9
        next_start = fav_sorted[i][0] if i<len(fav_sorted) else 10**9
        gaps.append( (prev_end,next_start) )
    res = total
    # For each gap find max number of compatible non-fav programs inside gap
    # classic interval scheduling
    for L,R in gaps:
        # filter non_fav candidates inside [L,R)
        cand_in_gap = [ (en, st) for st,en,_,_ in non_fav_cands if st>=L and en<=R]
        cand_in_gap.sort()
        count = 0
        last_end = L
        for en, st in cand_in_gap:
            if st>=last_end:
                count+=1
                last_end = en
        res+=count
    print(res)