def main():
    import sys
    moves = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    neighbors = {}
    for r0,c0 in moves:
        neighbors[(r0,c0)] = []
        for dr,dc in [(0,1),(0,2),(0,-1),(0,-2),(1,0),(2,0),(-1,0),(-2,0),(0,0)]:
            nr,nc = r0+dr,c0+dc
            if 0<=nr<=2 and 0<=nc<=2:
                neighbors[(r0,c0)].append((nr,nc))
    # area indices in 4x4 from 0..15, row-wise
    def get_covered(r,c):
        # cloud top-left corner at (r,c), covers 2x2 cells
        return {r*4+c, r*4+c+1, (r+1)*4+c, (r+1)*4+c+1}
    # central cells for day0 rain
    central = {5,6,9,10}
    for line in sys.stdin:
        line=line.strip()
        if line=="0":
            break
        N = int(line)
        sch = []
        for _ in range(N):
            sch.append(list(map(int,sys.stdin.readline().split())))
        # For day 0, rain on central anyway
        # For next days, we choose cloud position (r,c) in moves set at start of day
        # Conditions:
        # - Markets/festivals = 1 -> area must be sunny that day (not under cloud)
        # - All areas must get rain at least once every 7 days (max 6 days no rain)
        # Between days, cloud moves max 2 steps horizontal or vertical or stays
        # Represent cloud positions by their top-left corner (r,c) with r,c in 0..2
        # State: day, cloud_position, for each area count of consecutive no rain days (max 6)
        # To reduce state size store last day rain count since last rain for each area

        # Precompute for each cloud position which areas get rain (cloud covers them)
        rain_areas = {}
        for pos in moves:
            rain_areas[pos] = get_covered(pos[0],pos[1])

        from collections import deque
        # initial state day=0, cloud_pos=(1,1) because central cells (5,6,9,10) covered
        # consecutive no rain count 0 for central cells, maximum 6 for others (since rain yesterday)
        start_pos = (1,1) # top-left corner covering rows 1-2 and cols 1-2 covers indices 5,6,9,10
        # initialize no rain counters
        no_rain = [0]*16
        for i in range(16):
            if i in central:
                no_rain[i]=0
            else:
                no_rain[i]=6 # day before period rain all

        # use BFS or DP with pruning
        # state: day,cloud_pos,no_rain tuple
        # to keep memory reasonable truncate no_rain counts at 6
        visited = {}
        q = deque()
        key = (0,start_pos,tuple(no_rain))
        visited[key]=True
        q.append(key)
        while q:
            day,pos,nr = q.popleft()
            if day==N:
                print(1)
                break
            today_sch = sch[day]
            today_rain = rain_areas[pos]
            # Check festivals/market areas sunny
            # areas with 1 must not be under rain cloud
            ok = True
            for i,v in enumerate(today_sch):
                if v==1 and i in today_rain:
                    ok=False
                    break
            if not ok:
                continue
            # Update no_rain counters
            new_nr = []
            for i in range(16):
                if i in today_rain:
                    new_nr.append(0)
                else:
                    nr_i = nr[i]+1
                    if nr_i>6:
                        nr_i=7
                    new_nr.append(nr_i)
            # If any area has >6 no rain days, discard state
            if any(x>6 for x in new_nr):
                continue
            # Move cloud for next day day+1
            for npos in neighbors[pos]:
                nkey = (day+1,npos,tuple(new_nr))
                if nkey not in visited:
                    visited[nkey]=True
                    q.append(nkey)
        else:
            print(0)
if __name__=="__main__":
    main()