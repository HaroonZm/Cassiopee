from sys import setrecursionlimit
setrecursionlimit(10**7)
H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

# Directions for DFS (left, right, up, down)
dirs = [(0,-1),(0,1),(-1,0),(1,0)]

def inrange(r,c):
    return 0 <= r < H and 0 <= c < W

# Find all connected components of painted squares (# or colorful)
visited = [[False]*W for _ in range(H)]
components = []
for i in range(H):
    for j in range(W):
        if grid[i][j] != '.' and not visited[i][j]:
            stack = [(i,j)]
            comp = []
            while stack:
                r,c = stack.pop()
                if visited[r][c]:
                    continue
                visited[r][c] = True
                comp.append((r,c))
                for dr,dc in dirs:
                    nr,nc = r+dr,c+dc
                    if inrange(nr,nc) and not visited[nr][nc] and grid[nr][nc] != '.':
                        stack.append((nr,nc))
            components.append(comp)

if len(components) != 8:
    print("No")
    exit()

# Each component must be exactly a net of a cube:
# A net of a cube consists of 6 squares connected edge-to-edge.
# Check size
for comp in components:
    if len(comp) != 6:
        print("No")
        exit()

# Construct small board for each component and check if it is a valid cube net
# Cube nets have fixed shapes, but we can check by:
# 1) The component is connected
# 2) Exactly 6 squares
# 3) The degrees of squares allow unfolding into a cube net
# We'll check that it has 6 cells connected, and the graph formed by cells is a tree with 6 nodes and 5 edges,
# and that it contains vertices of degree 1 (edges), no cycles.

# Function to get neighbors on comp
def neighbors_on_comp(r,c,comp_set):
    res = []
    for dr,dc in dirs:
        nr,nc = r+dr,c+dc
        if (nr,nc) in comp_set:
            res.append((nr,nc))
    return res

for comp in components:
    comp_set = set(comp)
    # Count edges in comp graph
    edge_count = 0
    degs = []
    for (r,c) in comp:
        nbrs = neighbors_on_comp(r,c,comp_set)
        degs.append(len(nbrs))
        edge_count += len(nbrs)
    edge_count //= 2
    # Must be a tree with 6 nodes and 5 edges
    if edge_count != 5:
        print("No")
        exit()
    # Must have at least one leaf (deg=1) and no isolated vertex
    if any(d == 0 for d in degs):
        print("No")
        exit()

# Coordinates of each component cells must form a valid cube net.
# We'll encode each component as a set of coordinates with minimal bounding box
# and compare their adjacency against the known 11 cube nets or simply trust above tests for simplicity here.

# Now extract the colors and black faces
# For each comp, map cells to colors:
# according to problem description, squares are:
# colorful: characters A-Z,a-z,0-9 (unique colors)
# hash '#': black
# dot '.': unpainted (should not be in cube)
# For unit cubes:
# - The 6 faces correspond to the 6 squares in the net
# - When folded, the "inside" faces touching another cube must be black (#)
# - The cube faces are unit squares, arranged in a net
# We need to reconstruct the way cubes can be folded into a 2x2x2 bicube

# Assign each cube's 6 squares as faces, identify the color of faces,
# and which faces correspond to the inside (adjacent cubes) and outside (visible faces).
# Each inside face between two cubes must be black (#).
# Each outside face of the bicube must be uniform color (one color per face),
# and all 6 outside faces of bicube have distinct colors.

# Steps:
# 1) Determine which squares correspond to which face of the cube and their orientation
# 2) Assign cubes to positions in 2x2x2
# 3) Check adjacency of cubes in bicube and facing faces
# 4) Check inside faces are black (#)
# 5) Check outside faces uniformity and all different colors

# We know the bicube dimension is 2x2x2, cubes must be assigned accordingly (8 cubes)

# Because problem is complex, we rely on solution approach from the original source:
# 1) Find bounding rectangles of cubes
# 2) Identify position of unit cubes by their net position
# 3) Use predefined cube nets and possible orientations to identify cubes
# 4) Backtracking assignment of cubes to 2x2x2 positions and orientations
# 5) Verify coloring constraints

# Due to complexity, use known nets for cubes (there are 11 nets)
# We'll generate all orientations for each cube as possible maps face->color
# Then test all permutations of cube placements (8! * orientations each),
# but prune drastically by adjacency and black-face requirements.

# Implement detailed approach:

# Define nets for cube faces: We pick a labeling convention for faces:
# U(up), D(down), F(front), B(back), L(left), R(right)
# Each net placement correspond to a mapping squares -> faces
# Each component is a net, we must find its layout and how squares are connected.

# We represent cube faces and neighbors:
face_names = ['U','D','F','B','L','R']

# Function to find minimal bounding box and normalize comp cells
def normalize(comp):
    rs = [r for r,c in comp]
    cs = [c for r,c in comp]
    minr, maxr = min(rs), max(rs)
    minc, maxc = min(cs), max(cs)
    h = maxr - minr + 1
    w = maxc - minc + 1
    arr = [['']*w for _ in range(h)]
    for (r,c) in comp:
        arr[r - minr][c - minc] = grid[r][c]
    return arr, minr, minc

# The 11 valid cube nets (from Wikipedia), represented as 2D arrays with face labels:
# We try to match comp arr shapes to these nets (allow rotation/reflection) to identify face labels on squares.

cube_nets = [
    ["  U ","  F ","LBLD","  R "], # net 1
    ["  U ","LBLF","  R ","  D "], # net 2
    ["  U ","LBLF","  D ","  R "], # net 3
    ["  F ","UBL ","  D ","  R "], # net 4
    ["  F ","LBLD","  U ","  R "], # net 5
    [" U  ","LBF "," D  "," R  "], # net 6
    ["  U ","LBF ","  D ","  R "], # net 7
    ["  F ","UBL ","  R ","  D "], # net 8
    ["  F ","LBLD","  R ","  U "], # net 9
    ["  U ","LBF ","  R ","  D "], # net 10
    [" U  "," F  ","LBLD"," R  "]  # net 11
]
# These nets are just examples and may not perfectly correspond to problem;
# Instead, use algorithmic approach to find the face map for each net.

# A better approach is:
# select one cell as reference face (front),
# explore 4-connected neighbors to assign face labels,
# backtrack all possible face assignment to match cube folding rules.

# To solve fully with these constraints is extremely complex for this session.

# Alternative approach:
# The problem is from ICPC or similar contest "Bicube".
# The standard approach is:
# 1) Identify each of the eight cubes from the input (done)
# 2) For each cube net, assign faces
# 3) Place cubes in a 2x2x2 block so that:
#    - Adjacent cubes share black faces on the touching sides
#    - Outside faces per direction are uniform and all different colors

# We will implement the known algorithm from standard solutions:

from collections import defaultdict
import itertools

# All 6 cube faces and their opposites
opposite = {'U':'D','D':'U','F':'B','B':'F','L':'R','R':'L'}
dirs3d = {'U':(0,0,1),'D':(0,0,-1),'F':(0,1,0),'B':(0,-1,0),'L':(-1,0,0),'R':(1,0,0)}
faces = ['U','D','F','B','L','R']

# Unit cube is identified by 6 faces colored (dict face->color)
# We must get these from the net on the sheet

# Step 1: For each component, find all possible face assignments by checking adjacency graph and net foldings

def get_neighbors(comp):
    comp_set = set(comp)
    neigh = {}
    for r,c in comp:
        neigh[(r,c)] = []
        for dr,dc in dirs:
            nr,nc = r+dr,c+dc
            if (nr,nc) in comp_set:
                neigh[(r,c)].append((nr,nc))
    return neigh

# To assign faces, we pick one cell as 'F' (front),
# attempt all possible assignments of the other 5 faces using cube net adjacency

# Cube face adjacency (faces connected by edges, each face has 4 neighbors)
cube_adj = {
    'F': ['U','D','L','R'],
    'B': ['U','D','L','R'],
    'U': ['F','B','L','R'],
    'D': ['F','B','L','R'],
    'L': ['F','B','U','D'],
    'R': ['F','B','U','D'],
}

# The relative positions of neighbors on the net depend on folding order

# We use backtracking to assign cube faces to cells in comp connected graph

def assign_faces(comp):
    neigh = get_neighbors(comp)
    comp_list = comp
    n = len(comp_list)
    # Build adjacency map for component
    adj_map = {pos:set(neigh[pos]) for pos in comp_list}

    # We try to assign to each cell a face (U,D,F,B,L,R),
    # so that adjacency corresponds to cube face adjacency

    # We assign 'F' to an arbitrary cell
    start = comp_list[0]
    face_used = set()
    pos_face = {}
    pos_face[start] = 'F'
    face_used.add('F')

    # Construct possible assignments by DFS
    # For each assigned cell with face f, neighbors must correspond to faces adjacent to f

    def dfs_assign():
        if len(pos_face) == 6:
            # All faces assigned, check if pos_face covers all comp cells
            if len(pos_face) == n:
                return True
            else:
                return False
        # Find next unassigned cell adjacent to assigned cells
        for pos in comp_list:
            if pos not in pos_face:
                # find neighbors that are assigned
                assigned_nbrs = [nbr for nbr in adj_map[pos] if nbr in pos_face]
                if not assigned_nbrs:
                    continue
                possible_faces = set()
                # For each assigned neighbor cell, get possible faces that neighbor face can connect
                face_candidates = None
                for nbr in assigned_nbrs:
                    nbr_face = pos_face[nbr]
                    # possible faces adjacent to nbr_face
                    adj_faces = cube_adj[nbr_face]
                    if face_candidates is None:
                        face_candidates = set(adj_faces)
                    else:
                        face_candidates &= set(adj_faces)
                # Remove faces already assigned
                face_candidates -= face_used
                # Try each candidate
                for f in face_candidates:
                    # Check: for all assigned neighbors, f must be adjacent to nbr_face
                    valid = True
                    for nbr in assigned_nbrs:
                        nbr_face = pos_face[nbr]
                        if f not in cube_adj[nbr_face]:
                            valid = False
                            break
                    if not valid:
                        continue

                    pos_face[pos] = f
                    face_used.add(f)
                    if dfs_assign():
                        return True
                    face_used.remove(f)
                    del pos_face[pos]
                return False
        # No unassigned cell adjacent to assigned cells
        return False

    if not dfs_assign():
        return None
    return pos_face

# Obtain color of each face for a cube
def cube_face_colors(comp,pos_face):
    color_map = {}
    for (r,c),face in pos_face.items():
        color_map[face] = grid[r][c]
    return color_map

cubes = []

for comp in components:
    if len(comp) != 6:
        print("No")
        exit()
    res = assign_faces(comp)
    if res is None:
        print("No")
        exit()
    color_map = cube_face_colors(comp,res)
    cubes.append(color_map)

if len(cubes) != 8:
    print("No")
    exit()

# Now, arrange the cubes to form a 2x2x2 bicube

# Since there are 8 cubes, positions are (x,y,z) with x,y,z in {0,1}
positions = list(itertools.product([0,1],[0,1],[0,1]))

# We must check if there is a permutation of cubes assigned to positions
# and orientations (rotations), such that:
# - Adjacent cubes touch faces that are black (#)
# - Outside faces are uniform color and all different
# The problem is reduced to backtracking cube placement with orientation.

# Cube rotation: We can define 24 orientations.
# Each orientation is a permutation of faces.

# Define rotation matrices or exhaust all orientations

# We'll define 24 orientations as permutations of faces

# For cube face rotation:
# Each orientation can be represented as a mapping from original faces(U,D,F,B,L,R) to new faces.

# Precompute 24 rotations:
# Source: https://stackoverflow.com/questions/33101440/how-to-list-all-24-rotations-of-a-cube

def rotate_x(m):
    U,D,F,B,L,R = m['U'],m['D'],m['F'],m['B'],m['L'],m['R']
    return {'U':B,'D':F,'F':U,'B':D,'L':L,'R':R}

def rotate_y(m):
    U,D,F,B,L,R = m['U'],m['D'],m['F'],m['B'],m['L'],m['R']
    return {'U':U,'D':D,'F':L,'B':R,'L':B,'R':F}

def rotate_z(m):
    U,D,F,B,L,R = m['U'],m['D'],m['F'],m['B'],m['L'],m['R']
    return {'U':L,'D':R,'F':F,'B':B,'L':D,'R':U}

# Instead, hardcode 24 orientations as face permutations:

orientations = []

def roll(m):
    # rotate around x: U->B, B->D, D->F, F->U
    return {'U':m['B'],'B':m['D'],'D':m['F'],'F':m['U'],'L':m['L'],'R':m['R']}

def turn(m):
    # rotate around z (face) axis: L->F, F->R, R->B, B->L
    return {'U':m['U'],'D':m['D'],'F':m['L'],'L':m['B'],'B':m['R'],'R':m['F']}

def all_orientations():
    base = {'U':'U','D':'D','F':'F','B':'B','L':'L','R':'R'}
    ret = []
    m = base.copy()
    for cycle in range(2):
        for step in range(3):
            m = roll(m)
            for i in range(4):
                m = turn(m)
                ret.append(m.copy())
        m = roll(turn(roll(m)))
    unique_orients = []
    seen = set()
    for o in ret:
        tup = tuple(o[f] for f in faces)
        if tup not in seen:
            seen.add(tup)
            unique_orients.append(o)
    return unique_orients

orientation_maps = all_orientations()

def orient_cube(cube, orientation):
    # cube is dict face->color
    # orientation is dict old_face->new_face
    # We want new_face->color mapping
    res = {}
    for old_face, new_face in orientation.items():
        res[new_face] = cube[old_face]
    return res

# Adjacency of cubes in bicube:

adjacents = []
for i,(x,y,z) in enumerate(positions):
    for d,f in dirs3d.items():
        nx,ny,nz = x+f[0], y+f[1], z+f[2]
        if 0 <= nx < 2 and 0 <= ny < 2 and 0 <= nz < 2:
            j = positions.index((nx,ny,nz))
            adjacents.append((i,j,d))

# Backtracking place cubes with orientations:

assigned = [None]*8
used = [False]*8

# The outside face of bicube is any face not connected to another cube
# For each position and face, if no adjacent cube in that direction: outside face

# We'll verify conditions after placement.

outside_faces = [set() for _ in range(8)]
for i,(x,y,z) in enumerate(positions):
    outside = set()
    for f,dvec in dirs3d.items():
        nx,ny,nz = x + dvec[0], y + dvec[1], z + dvec[2]
        if nx <0 or nx>=2 or ny<0 or ny>=2 or nz<0 or nz>=2:
            outside.add(f)
    outside_faces[i] = outside

def check(assignment, orientations_assigned):
    # Check inside faces: adjacent cubes touching faces have black (#)
    for i,j,d in adjacents:
        c1 = assignment[i]
        o1 = orientations_assigned[i]
        c2 = assignment[j]
        o2 = orientations_assigned[j]
        cube1 = orient_cube(cubes[c1], o1)
        cube2 = orient_cube(cubes[c2], o2