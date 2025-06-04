import sys
import heapq

def parse_intersection(s):
    h,v = s.split('-')
    return (h,v)

def next_direction(dir):
    # directions with dx,dy and their opposite
    # 'E','W','N','S'
    # U-turn forbidden: cannot go back to dir opposite to coming
    return ['N','S','E','W']

def dir_vec():
    return {'E':(1,0), 'W':(-1,0), 'N':(0,-1), 'S':(0,1)}

def opposite(d):
    opp = {'E':'W', 'W':'E', 'N':'S', 'S':'N'}
    return opp[d]

def coord_index(h, v, hlist, vlist):
    x = hlist.index(h)
    y = vlist.index(v)
    return (x,y)

def inside(x,y,M,N):
    return 0<=x<M and 0<=y<N

def signal_state_at(signal_k, t):
    # signal changes every k minutes: starting with NS green (i.e. EW red) at t=0
    # we return True if EW green, False if EW red
    # so ew green duration k, then ew red k, repeatedly
    cycle = 2*signal_k
    t = t % cycle
    if t < signal_k:
        # NS green; EW red
        return False
    else:
        # EW green
        return True

def signal_allows_entry(intersection, dir_arrive, t, signals):
    # If intersection has no signal, entry allowed.
    # Else:
    # At time t of arrival, if signal allows going on dir_arrive
    # Truck comes from opposite direction of dir_arrive, so is arriving on the edge in that direction.
    # At signals, when the light is green for NS => can enter intersection moving north or south
    # when green for EW => can enter intersection moving east or west
    # Truck can move in 4 directions, but arrive from direction opposite to moving direction.
    # Here, dir_arrive is direction the truck moves from intersection to next.
    # But we need to check light state to enter the intersection from previous road.
    # The problem states "トラックは交差点に到達した時刻に、信号が赤の場合には進入できません"
    # so the arrival point intersection's signal decides.
    # Let's deduce:
    # The light cycle is:
    # NS green = north or south allowed to move through intersection (i.e. entering intersection on N or S)
    # EW green = east or west allowed
    # The arrival to intersection comes from previous edge, the truck then leaves intersection on dir_arrive.
    # But the rule is the truck cannot enter intersection if signal is red for that direction at the arrival time.
    # Since initial direction is east, the truck heading east moves from west intersection to east intersection.
    # So the direction on edge is the direction the truck moves from current intersection.
    # But when the truck arrives at next intersection, it 'arrives' from opposite direction to dir_arrive.
    # So the color at the next intersection at time t must allow the truck to enter from the edge dir opposite to dir_arrive.
    # The problem says "交差点のいくつかには東西 - 南北の方向に信号機が設置され"，"東西が青ならば南北が赤で"
    # Let's thus consider the direction from which the truck arrives at intersection: opp_dir = opposite of dir_arrive
    # If opp_dir in E or W, then the signal at intersection must be EW green.
    # If opp_dir in N or S, then signal at intersection must be NS green.
    # So if signal is green for that direction at arrival time, can enter, else must wait.
    if intersection not in signals:
        return True

    k = signals[intersection]
    cycle = 2*k
    t_mod = t % cycle
    opp_dir = opposite(dir_arrive)
    # NS green first k minutes, then EW green k minutes
    if opp_dir in ('N','S'):
        # NS green first k minutes
        if t_mod < k:
            return True
        else:
            return False
    else:
        # EW green second k minutes
        if t_mod >= k:
            return True
        else:
            return False

def wait_time_to_enter_signal(intersection, dir_arrive, current_time, signals):
    if intersection not in signals:
        return 0
    k = signals[intersection]
    cycle = 2*k
    t_mod = current_time % cycle
    opp_dir = opposite(dir_arrive)
    if opp_dir in ('N','S'):
        if t_mod < k:
            # NS green, can enter
            return 0
        else:
            # wait until next NS green start
            return (cycle - t_mod)
    else:
        if t_mod >= k:
            # EW green ok
            return 0
        else:
            return (k - t_mod)

def build_graph(M,N,D,signals,road_invalid,road_jam, jam_time, hlist, vlist):
    # intersections are grid points (x in 0..M-1, y in 0..N-1)
    # edges between adjacent intersections horizontally and vertically if no road_invalid
    # Create adjacency list:
    # graph[node] = list of (neighbor, travel_time)
    graph = {}
    for x in range(M):
        for y in range(N):
            node = (x,y)
            neighbors = []
            # four directions
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < M and 0 <= ny < N:
                    # map back to intersection string to check road_invalid and road_jam
                    from_inter = (hlist[x], vlist[y])
                    to_inter = (hlist[nx], vlist[ny])
                    e1 = from_inter
                    e2 = to_inter
                    # roads are two-way; check if this edge is invalid
                    key = (e1,e2)
                    key_rev = (e2,e1)
                    if key in road_invalid or key_rev in road_invalid:
                        continue
                    timecost = D
                    if key in road_jam:
                        timecost += jam_time[key]
                    elif key_rev in road_jam:
                        timecost += jam_time[key_rev]
                    neighbors.append(((nx,ny), timecost))
            graph[node] = neighbors
    return graph


def solve():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        line=line.strip()
        if line == '':
            continue
        M,N = map(int,line.split())
        if M==0 and N==0:
            break
        D = int(input())
        ns = int(input())
        signals = {}
        for _ in range(ns):
            s,k = input().split()
            k=int(k)
            inter = parse_intersection(s)
            signals[inter] = k
        nc = int(input())
        road_invalid = set()
        for _ in range(nc):
            s1,s2 = input().split()
            i1 = parse_intersection(s1)
            i2 = parse_intersection(s2)
            road_invalid.add( (i1,i2) )
            road_invalid.add( (i2,i1) )
        nj = int(input())
        road_jam = set()
        jam_time = {}
        for _ in range(nj):
            s1,s2,dj = input().split()
            dj = int(dj)
            i1 = parse_intersection(s1)
            i2 = parse_intersection(s2)
            road_jam.add( (i1,i2) )
            road_jam.add( (i2,i1) )
            jam_time[(i1,i2)] = dj
            jam_time[(i2,i1)] = dj
        s,d = input().split()
        start = parse_intersection(s)
        goal = parse_intersection(d)

        # create hlist and vlist from problem:
        # h: 'a' to ...
        # v: '1' to ...
        hset = set()
        vset = set()
        # collect all intersections including signals, roads
        hset.add(start[0])
        hset.add(goal[0])
        vset.add(start[1])
        vset.add(goal[1])
        for k in signals.keys():
            hset.add(k[0])
            vset.add(k[1])
        for e in road_invalid:
            hset.add(e[0][0])
            vset.add(e[0][1])
            hset.add(e[1][0])
            vset.add(e[1][1])
        for e in road_jam:
            hset.add(e[0][0])
            vset.add(e[0][1])
            hset.add(e[1][0])
            vset.add(e[1][1])
        # make sure to add all intersections in grid:
        # h: a,b,... length M
        # v: 1,2,... length N
        hlist = [ chr(ord('a')+i) for i in range(M) ]
        vlist = [ str(i+1) for i in range(N) ]

        # Build graph adjacency
        graph = build_graph(M,N,D,signals,road_invalid,road_jam,jam_time,hlist,vlist)

        # initial conditions
        # truck starts facing east at start intersection
        # states: (cost, x, y, dir)
        # dir in 'E','W','N','S'
        # initial dir = 'E'

        # Use Dijkstra on state space: node=(x,y), dir
        # store best times:
        INF = 10**9
        dist = {}
        hq = []
        for x in range(M):
            for y in range(N):
                for d in ['E','W','N','S']:
                    dist[(x,y,d)] = INF
        sx,sy = coord_index(start[0], start[1], hlist,vlist)
        gx,gy = coord_index(goal[0], goal[1], hlist,vlist)
        start_dir = 'E'
        dist[(sx,sy,start_dir)] = 0
        heapq.heappush(hq,(0,sx,sy,start_dir))

        while hq:
            t,x,y,d = heapq.heappop(hq)
            if dist[(x,y,d)] < t:
                continue
            if (x,y) == (gx,gy):
                # found goal
                print(t)
                break
            node = (x,y)

            for (nx,ny), tt in graph[node]:
                # determine direction from (x,y) to (nx,ny)
                dx = nx - x
                dy = ny - y
                if dx==1 and dy==0:
                    nd = 'E'
                elif dx==-1 and dy==0:
                    nd = 'W'
                elif dx==0 and dy==1:
                    nd = 'S'
                elif dx==0 and dy==-1:
                    nd = 'N'
                else:
                    continue
                # can't U-turn
                if nd == opposite(d):
                    continue
                # at node (x,y), wait if needed to enter next intersection of (nx,ny)
                # arrival time at next intersection = t + tt
                # check signal at next intersection if can enter immediately or wait there?
                # problem states: "交差点に到達した時刻に、信号が赤の場合には進入できません"
                # so arrival time must be when signal allows entering (i.e. direction opposite to nd allowed at arrival)
                arrival_time = t + tt
                wait = wait_time_to_enter_signal( (hlist[nx], vlist[ny]), nd, arrival_time, signals)
                arrival_time += wait

                if dist[(nx,ny,nd)] > arrival_time:
                    dist[(nx,ny,nd)] = arrival_time
                    heapq.heappush(hq,(arrival_time,nx,ny,nd))
        else:
            # no path found: problem states always within 100 min possible
            print(-1)

if __name__=="__main__":
    solve()