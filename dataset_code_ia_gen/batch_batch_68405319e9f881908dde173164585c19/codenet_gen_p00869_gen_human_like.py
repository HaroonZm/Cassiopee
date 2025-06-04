import sys
from collections import deque

# Cube dice faces indices
# We keep faces in order: [top, bottom, north, south, east, west]
# Colors: r, g, b, c, m, y correspond to cube faces in initial state.

def roll_cube(faces, direction):
    # faces: [top, bottom, north, south, east, west]
    top, bottom, north, south, east, west = faces
    if direction == 'N':
        # roll north: top <- south, bottom <- north, north <- top, south <- bottom, east/west unchanged
        return [south, north, top, bottom, east, west]
    elif direction == 'S':
        # roll south: top <- north, bottom <- south, north <- bottom, south <- top, east/west unchanged
        return [north, south, bottom, top, east, west]
    elif direction == 'E':
        # roll east: top <- west, bottom <- east, east <- top, west <- bottom, north/south unchanged
        return [west, east, north, south, top, bottom]
    elif direction == 'W':
        # roll west: top <- east, bottom <- west, east <- bottom, west <- top, north/south unchanged
        return [east, west, north, south, bottom, top]

def parse_input():
    datasets = []
    input_lines = sys.stdin.read().strip('\n ').split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        w, d = input_lines[idx].split()
        w = int(w)
        d = int(d)
        idx += 1
        if w == 0 and d == 0:
            break
        bed = [list(input_lines[idx+i]) for i in range(d)]
        idx += d
        order = input_lines[idx]
        idx += 1
        datasets.append((w, d, bed, order))
    return datasets

def solve_dataset(w, d, bed, order):
    # Map colors to their positions on bed
    color_pos = {}
    start_pos = None
    for y in range(d):
        for x in range(w):
            c = bed[y][x]
            if c == '#':
                start_pos = (x, y)
            elif c in 'rgbcmy':
                color_pos[c] = (x, y)

    # colors to visit in order
    target_colors = list(order)

    # Initial cube faces colors: top, bottom, north, south, east, west
    # r, c, g, m, b, y (given)
    cube_init = ['r','c','g','m','b','y']

    # We'll do BFS from start to first color, then from first to second, etc.
    # At each step, cube state is (x,y, faces tuple of colors)
    # We must visit each chromatic color square exactly once, in order.
    # We can revisit white squares('w') many times.
    # Can't visit black('k').
    # If we want to go on chromatic color square, the cube top face color after roll must match the square color.
    # Also, once a chromatic square is visited, we cannot visit it again.
    # After last chromatic square, cube disappears.

    def neighbors(x,y):
        for dx,dy,direc in [(0,-1,'N'),(0,1,'S'),(1,0,'E'),(-1,0,'W')]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < w and 0 <= ny < d:
                yield nx, ny, direc

    # We'll do BFS in stages: from start to visit color v1,
    # then from position on v1 visiting v2, etc.
    # At each stage, we keep track of cube position and orientation (faces),
    # as the path depends on cube orientation and board.

    # Function to find minimal steps from a start state to a target color square,
    # while respecting the rules:
    # cube top face must match chromatic color squares we land on,
    # cannot enter black squares,
    # can visit chromatic ones only once (except the target which is visited at the end of stage),
    # can visit white squares multiple times,
    # cannot go on other chromatic color squares than target ones in order.

    def bfs_stage(start_x, start_y, faces, target_color, forbidden_colors):
        # forbidden_colors: chromatic colors already visited before this stage
        # We'll not walk onto chromatic squares in forbidden_colors, or any chromatic square that is not target_color and not white.
        queue = deque()
        # state = (x, y, faces)
        queue.append((start_x, start_y, tuple(faces), 0))
        visited = set()
        visited.add( (start_x, start_y, tuple(faces)) )

        while queue:
            x,y,fs,steps = queue.popleft()
            # If we arrived at target_color position with correct cube top color, done.
            if (x,y) == color_pos[target_color]:
                # cube top face color must be target_color also already checked below
                return (x,y,fs,steps)
            for nx, ny, direc in neighbors(x,y):
                c = bed[ny][nx]
                if c == 'k': # black square forbidden
                    continue
                if c in forbidden_colors:
                    # already visited chromatic (except current target)
                    continue
                if c in 'rgbcmy' and c != target_color:
                    # other chromatic squares not yet to visit
                    # cannot step there now
                    continue
                # Roll cube
                new_faces = roll_cube(fs, direc)
                top_color = new_faces[0]
                # If target_color != c (maybe c == 'w'), no restriction on top face.
                # If c is chromatic color (and should be target_color), top face must match c
                if c in 'rgbcmy':
                    if top_color != c:
                        continue
                state = (nx, ny, tuple(new_faces))
                if state not in visited:
                    visited.add(state)
                    queue.append((nx, ny, tuple(new_faces), steps+1))
        return None

    current_pos = start_pos
    current_faces = cube_init
    total_steps = 0
    visited_colors = set()
    for i,color in enumerate(target_colors):
        path = bfs_stage(current_pos[0], current_pos[1], current_faces, color, visited_colors)
        if path is None:
            return "unreachable"
        x,y,faces,steps = path
        total_steps += steps
        current_pos = (x,y)
        current_faces = list(faces)
        visited_colors.add(color)
    return total_steps

def main():
    datasets = parse_input()
    for w,d,bed,order in datasets:
        res = solve_dataset(w,d,bed,order)
        print(res)

if __name__ == '__main__':
    main()