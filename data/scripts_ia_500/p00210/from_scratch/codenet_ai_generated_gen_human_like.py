import sys

DIRS = {'E': (0, 1), 'N': (-1, 0), 'W': (0, -1), 'S': (1, 0)}
RIGHT = {'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E'}
LEFT = {'E': 'N', 'N': 'W', 'W': 'S', 'S': 'E'}
BACK = {'E': 'W', 'W': 'E', 'N': 'S', 'S': 'N'}
PRIORITY = ['E', 'N', 'W', 'S']  # For conflict resolution

def in_bounds(r, c, H, W):
    return 0 <= r < H and 0 <= c < W

def simulate(W, H, grid, people):
    time = 0
    # people: list of (r,c,direction)
    # grid cells: '#', '.', 'X'
    while people:
        time += 1
        if time > 180:
            return 'NA'
        # 1) Try to update directions
        new_dirs = []
        for (r,c,d) in people:
            # check right, front, left, back from current direction
            check_dirs = []
            d_right = RIGHT[d]
            d_front = d
            d_left = LEFT[d]
            d_back = BACK[d]
            check_dirs = [d_right, d_front, d_left, d_back]
            updated_dir = d
            for nd in check_dirs:
                dr, dc = DIRS[nd]
                nr, nc = r+dr, c+dc
                if in_bounds(nr,nc,H,W) and grid[nr][nc] in ['.', 'X']:
                    updated_dir = nd
                    break
            new_dirs.append((r,c,updated_dir))
        people = new_dirs
        # 2) Determine target cells for movement
        target_map = dict()  # (nr,nc) -> list of person indices wanting to move there
        move_intent = []
        for idx, (r,c,d) in enumerate(people):
            dr, dc = DIRS[d]
            nr, nc = r+dr, c+dc
            if not in_bounds(nr,nc,H,W):
                # Can't move out of bounds
                move_intent.append(None)
                continue
            if grid[nr][nc] not in ['.', 'X']:
                # can't move into wall
                move_intent.append(None)
                continue
            move_intent.append((nr,nc))
            target_map.setdefault((nr,nc), []).append(idx)
        # 3) Apply tie-breaking to decide which person move if multiple target same cell
        # The tie-break order is based on the occupants adjacent to the target cell
        # Checking occupants in order E,N,W,S direction adjacent to the target cell
        move_allowed = set()
        for pos, indices in target_map.items():
            if len(indices) == 1:
                # only one person wants to move here
                move_allowed.add(indices[0])
            else:
                # multiple want to move, pick one according to priority
                nr,nc = pos
                chosen = None
                for dir_ in PRIORITY:
                    dr, dc = DIRS[dir_]
                    rr, cc = nr+dr, nc+dc
                    if not in_bounds(rr,cc,H,W):
                        continue
                    # check if a person is at (rr,cc)
                    for iidx, (pr, pc, pd) in enumerate(people):
                        if iidx in indices and iidx in move_allowed:
                            # already moved this time? no, movement simultaneous so no
                            pass
                        if (pr, pc) == (rr, cc) and iidx in indices:
                            chosen = iidx
                            break
                    if chosen is not None:
                        break
                # If no adjacent person found in that order, fallback to first index
                if chosen is None:
                    chosen = indices[0]
                move_allowed.add(chosen)
        # 4) Move those allowed, others stay
        new_people = []
        for i, (r,c,d) in enumerate(people):
            if move_intent[i] is not None and i in move_allowed:
                nr, nc = move_intent[i]
                # Check if new spot is exit
                if grid[nr][nc] == 'X':
                    # Person escaped, do not add
                    continue
                else:
                    new_people.append((nr,nc,d))
            else:
                new_people.append((r,c,d))
        people = new_people
    return time

def main():
    input = sys.stdin.readline
    while True:
        line = ''
        while line.strip() == '':
            line = input()
            if line == '':
                return
        W,H = map(int,line.strip().split())
        if W == 0 and H == 0:
            break
        grid = []
        people = []
        for r in range(H):
            row = input().rstrip('\n')
            grid.append(list(row))
            for c,ch in enumerate(row):
                if ch in ['E','W','S','N']:
                    people.append((r,c,ch))
                    # mark cell as floor so we don't confuse later with person
                    grid[r][c] = '.'
        ans = simulate(W,H,grid,people)
        print(ans)

if __name__ == '__main__':
    main()