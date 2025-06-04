import math
import sys

input = sys.stdin.readline

def vec_sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])

def vec_dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def vec_len_sq(v):
    return v[0]*v[0] + v[1]*v[1] + v[2]*v[2]

def line_sphere_intersection(P0, P1, C, r):
    # Compute intersection points between segment P0P1 and sphere centered at C with radius r
    # Returns a tuple (t1, t2) of parametric values along the segment line where intersections occur, or None if no intersection
    # Parametric line: P(t) = P0 + t*(P1-P0), t in [0, 1]
    d = vec_sub(P1, P0)
    f = vec_sub(P0, C)
    a = vec_dot(d, d)
    b = 2 * vec_dot(f, d)
    c = vec_dot(f, f) - r*r

    discriminant = b*b - 4*a*c
    if discriminant < 0:
        return None
    sqrt_disc = math.sqrt(discriminant)
    t1 = (-b - sqrt_disc)/(2*a)
    t2 = (-b + sqrt_disc)/(2*a)
    # Restrict to segment [0,1]
    intervals = []
    if 0 <= t1 <= 1:
        intervals.append(t1)
    if 0 <= t2 <= 1:
        intervals.append(t2)
    if len(intervals) == 0:
        return None
    # Return sorted
    return sorted(intervals)

N, Q = map(int, input().split())
obstacles = []
for _ in range(N):
    x, y, z, r, l = map(int, input().split())
    obstacles.append((x,y,z,r,l))
queries = []
for _ in range(Q):
    sx, sy, sz, dx, dy, dz = map(int, input().split())
    queries.append(((sx,sy,sz),(dx,dy,dz)))

for s, d in queries:
    events = []  # list of tuples (t, l_i, type) type: +1 enter, -1 leave
    # For each obstacle find intersection interval [t0,t1]
    for (x,y,z,r,l) in obstacles:
        inter = line_sphere_intersection(s,d,(x,y,z),r)
        if inter is None:
            continue
        if len(inter) == 1:
            t0 = t1 = inter[0]
        else:
            t0, t1 = inter
        # Add entering and leaving events
        # If intersection is a single point, both events at same t
        events.append((t0, l, +1))
        events.append((t1, l, -1))
    # Sort events by t
    events.sort(key=lambda x: (x[0], -x[2]))  # Leaves processed after enters at same t so +1 before -1

    # Sweep line along the segment from s to d
    active = set()
    total_cost = 0
    prev_t = 0.0
    idx = 0
    # We move from t=0 to t=1 over the line segment
    # Whenever we hit an event, update active set and add cost of crossing intervals
    while idx < len(events):
        t = events[idx][0]
        # Add cost if t>prev_t and some obstacles active
        if t > prev_t and len(active) > 0:
            # Sum magic cost for all active obstacles and add once (for this interval)
            # Actually, cost is sum of l_i for obstacles intersected simultaneously
            cost = sum(active)
            total_cost += cost
        # Process all events at this t
        while idx < len(events) and math.isclose(events[idx][0], t):
            _t, l_val, typ = events[idx]
            if typ == +1:
                active.add(l_val)
            else:
                active.discard(l_val)
            idx += 1
        prev_t = t
    # After last event till t=1
    if prev_t < 1.0 and len(active) > 0:
        cost = sum(active)
        total_cost += cost

    print(total_cost)