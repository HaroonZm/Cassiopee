def robot_moves(N, layout, positions, directions):
    # directions: 0 = north, 1 = east, 2 = south, 3 = west
    # returns new positions, new directions, halted flags
    # adjacent detection order: left, right, forward
    # left/right/forward depends on current direction
    dir_move = [(-1,0),(0,1),(1,0),(0,-1)]
    def left_dir(d): return (d+3)%4
    def right_dir(d): return (d+1)%4

    new_positions = []
    new_directions = []
    halted = []

    pos_set = set(positions)

    for i in range(len(positions)):
        r,c = positions[i]
        d = directions[i]
        current_color = layout[r][c]

        neighbors = []
        # left
        ld = left_dir(d)
        lr, lc = r+dir_move[ld][0], c+dir_move[ld][1]
        if 0 <= lr < N and 0 <= lc < N:
            neighbors.append((layout[lr][lc],'L',(lr,lc),ld))
        else:
            neighbors.append((None,'L',None,None))
        # right
        rd = right_dir(d)
        rr, rc = r+dir_move[rd][0], c+dir_move[rd][1]
        if 0 <= rr < N and 0 <= rc < N:
            neighbors.append((layout[rr][rc],'R',(rr,rc),rd))
        else:
            neighbors.append((None,'R',None,None))
        # forward
        fd = d
        fr, fc = r+dir_move[fd][0], c+dir_move[fd][1]
        if 0 <= fr < N and 0 <= fc < N:
            neighbors.append((layout[fr][fc],'F',(fr,fc),fd))
        else:
            neighbors.append((None,'F',None,None))

        same_color_neighbors = [n for n in neighbors if n[0] == current_color]

        if len(same_color_neighbors) == 1:
            # change direction to that side and move forward
            ncolor, pos_dir, pos_coord, newdir = same_color_neighbors[0]
            # move
            new_positions.append(pos_coord)
            new_directions.append(newdir)
            halted.append(False)
        else:
            # halt
            new_positions.append((r,c))
            new_directions.append(d)
            halted.append(True)

    # check collision:
    # no two robots on same room
    pos_count = {}
    for p in new_positions:
        if p in pos_count:
            pos_count[p] += 1
        else:
            pos_count[p] = 1
    collision = False
    for p,cnt in pos_count.items():
        if cnt >= 2:
            collision = True

    # check exchange positions: two robots swapped positions
    if not collision:
        for i in range(len(positions)):
            for j in range(i+1,len(positions)):
                if new_positions[i] == positions[j] and new_positions[j] == positions[i]:
                    collision = True
                    break
            if collision:
                break

    if collision:
        # all robots halt
        new_positions = positions[:]
        new_directions = directions[:]
        halted = [True]*len(positions)

    return new_positions, new_directions, halted

def can_clean_all(layout, N):
    # try to check if there's an initial placement and directions
    # that cause the robots to clean all rooms (simulate some robots?)
    # Due to problem complexity, we try a simple approach:
    # place one robot on each room with all 4 directions,
    # simulate for some steps, and check if all rooms are cleaned.

    # cleaning record, 2D bool
    cleaned = [[False]*N for _ in range(N)]
    # list of robots: positions and directions
    robots = []
    for r in range(N):
        for c in range(N):
            for d in range(4):
                robots.append(((r,c),d))

    # initially all robots clean their rooms
    for (r,c),d in robots:
        cleaned[r][c] = True

    max_steps = 2*N*N  # arbitrary limit

    positions = [pos for pos,d in robots]
    directions = [d for pos,d in robots]
    active = [True]*len(robots)

    for step in range(max_steps):
        if all(all(row) for row in cleaned):
            return True
        if not any(active):
            return False

        # collect positions and directions of only active robots
        current_positions = []
        current_directions = []
        active_indexes = []
        for i in range(len(robots)):
            if active[i]:
                current_positions.append(positions[i])
                current_directions.append(directions[i])
                active_indexes.append(i)
        if not current_positions:
            return False

        new_positions, new_directions, halted = robot_moves(N, layout, current_positions, current_directions)

        # update main lists
        for idx,pos,direction,halt in zip(active_indexes, new_positions, new_directions, halted):
            positions[idx] = pos
            directions[idx] = direction
            active[idx] = not halt

            if not halt:
                r,c = pos
                cleaned[r][c] = True

    # if cleaned all
    if all(all(row) for row in cleaned):
        return True
    return False

def generate_layouts(N, K):
    # generate all layouts lex order: '.' < 'E'
    # layout string length = N*N
    # we want the K-th layout that meet condition
    # return layout as list of strings or None
    from itertools import product

    # use a generator to generate all layouts lex order
    # '.' -> 0, 'E'->1
    # So layout like '...E..E.' etc
    # we go from 0 to 2^(N*N)-1 lex order by binary number
    # but since N*N might be large we only generate as many as needed

    max_layouts = 1 << (N*N)
    count = 0

    # To go lex order with '.' < 'E', we can generate all bit masks from 0 to max_layouts-1
    # but bits 0 = '.', 1='E'
    # we try increasing binary numbers from 0 upwards
    for num in range(max_layouts):
        # construct layout string
        s = ''
        for i in range(N*N):
            bit = (num >> (N*N - 1 - i)) & 1
            if bit == 0:
                s += '.'
            else:
                s += 'E'
        layout = [s[i*N:(i+1)*N] for i in range(N)]
        if can_clean_all(layout, N):
            count += 1
            if count == K:
                return layout
    return None

def main():
    import sys
    for line in sys.stdin:
        if line.strip() == '':
            continue
        N,K = map(int, line.strip().split())
        if N == 0 and K == 0:
            break
        layout = generate_layouts(N,K)
        if layout is None:
            print("No\n")
        else:
            for row in layout:
                print(row)
            print()

main()