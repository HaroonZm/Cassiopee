from collections import defaultdict, deque

dir_map = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W': (-1,0)}
rev_dir = {(0,1):'N', (1,0):'E', (0,-1):'S', (-1,0):'W'}

n,x0,y0,t = map(int,input().split())
streets = []
for _ in range(n):
    xs,ys,xe,ye = map(int,input().split())
    # store as normalized segment from low to high
    if xs == xe:
        if ys>ye: ys,ye = ye,ys
    else:
        if xs>xe: xs,xe = xe,xs
    streets.append((xs,ys,xe,ye))
# Build graph of junctions and adjacency (intersections)
# junctions are endpoints of streets, and intersections between orthogonal streets

# Extract all endpoints
points = set()
for xs,ys,xe,ye in streets:
    points.add((xs,ys))
    points.add((xe,ye))

# Mapping from point to edges (segments) they belong to
pt_edges = defaultdict(list)
for i,(xs,ys,xe,ye) in enumerate(streets):
    pt_edges[(xs,ys)].append(i)
    pt_edges[(xe,ye)].append(i)

# To find intersections, for each street check orthogonal streets
# Build graph: nodes are points, edges are street segments between points (junctions or intersections)

# For each street, find all intersection points
street_points = []
for i,(xs,ys,xe,ye) in enumerate(streets):
    pts = []
    if xs == xe: # vertical
        x=xs
        # collect all intersections with horizontal streets
        for j,(x2,y2,x3,y3) in enumerate(streets):
            if x2 != x3: # horizontal
                # check if lines cross
                xh_min, xh_max = min(x2,x3), max(x2,x3)
                yh = y2
                v_min, v_max = min(ys,ye), max(ys,ye)
                if xh_min <= x <= xh_max and v_min <= yh <= v_max:
                    pts.append((x,yh))
        pts.extend([(xs,ys),(xe,ye)])
        pts = list(set(pts))
        pts.sort(key=lambda p: p[1])
    else: # horizontal
        y=ys
        for j,(x2,y2,x3,y3) in enumerate(streets):
            if y2 == y3 and y2 == y:
                continue
            if x2 == x3: # vertical
                xv = x2
                h_min, h_max = min(xs,xe), max(xs,xe)
                v_min, v_max = min(y2,y3), max(y2,y3)
                if h_min <= xv <= h_max and v_min <= y <= v_max:
                    pts.append((xv,y))
        pts.extend([(xs,ys),(xe,ye)])
        pts = list(set(pts))
        pts.sort(key=lambda p: p[0])
    street_points.append(pts)

# Build adjacency: for each street, link consecutive points
adj = defaultdict(list)
seg_dir = dict()  # edge (p1,p2) direction vector normalized
for i,pts in enumerate(street_points):
    for k in range(len(pts)-1):
        p1 = pts[k]
        p2 = pts[k+1]
        adj[p1].append(p2)
        adj[p2].append(p1)
        dx = p2[0]-p1[0]
        dy = p2[1]-p1[1]
        if dx != 0:
            dx = dx//abs(dx)
        if dy != 0:
            dy = dy//abs(dy)
        seg_dir[(p1,p2)] = (dx,dy)
        seg_dir[(p2,p1)] = (-dx,-dy)

# Determine which street(s) the start point lies on and possible initial directions
init_states = []
for i,(xs,ys,xe,ye) in enumerate(streets):
    # Check if (x0,y0) lies on street i
    if xs == xe == x0 and min(ys,ye) <= y0 <= max(ys,ye):
        # possible directions along vertical segment
        # possible directions: (0,1) or (0,-1)
        # We consider directions along segment that go away from initial point inside street
        # i.e. if y0>ys, can go south (0,-1), if y0<ye go north (0,1)
        if y0 > ys:
            init_states.append((x0,y0,(0,-1)))
        if y0 < ye:
            init_states.append((x0,y0,(0,1)))
        if y0 == ys == ye:
            # single point segment (not possible here as per input)
            pass
    elif ys == ye == y0 and min(xs,xe) <= x0 <= max(xs,xe):
        # horizontal street
        if x0 > xs:
            init_states.append((x0,y0,(-1,0)))
        if x0 < xe:
            init_states.append((x0,y0,(1,0)))
        if x0 == xs == xe:
            pass

# Read measurements: (distance, direction letter)
measures = []
for _ in range(t):
    d,c = input().split()
    measures.append((int(d), c))

# State: position (x,y), direction (dx,dy)
# BFS style exploration of possible states at each time step
states = set(init_states)

for i in range(t):
    d,c = measures[i]
    ndir = dir_map[c]
    next_states = set()
    for (x,y),(dx,dy) in (( (st[0:2]),st[2]) for st in states):
        # Move d units along current direction if possible
        # Movement along edges, can turn at junctions
        # No U-turns allowed: direction can't become -dx,-dy
        # Measured direction at time i can be before or after turn
        # So possible directions after move: direction before or direction after turn
        # We try to simulate movement: move d units along current direction, possibly turning at junctions

        dist = d
        cx,cy = x,y
        cdx,cdy = dx,dy

        # For movement along streets: we move along edges, possibly turning at junctions
        # We implement walking along edges with given direction cdx,cdy until moved dist units
        # At end of dist, we record possible positions and directions (before or after turn)
        # We do BFS search over moves limited to distance dist and obeying street layout

        # Implement DFS or BFS for walking dist units on graph edges along valid direction

        queue = deque()
        # (x,y), direction, distance moved
        queue.append((cx,cy,cdx,cdy,0))
        visited = dict()  # (pos,dir) -> distance moved when first visited to prevent loops and prune
        visited[(cx,cy,cdx,cdy)] = 0

        while queue:
            ux,uy,udx,udy,mv = queue.popleft()
            rem = dist - mv
            # move along edge in direction udx,udy
            # find next junction along this direction
            adjs = adj[(ux,uy)]
            for vx,vy in adjs:
                ddx = vx - ux
                ddy = vy - uy
                ndx = 0 if ddx == 0 else ddx//abs(ddx)
                ndy = 0 if ddy == 0 else ddy//abs(ddy)
                # Can move on this edge if direction matches
                if ndx == udx and ndy == udy:
                    length = abs(vx - ux) + abs(vy - uy)  # since segments axis-aligned
                    if rem < length:
                        # partial move on edge
                        px = ux + udx*rem
                        py = uy + udy*rem
                        # two possible directions after move:
                        # If turning here, direction could be new one at junction or old one?
                        # At a partial move, no turn, direction same
                        # Check if measured direction c can be either before or after turn:
                        # Here, direction unchanged
                        # Check if measured direction matches direction before or after turn
                        # Theoretically, direction can be measured either before or after turn
                        # Here direction unchanged so c == udx,udy or c == ... same
                        # So we accept if measured direction matches udx,udy
                        if ndir == (udx,udy):
                            next_states.add((px,py,(udx,udy)))
                        # also consider direction after turn (doesn't exist since partial)
                        # no other direction at partial move, so no add
                    else:
                        # full move to junction
                        n_mv = mv + length
                        # At junction after full move, can continue or turn
                        # After move, at (vx,vy)
                        # possible next directions at junction: all edges from vx,vy except no U-turn

                        # First, check measured direction can be before move or after move direction
                        # Before move direction is udx,udy
                        # After move direction can be any direction along edges at (vx,vy) except U-turn (-udx,-udy)
                        # According to problem, measured direction can be either before or after turn
                        # So we accept states with directions:
                        #   - before turn: udx,udy
                        #   - after turn: any direction != (-udx,-udy)

                        # Add state continuing straight:
                        if ndir == (udx,udy):
                            key = (vx,vy,udx,udy)
                            if key not in visited or visited[key]>n_mv:
                                visited[key]=n_mv
                                if n_mv==dist:
                                    next_states.add((vx,vy,udx,udy))
                                else:
                                    queue.append((vx,vy,udx,udy,n_mv))

                        # Add states with turn (all possible directions at junction except U-turn)
                        for wx,wy in adj[(vx,vy)]:
                            ddx2 = wx - vx
                            ddy2 = wy - vy
                            ndx2 = 0 if ddx2 == 0 else ddx2//abs(ddx2)
                            ndy2 = 0 if ddy2 == 0 else ddy2//abs(ddy2)
                            if (ndx2,ndy2) != (-udx,-udy) and (ndx2,ndy2)!=(udx,udy):
                                if ndir == (udx,udy) or ndir == (ndx2,ndy2):
                                    key2 = (vx,vy,ndx2,ndy2)
                                    if key2 not in visited or visited[key2]>n_mv:
                                        visited[key2]=n_mv
                                        if n_mv == dist:
                                            next_states.add((vx,vy,ndx2,ndy2))
                                        else:
                                            queue.append((vx,vy,ndx2,ndy2,n_mv))
                    # We process only the edge matching current direction for movement
                    # Because no U-turns and cannot move against direction
    states=next_states

# Extract final positions sorted lex order
res = sorted({(int(round(x)),int(round(y))) for x,y,_ in states})
for x,y in res:
    print(x,y)