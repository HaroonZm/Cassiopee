from collections import defaultdict, deque

def main():
    n, x0, y0, t = map(int, input().split())
    streets = []
    vert_streets = []
    horiz_streets = []
    for _ in range(n):
        xs, ys, xe, ye = map(int, input().split())
        streets.append((xs, ys, xe, ye))
        if xs == xe:
            vert_streets.append((xs, min(ys, ye), max(ys, ye)))
        else:
            horiz_streets.append((ys, min(xs, xe), max(xs, xe)))
    moves = []
    for _ in range(t):
        d, c = input().split()
        moves.append((int(d), c))

    # Build graph nodes: intersections of streets
    # But the car can be anywhere on streets, not only intersections.
    # We'll represent position as (street_id, position_along_street)
    # position_along_street: distance from one end (start point) along the street.

    # Precompute street lengths and direction vectors
    street_data = []
    for i,(xs,ys,xe,ye) in enumerate(streets):
        length = abs(xe - xs) + abs(ye - ys)
        # Direction vector (dx, dy) pointing from start to end
        dx = 0
        dy = 0
        if xe > xs:
            dx = 1
        elif xe < xs:
            dx = -1
        elif ye > ys:
            dy = 1
        elif ye < ys:
            dy = -1
        street_data.append({'id': i, 'start':(xs,ys), 'end':(xe,ye), 'length':length, 'dx':dx, 'dy':dy})

    # Build street intersections: for each street end point, find the other streets that connect there
    connections = defaultdict(list)  # (street_id, end_flag) -> list of (other_street_id, other_end_flag)
    # end_flag: 0 for start point, 1 for end point
    # The problem states there are no dead ends and no overlapping parallel streets.

    # Map each endpoint to the streets that connect there
    point_to_ends = defaultdict(list)  # point -> list of (street_id, end_flag)
    for s in street_data:
        point_to_ends[s['start']].append((s['id'],0))
        point_to_ends[s['end']].append((s['id'],1))

    for point, ends_list in point_to_ends.items():
        # Connect all ends at this point to each other (except same street ends)
        for sid1, end1 in ends_list:
            for sid2, end2 in ends_list:
                if sid1 != sid2:
                    connections[(sid1,end1)].append((sid2,end2))

    # Determine which streets the initial point (x0,y0) is on
    # and possible directions at time 0
    start_states = []
    for s in street_data:
        x1,y1 = s['start']
        x2,y2 = s['end']
        # The streets are axis-aligned
        # Check if (x0,y0) lies on street segment
        if x1 == x2:
            # vertical street
            if x0 == x1 and min(y1,y2) <= y0 <= max(y1,y2):
                # possible directions: along the street, either dy=1 or dy=-1
                # At the initial position, the car's direction is unknown.
                # So consider both directions allowed on the street at that point
                pos_along = abs(y0 - y1) if y0 >= y1 else abs(y0 - y2)
                # better to define pos_along as distance from start point
                pos_along = abs(y0 - y1)
                # directions are along dy=1 or dy=-1
                # But we do not know if start point corresponds to position 0 or length
                # We defined direction from start to end, so distance along is from start point
                start_states.append((s['id'], pos_along, s['dx'], s['dy']))
                start_states.append((s['id'], pos_along, -s['dx'], -s['dy']))
        else:
            # horizontal street
            if y0 == y1 and min(x1,x2) <= x0 <= max(x1,x2):
                pos_along = abs(x0 - x1)
                start_states.append((s['id'], pos_along, s['dx'], s['dy']))
                start_states.append((s['id'], pos_along, -s['dx'], -s['dy']))

    # Function to get street coordinate from pos_along
    def pos_to_coord(street, pos):
        x1,y1 = street['start']
        dx, dy = street['dx'], street['dy']
        return (x1 + dx * pos, y1 + dy * pos)

    # Function to move forward along the street by dist, return new pos or None if can't
    def move_forward(street, pos, dist, forward=True):
        length = street['length']
        dx, dy = street['dx'], street['dy']
        # If forward is False, moving opposite to street direction
        if not forward:
            dist = -dist
        new_pos = pos + dist
        if 0 <= new_pos <= length:
            return new_pos
        else:
            return None

    # Check if two directions match (N,E,S,W)
    def dir_match(dx, dy, c):
        if c == 'N':
            return dx == 0 and dy == 1
        if c == 'S':
            return dx == 0 and dy == -1
        if c == 'E':
            return dx == 1 and dy == 0
        if c == 'W':
            return dx == -1 and dy == 0
        return False

    # Because direction can be the direction before or after the turn,
    # at turning points we consider both directions

    # State is tuple: (street_id, pos_along, dx, dy)
    # dx, dy represent direction of travel (unit vector along street axis)
    # We'll BFS over states at each time step

    from collections import deque

    curr_states = set(start_states)
    for dist, cdir in moves:
        next_states = set()
        for sid, pos, dx, dy in curr_states:
            s = street_data[sid]
            length = s['length']
            # Try to move dist forward along current direction
            # direction dx, dy may be aligned with s['dx'], s['dy'] or opposite
            forward = (dx == s['dx'] and dy == s['dy'])
            new_pos = move_forward(s, pos, dist, forward=forward)
            if new_pos is not None:
                # No turn needed
                # Check if direction matches measured cdir
                if dir_match(dx, dy, cdir):
                    next_states.add((sid, new_pos, dx, dy))
                # else no possible with no turn
                continue
            # Else, we hit end of street, try to turn at endpoint
            # Need to go dist steps, moving to adjacent street
            # How many steps to reach end of street along current direction?
            if forward:
                dist_to_end = length - pos
                endpoint_flag = 1  # end point
                new_pos_at_end = length
            else:
                dist_to_end = pos
                endpoint_flag = 0  # start point
                new_pos_at_end = 0

            if dist_to_end > dist:
                # Should not happen since previous move_forward returned None
                continue

            rem_dist = dist - dist_to_end
            # From endpoint, can turn to other streets connected
            connects = connections.get((sid, endpoint_flag), [])
            for nsid, n_end_flag in connects:
                ns = street_data[nsid]
                # Determine direction possibilities on new street
                # The car can be going in direction s['dx'],s['dy'] or opposite
                # Choose directions consistent; at turn, direction can be either before or after turn
                # So direction at current time can be before or after turning
                # So cdir measured can be direction on previous street or new street
                
                # Directions on new street:
                ndx = ns['dx']
                ndy = ns['dy']
                candidates_dir = [(ndx, ndy), (-ndx, -ndy)]

                for ndxx, ndyy in candidates_dir:
                    # We will start at the endpoint of new street that connects here
                    # position at new street depends on which end is connected
                    if n_end_flag == 0:
                        npos = 0
                        nforward = (ndxx == ns['dx'] and ndyy == ns['dy'])
                    else:
                        npos = ns['length']
                        nforward = (ndxx == -ns['dx'] and ndyy == -ns['dy'])

                    # Move rem_dist along new street in direction ndx,ndy or reversed
                    # Determine if direction vector matches moving from npos along ndx, ndy (or reverse)
                    # But depending on direction assigned, moving forward or backward on the new street
                    # Need to check if have enough length
                    if nforward:
                        if rem_dist > ns['length'] - npos:
                            continue
                        new_npos = npos + rem_dist
                    else:
                        if rem_dist > npos:
                            continue
                        new_npos = npos - rem_dist

                    # Now, check direction measurement cdir: the measurement can be either before turn (old dx,dy) or after turn (ndxx,ndyy)
                    # So if cdir matches either (dx,dy) or (ndxx,ndyy), accept

                    if dir_match(dx, dy, cdir) or dir_match(ndxx, ndyy, cdir):
                        next_states.add((nsid, new_npos, ndxx, ndyy))
        curr_states = next_states

    # Extract all possible end positions coordinates and output unique sorted by lex order

    result = set()
    for sid, pos, dx, dy in curr_states:
        s = street_data[sid]
        coord = pos_to_coord(s, pos)
        result.add(coord)

    result = sorted(result)
    for x,y in result:
        print(x, y)

if __name__ == '__main__':
    main()