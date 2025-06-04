import sys
sys.setrecursionlimit(10000)

H, W = map(int, input().split())
sheet = [list(input()) for _ in range(H)]

visited = [[False]*W for _ in range(H)]
cubes = []

def neighbors(r,c):
    for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
        if 0 <= nr < H and 0 <= nc < W:
            yield nr,nc

def dfs(r,c):
    stack = [(r,c)]
    comp = []
    while stack:
        rr, cc = stack.pop()
        if visited[rr][cc]:
            continue
        visited[rr][cc] = True
        comp.append((rr,cc))
        for nr,nc in neighbors(rr,cc):
            if not visited[nr][nc] and sheet[nr][nc] != '.':
                stack.append((nr,nc))
    return comp

# Find cubes: connected components of non '.' squares
for i in range(H):
    for j in range(W):
        if sheet[i][j] != '.' and not visited[i][j]:
            comp = dfs(i,j)
            cubes.append(comp)

# Check if number of cubes is 8
if len(cubes) != 8:
    print("No")
    sys.exit()

# For each cube, find bounds and build a 3x4 unfolded cube net representation from the sheet
# The net layout is assumed as:
#   [ ] [0] [ ] [ ]
#   [1] [2] [3] [4]
#   [ ] [5] [ ] [ ]
# where numbers are faces of the cube:
# 0 = front
# 1 = left
# 2 = bottom
# 3 = right
# 4 = top
# 5 = back
# We are told front sides are painted and exposed, inside faces are black (#).
# So we need to find colors of all faces.

# For each cube, create a dictionary face->color or black
# Then we need to assign coordinates in 3D for these cubes to build the 2x2x2 bicube
# Inside faces must be black
# Outside faces must be uniform color per face of the bicube, all different colors on 6 faces
# Let's do a simple way: assign each cube a position in 3D (x,y,z) from their min row and col to get a 2x2x2
# Then check adjacency and faces colors.

def get_bbox(comp):
    rs = [r for r,_ in comp]
    cs = [c for _,c in comp]
    return min(rs), max(rs), min(cs), max(cs)

def get_face_color(r,c):
    ch = sheet[r][c]
    if ch == '#':
        return '#'
    else:
        return ch

def extract_cube_faces(comp):
    # get bounding box
    rmin,rmax,cmin,cmax = get_bbox(comp)
    cube_map = {}
    for r,c in comp:
        cube_map[(r,c)] = sheet[r][c]

    # Faces in net positions (r,c) relative to rmin,cmin
    # Let's store the 3x4 net in an array filled with '.' if no face
    net = [['.' for _ in range(4)] for _ in range(3)]
    for r,c in comp:
        nr = r - rmin
        nc = c - cmin
        if 0 <= nr < 3 and 0 <= nc < 4:
            net[nr][nc] = sheet[r][c]

    # Identify faces by position in net:
    # We'll find color of each face by majority color in its one-square face or multiple squares if painted that way
    # The problem states each face consists of one square for the unit cube in the sheet?
    # Actually it's a sheet of squares folded out, each cube's net is 6 squares connected in cross shape.
    # So count colors in positions:
    # 0: net[0][1], top row 2nd position = front face
    # 1: net[1][0] left face
    # 2: net[1][1] bottom face
    # 3: net[1][2] right face
    # 4: net[1][3] top face
    # 5: net[2][1] back face
    
    faces_pos = [(0,1),(1,0),(1,1),(1,2),(1,3),(2,1)]
    faces = {}
    for i,(rr,cc) in enumerate(faces_pos):
        ch = net[rr][cc]
        if ch == '.':
            # missing face; treat as unpainted
            faces[i] = '.'
        else:
            faces[i] = ch
    return faces

cubes_faces = []
positions = []

# To find positions of cubes, use min r and c to detect 2x2 grid arrangement
# From problem samples looks like each cube corresponds roughly to some position divided by width of connected squares
# We'll try to assign positions by row and col ranges of cubes' bounding boxes:
# Create a list of unique bounding box top-left corners rows and cols
rows_set = set()
cols_set = set()
for comp in cubes:
    rmin,rmax,cmin,cmax = get_bbox(comp)
    rows_set.add(rmin)
    cols_set.add(cmin)

rows_list = sorted(list(rows_set))
cols_list = sorted(list(cols_set))
# Expect 2 unique rows and 4 unique cols since net width is 3x4 and 8 cubes arranged as 2x4 grid?

# Because bicube is 2x2x2, 8 cubes arranged in a cube shape.
# So we try to find a 2x2x2 position for cubes by grouping bounding boxes
# But as a beginner, just try to assign position by (row index in rows_list, col index in cols_list)
# and then we map them to 3D coordinates (x,y,z)

pos_map = {}
for idx,comp in enumerate(cubes):
    rmin,rmax,cmin,cmax = get_bbox(comp)
    r_pos = rows_list.index(rmin)
    c_pos = cols_list.index(cmin)
    pos_map[idx] = (r_pos, c_pos)
    faces = extract_cube_faces(comp)
    cubes_faces.append(faces)
    positions.append((r_pos,c_pos))

# From sample input, looks like rows_list has length 2, cols_list length 4
# But bicube is 2x2x2 so we must identify z coordinate
# Each cube net has 6 faces. The front square is painted and exposed - so net position (0,1)
# Inside faces are black (#)
# Approach: try all ways to assign cubes to 3D positions in 2x2x2

# We'll try to assign cubes to (x,y,z) coordinates from positions (r_pos,c_pos)
# try to group cubes in two layers (z=0 and z=1) based on rows_list and cols_list grouping, assuming rows for z and cols for x,y

# We do not know exact way so we'll try to find a mapping from (r_pos,c_pos) to (x,y,z) 
# Let's try all ways to separate the 8 cubes into two layers of 4 cubes each (z=0 and z=1)
# For each layer assign x,y from positions

from itertools import combinations, permutations

def adj_faces(a,b):
    # Returns which faces are adjacent for two cubes if they share a face in 3D
    # a and b are tuples (x,y,z)
    dx = b[0]-a[0]
    dy = b[1]-a[1]
    dz = b[2]-a[2]
    # if they share a face, difference must be exactly one in one axis, zero in others
    if abs(dx)+abs(dy)+abs(dz) != 1:
        return None,None
    # adjacent faces indexes same as in extract_cube_faces: 0-front,1-left,2-bottom,3-right,4-top,5-back

    # direction vectors -> face pairs:
    # if b is at x+1: face 3 of a adjacent to face 1 of b
    if dx == 1:
        return 3,1
    if dx == -1:
        return 1,3
    # if b is at y+1: face 4 (top) of a adjacent to 2 (bottom) of b
    if dy == 1:
        return 4,2
    if dy == -1:
        return 2,4
    # if b is at z+1: face 0 (front) of a adjacent to 5 (back) of b
    if dz == 1:
        return 0,5
    if dz == -1:
        return 5,0
    return None,None

found = False
idxs = range(8)
# since cubes count is 8, separate into two groups of 4 for two layers (z=0 and z=1)
for lower_layer in combinations(idxs,4):
    upper_layer = [i for i in idxs if i not in lower_layer]
    # assign positions in layer: find permutations of cubes in each layer to map 4 cubes in layer to 4 position points for x,y
    # for simplicity we try to place cubes at positions in positions and assign z=0 or z=1 depending on layer

    # must find 4 unique (x,y) positions for each layer
    # So pick positions of cubes in layer and check if their (r_pos,c_pos) have 4 unique (x,y) combos
    lower_pos = [positions[i] for i in lower_layer]
    upper_pos = [positions[i] for i in upper_layer]

    if len(set(lower_pos)) != 4 or len(set(upper_pos)) !=4:
        continue

    # Try all permutations to assign cubes to (x,y)
    for perm_low in permutations(lower_layer):
        for perm_up in permutations(upper_layer):
            dic_pos = {}
            # map cubes in perm_low to lower_pos
            for i, cube_i in enumerate(perm_low):
                dic_pos[cube_i] = (lower_pos[i][0], lower_pos[i][1], 0)
            # map cubes in perm_up to upper_pos with z=1
            for i, cube_i in enumerate(perm_up):
                dic_pos[cube_i] = (upper_pos[i][0], upper_pos[i][1], 1)

            # Check adjacency and inside faces black
            # For each cube, check neighbors in dic_pos by coordinates difference
            # If cubes adjacent, their touching faces must be black (#)

            valid = True
            for i in range(8):
                for j in range(i+1,8):
                    a = dic_pos[i]
                    b = dic_pos[j]
                    a_face, b_face = adj_faces(a,b)
                    if a_face is not None:
                        # faces touching must be black
                        if cubes_faces[i][a_face] != '#' or cubes_faces[j][b_face] != '#':
                            valid = False
                            break
                if not valid:
                    break
            if not valid:
                continue

            # Check bicube faces colors
            # For each of 6 faces of bicube, all unit cube faces that lie on outside must be same colorful color
            # and colors all different on 6 faces

            face_colors = [None]*6
            # faces order of bicube same as our face index:
            # 0-front, 1-left, 2-bottom, 3-right, 4-top, 5-back

            # Check faces on the outside of bicube cube (2x2x2)
            # For each cube face that is on the boundary of the cube (x,y,z in 0..1):
            # Face is outside if on the outer side: for example x=0 left face is outside
            # mapping:
            # front (0) outer if z=0
            # back (5) outer if z=1
            # left (1) outer if x=0
            # right (3) outer if x=1
            # bottom (2) outer if y=0
            # top (4) outer if y=1

            for i in range(8):
                x,y,z = dic_pos[i]
                faces = cubes_faces[i]
                # front
                if z == 0:
                    c = faces[0]
                    if c == '#' or c == '.':
                        valid = False
                        break
                    if face_colors[0] is None:
                        face_colors[0] = c
                    elif face_colors[0] != c:
                        valid = False
                        break
                # back
                if z == 1:
                    c = faces[5]
                    if c == '#' or c == '.':
                        valid = False
                        break
                    if face_colors[5] is None:
                        face_colors[5] = c
                    elif face_colors[5] != c:
                        valid = False
                        break
                # left
                if x == 0:
                    c = faces[1]
                    if c == '#' or c == '.':
                        valid = False
                        break
                    if face_colors[1] is None:
                        face_colors[1] = c
                    elif face_colors[1] != c:
                        valid = False
                        break
                # right
                if x == 1:
                    c = faces[3]
                    if c == '#' or c == '.':
                        valid = False
                        break
                    if face_colors[3] is None:
                        face_colors[3] = c
                    elif face_colors[3] != c:
                        valid = False
                        break
                # bottom
                if y == 0:
                    c = faces[2]
                    if c == '#' or c == '.':
                        valid = False
                        break
                    if face_colors[2] is None:
                        face_colors[2] = c
                    elif face_colors[2] != c:
                        valid = False
                        break
                # top
                if y == 1:
                    c = faces[4]
                    if c == '#' or c == '.':
                        valid = False
                        break
                    if face_colors[4] is None:
                        face_colors[4] = c
                    elif face_colors[4] != c:
                        valid = False
                        break
            if not valid:
                continue
            # Check that all 6 face colors are different
            if len(set(face_colors)) != 6:
                continue
            # all conditions met
            found = True
            break
        if found:
            break
    if found:
        break

if found:
    print("Yes")
else:
    print("No")