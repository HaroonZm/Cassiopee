import sys
from collections import deque

def can_princess_escape(H, W, palace_map):
    # Directions for moves: up, down, left, right, and stay (no move)
    directions = [(-1,0), (1,0), (0,-1), (0,1), (0,0)]

    # Initialize positions and grids
    # soldiers: list of starting positions of soldiers
    soldiers = []
    princess = None
    escape = None

    # Parse the map and find princess, soldiers and escape hatch positions
    for i in range(H):
        for j in range(W):
            c = palace_map[i][j]
            if c == '@':
                princess = (i, j)
            elif c == '$':
                soldiers.append((i, j))
            elif c == '%':
                escape = (i, j)

    # Compute minimum time for soldiers to reach each cell using multi-source BFS
    # The soldiers can only enter empty cells ('.'), princess (@), escape hatch (%), or soldier ($) cells
    # Walls '#' are impassable.
    soldiers_arrival = [[float('inf')] * W for _ in range(H)]
    q_soldiers = deque()

    # Initialize queue with all soldiers and arrival time 0 at their positions
    for sx, sy in soldiers:
        soldiers_arrival[sx][sy] = 0
        q_soldiers.append((sx, sy))

    while q_soldiers:
        x, y = q_soldiers.popleft()
        current_time = soldiers_arrival[x][y]
        for dx, dy in directions[:-1]:  # soldiers can't stay in place to benefit; but let's keep consistency and include stay later if needed
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W:
                # Check if cell is empty or special passable
                cell = palace_map[nx][ny]
                if cell != '#':
                    # If arrival time not set or found quicker way
                    if soldiers_arrival[nx][ny] > current_time + 1:
                        soldiers_arrival[nx][ny] = current_time + 1
                        q_soldiers.append((nx, ny))
    
    # Now do BFS for princess paths
    # The princess must never move into or remain in a cell where a soldier can be at the same time or earlier.
    # Because all move simultaneously, the princess cannot enter a cell where soldiers arrival time <= princess arrival time.
    princess_arrival = [[float('inf')] * W for _ in range(H)]
    q_princess = deque()
    px, py = princess
    princess_arrival[px][py] = 0
    q_princess.append((px, py))

    while q_princess:
        x, y = q_princess.popleft()
        current_time = princess_arrival[x][y]
        # If princess reached escape, return True
        if (x, y) == escape:
            # Princess reached escape hatch before or alone
            # Note: if soldiers arrive at the same time, princess is caught.
            # We guarantee that soldiers_arrival[x][y] > princess_arrival[x][y] to be safe.
            if soldiers_arrival[x][y] > current_time:
                return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            nt = current_time + 1
            if 0 <= nx < H and 0 <= ny < W:
                cell = palace_map[nx][ny]
                # princess can enter if not wall
                if cell != '#':
                    # princess arrival time must be improved
                    # and soldiers arrival time at nx, ny must be strictly greater than princess arrival time (no simultaneous or earlier arrival)
                    if princess_arrival[nx][ny] > nt and soldiers_arrival[nx][ny] > nt:
                        princess_arrival[nx][ny] = nt
                        q_princess.append((nx, ny))

    # If no path found for princess to safely reach escape hatch
    return False

def main():
    input_lines = sys.stdin.read().splitlines()
    idx = 0
    while idx < len(input_lines):
        if not input_lines[idx].strip():
            idx += 1
            continue
        H_W = input_lines[idx].strip().split()
        if len(H_W) != 2:
            break
        H, W = map(int, H_W)
        idx +=1
        palace_map = []
        for _ in range(H):
            palace_map.append(input_lines[idx])
            idx +=1
        if can_princess_escape(H, W, palace_map):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()