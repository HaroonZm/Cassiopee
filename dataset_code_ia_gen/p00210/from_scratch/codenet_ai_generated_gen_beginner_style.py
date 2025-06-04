directions = {
    'E': (0, 1),
    'N': (-1, 0),
    'W': (0, -1),
    'S': (1, 0)
}

right_turn = {
    'E': 'S',
    'S': 'W',
    'W': 'N',
    'N': 'E'
}

left_turn = {
    'E': 'N',
    'N': 'W',
    'W': 'S',
    'S': 'E'
}

back_turn = {
    'E': 'W',
    'W': 'E',
    'N': 'S',
    'S': 'N'
}

def in_bounds(r, c, H, W):
    return 0 <= r < H and 0 <= c < W

def main():
    while True:
        line = input()
        if line.strip() == '':
            continue
        W_H = line.split()
        if len(W_H) < 2:
            continue
        W, H = map(int, W_H)
        if W == 0 and H == 0:
            break
        maze = []
        for _ in range(H):
            maze.append(list(input()))
        # persons: list of (r, c, dir)
        persons = []
        for r in range(H):
            for c in range(W):
                if maze[r][c] in ['E', 'W', 'N', 'S']:
                    persons.append([r, c, maze[r][c]])
                    maze[r][c] = '.'
        time = 0
        max_time = 180
        while time <= max_time:
            if not persons:
                print(time)
                break
            time += 1
            # first decide next direction for each person
            new_dirs = []
            for p in persons:
                r, c, d = p
                found = False
                check_dirs = [right_turn[d], d, left_turn[d], back_turn[d]]
                for nd in check_dirs:
                    dr, dc = directions[nd]
                    nr, nc = r + dr, c + dc
                    if in_bounds(nr, nc, H, W):
                        if maze[nr][nc] == '.' or maze[nr][nc] == 'X':
                            new_dirs.append(nd)
                            found = True
                            break
                if not found:
                    new_dirs.append(d)
            # id => next move pos or None
            next_pos = []
            for i, p in enumerate(persons):
                r, c, d = p
                nd = new_dirs[i]
                dr, dc = directions[nd]
                nr, nc = r + dr, c + dc
                if in_bounds(nr, nc, H, W) and (maze[nr][nc] == '.' or maze[nr][nc] == 'X'):
                    next_pos.append((nr, nc))
                else:
                    next_pos.append(None)
            # count how many want to move to same pos
            pos_dict = {}
            for pos in next_pos:
                if pos is not None:
                    if pos not in pos_dict:
                        pos_dict[pos] = 0
                    pos_dict[pos] += 1
            # for any pos with multiple want to move, choose who moves by order:
            # east, north, west, south occupant priority order for that pos
            # occupants list for each square
            occupant_grid = [[[] for _ in range(W)] for __ in range(H)]
            for idx, p in enumerate(persons):
                r, c, d = p
                occupant_grid[r][c].append((idx, d))
            # now decide who move if conflict
            move_allowed = [False]*len(persons)
            attempted_positions = {}
            for pos in pos_dict:
                if pos_dict[pos] == 1:
                    # only one person wants to move here
                    idx = next(i for i, np in enumerate(next_pos) if np == pos)
                    move_allowed[idx] = True
                else:
                    # multiple want to move here
                    # find occupant order of east, north, west, south at pos
                    r, c = pos
                    order_dir = ['E', 'N', 'W', 'S']
                    candidate_idxs = []
                    for dir_ in order_dir:
                        # check if occupant in occupant_grid[r][c] with dir_
                        for idx2, d2 in occupant_grid[r][c]:
                            if d2 == dir_:
                                candidate_idxs.append(idx2)
                    # now check for persons wanting to move there which one is first in candidate_idxs
                    # if none of occupant in order_dir want to move there, we check all persons wanting to move there in order of occupants at their pos?
                    # But the problem statement says "東、北、西、南のマス目にいる人の順", so checking current occupant of the target square in order E,N,W,S
                    # the first occupant of these directions who wants to move will move
                    allowed_idx = None
                    for candidate in candidate_idxs:
                        if next_pos[candidate] == pos:
                            allowed_idx = candidate
                            break
                    # if still None, just pick first wanting to move
                    if allowed_idx is None:
                        for i, np in enumerate(next_pos):
                            if np == pos:
                                allowed_idx = i
                                break
                    move_allowed[allowed_idx] = True
            # move persons who can move, update direction to new_dirs for everyone
            new_persons = []
            for i, p in enumerate(persons):
                r, c, d = p
                nd = new_dirs[i]
                if move_allowed[i]:
                    dr, dc = directions[nd]
                    nr, nc = r + dr, c + dc
                    # check if person escaped
                    if maze[nr][nc] == 'X':
                        # person escape, do not add
                        continue
                    else:
                        new_persons.append([nr, nc, nd])
                else:
                    # person stays, direction updated anyway
                    new_persons.append([r, c, nd])
            persons = new_persons
        else:
            # time exceeded max_time and persons remain
            print("NA")

main()