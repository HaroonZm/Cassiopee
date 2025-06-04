import sys
import math
input=sys.stdin.readline

WIDTH=100
HEIGHT=50
DEPTH=30
VOLUME=WIDTH*HEIGHT*DEPTH

D=int(input())
for _ in range(D):
    N=int(input())
    boards=[]
    for __ in range(N):
        b,h=map(int,input().split())
        boards.append((b,h))
    boards.sort()
    M=int(input())
    faucets=[]
    for __ in range(M):
        f,a=map(int,input().split())
        faucets.append((f,a))
    faucets.sort()
    L=int(input())
    queries=[]
    for __ in range(L):
        p,t=map(int,input().split())
        queries.append((p,t))

    # Create segments by boards including edges
    # Each segment represented as (left_x, right_x), and height is min height among partition boards between these x
    # First segment: [0, B1), last segment: [BN,100)
    xs=[0]+[b for b,_ in boards]+[100]

    # Heights of boards
    # between segments i and i+1, there is a board at xs[i+1] with height boards[i].height
    # So number of segments = N+1
    # The height of water for segment bounded by boards or edges is min of board heights bordering it
    # But bordering board height may differ, so water level in segment limited by min heights of bordering boards
    # Left board height set to 0, right board height set to 0 to represent tank edges
    # Actually edges have no board, so infinite height (50cm)
    board_heights=[50]+[h for _,h in boards]+[50]

    segs=[]
    # for i in 0..N segments
    # segment from xs[i] to xs[i+1], height limit:
    # the water level inside segment <= min board heights adjacent: board_heights[i] and board_heights[i+1]
    # so max water level = min(board_heights[i], board_heights[i+1])
    for i in range(len(xs)-1):
        left=xs[i]
        right=xs[i+1]
        height_limit=min(board_heights[i],board_heights[i+1])
        width=right-left
        segs.append({'left':left,'right':right,'width':width,'height_limit':height_limit,'volume':0,'rate_flow':0})

    # Assign faucets to segments
    # Faucets don't coincide with boards; find segment containing faucet
    def find_seg(x):
        # binary search over xs
        low=0
        high=len(xs)-2
        while low<=high:
            mid=(low+high)//2
            if segs[mid]['left']<=x<segs[mid]['right']:
                return mid
            elif x<segs[mid]['left']:
                high=mid-1
            else:
                low=mid+1
        return -1

    for f,a in faucets:
        idx=find_seg(f)
        segs[idx]['rate_flow']+=a

    # Precompute total flow rate
    total_rate=sum(s['rate_flow'] for s in segs)

    # Preprocessing queries for efficiency to avoid repeated calculations
    # For each query, we will simulate water level at position P_k at time T_k
    # We compute water distribution according to water level rise logic:
    # Water fills segments in order of their height limits, lowest limit first
    # When water level equals the segment limit, next level rises to next higher limit where some segment can fill more volume
    # We compute "levels" defined by sorted distinct height limits of segments with positive flow
    # At each level interval, compute volume needed to raise water level
    # We precompute prefix sums of widths of segments which can be filled at each level

    # Get segments with flow > 0
    flow_segments=[s for s in segs if s['rate_flow']>0]

    # Edge case: no flow
    if total_rate==0:
        # Output 0 or 0 height for all queries at these positions
        # Height is 0 always
        for p,t in queries:
            # But if tank full, height=50
            print(0)
        continue

    # Extract unique height limits from flow segments and sort
    heights_set=set()
    for s in flow_segments:
        heights_set.add(s['height_limit'])
    levels=sorted(heights_set)

    # Add 50 at the end if not there
    if levels[-1]<50:
        levels.append(50)

    # Prepare intervals between levels to simulate stepwise filling
    # For each level interval [levels[i], levels[i+1]], volume needed = (levels[i+1]-levels[i]) * total_width_of_segments_that_can_fill
    # Segments that can fill up to at least levels[i+1]

    # For each segment, find the minimum level index where height_limit <= levels[index]
    # For all levels, compute sum of widths of segments with height_limit >= levels[level_index]

    # Precompute total width per level
    # For levels sorted ascending: for each level, segments whose height_limit >= levels[i]
    n_levels=len(levels)
    total_widths=[0]*n_levels
    for i in range(n_levels):
        lvl=levels[i]
        w=0
        for s in flow_segments:
            if s['height_limit']>=lvl:
                w+=s['width']
        total_widths[i]=w

    # Compute volume increments per level interval
    vol_increments=[]
    for i in range(n_levels-1):
        h_diff=levels[i+1]-levels[i]
        vol_increments.append(total_widths[i]*DEPTH*h_diff)

    # Compute cumulative volumes to reach next level
    cum_volumes=[0]
    for v in vol_increments:
        cum_volumes.append(cum_volumes[-1]+v)

    # total tank volume for water height 50 cm = 100*50*30 = 150000 cm3
    # Given total_rate, water volume at time t = min(total_rate*t, VOLUME)

    # To find current water level:
    # 1. Compute volume v = min(total_rate * t, VOLUME)
    # 2. Find which level interval volume v belongs to by binary search on cum_volumes
    # 3. Compute water_height = levels[idx] + (v - cum_volumes[idx]) / (total_widths[idx]*DEPTH)

    # Assign final volume in each segment = (water_height) clamped by segment height_limit * width * depth

    # For faster queries, since queries up to 10, can process each query independently

    for p,t in queries:
        v = total_rate*t
        if v >= VOLUME:
            water_height = 50.0
        else:
            # binary search cum_volumes for v
            low,high=0,len(cum_volumes)-1
            while low<high:
                mid=(low+high)//2
                if cum_volumes[mid]>v:
                    high=mid
                else:
                    low=mid+1
            idx=low-1
            if idx<0:
                idx=0
            vol_remain=v - cum_volumes[idx]
            denom=total_widths[idx]*DEPTH
            if denom>0:
                water_height=levels[idx] + vol_remain/denom
            else:
                water_height=levels[0]

        # At position p, find segment
        idx=find_seg(p)
        seg=segs[idx]
        level_limit=seg['height_limit']

        res_height=water_height
        if water_height>level_limit:
            res_height=level_limit
        if res_height>50:
            res_height=50

        # Round to 6 decimal places or less, error<=0.001 allowed
        print(res_height)