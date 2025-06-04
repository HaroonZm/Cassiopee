import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline()

# Directions for BFS/DFS
WHITE_DIRS = [(0,1),(0,-1),(1,0),(-1,0)]
BLACK_DIRS = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

def read_image():
    h,w = map(int,input().split())
    if h==0 and w==0:
        return None,None,None
    grid = [list(input().strip()) for _ in range(h)]
    return h,w,grid

def inside(h,w,y,x):
    return 0<=y<h and 0<=x<w

# Find connected components in the image.
# Returns: 
#  comp_list: list of components. Each component is set of pixels (y,x)
#  comp_map: 2D array with component indices, -1 if none
#  colors: list of colors ('.' or '#') for each component
def find_components(h,w,grid,color):
    comp_map = [[-1]*w for _ in range(h)]
    comp_list = []
    dirs = WHITE_DIRS if color=='.' else BLACK_DIRS
    visited = [[False]*w for _ in range(h)]
    comp_id = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x]==color and not visited[y][x]:
                stack = [(y,x)]
                comp = []
                visited[y][x] = True
                comp_map[y][x] = comp_id
                while stack:
                    cy,cx = stack.pop()
                    comp.append((cy,cx))
                    for dy,dx in dirs:
                        ny,nx = cy+dy,cx+dx
                        if inside(h,w,ny,nx) and not visited[ny][nx] and grid[ny][nx]==color:
                            visited[ny][nx] = True
                            comp_map[ny][nx] = comp_id
                            stack.append((ny,nx))
                comp_list.append(comp)
                comp_id+=1
    return comp_list,comp_map

def find_all_components(h,w,grid):
    white_comps, white_map = find_components(h,w,grid,'.')
    black_comps, black_map = find_components(h,w,grid,'#')

    # We will number components so that:
    # components indices: 0..wcnt-1 are white components
    # wcnt..wcnt+bcnt-1 are black components
    components = []
    colors = []
    for c in white_comps:
        components.append(set(c))
        colors.append('.')
    for c in black_comps:
        components.append(set(c))
        colors.append('#')
    comp_map = [[-1]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if white_map[y][x]>=0:
                comp_map[y][x] = white_map[y][x]
            elif black_map[y][x]>=0:
                comp_map[y][x] = len(white_comps)+black_map[y][x]
    return components,colors,comp_map

# Find background component: component of white pixels connected to outside
# White connected component including all pixels outside the image.
# It is white component at border, or synthesized outside
def find_background_component(h,w,grid):
    # create visited for white pixels (color '.')
    visited = [[False]*w for _ in range(h)]
    from collections import deque
    q = deque()
    # Mark all outside pixels as visited, simulate outside
    # Add all white pixels at edge to BFS
    for x in range(w):
        if grid[0][x] == '.':
            q.append((0,x))
            visited[0][x] = True
        if grid[h-1][x] == '.':
            q.append((h-1,x))
            visited[h-1][x] = True
    for y in range(h):
        if grid[y][0] == '.':
            q.append((y,0))
            visited[y][0] = True
        if grid[y][w-1] == '.':
            q.append((y,w-1))
            visited[y][w-1] = True
    while q:
        y,x = q.popleft()
        for dy,dx in WHITE_DIRS:
            ny,nx = y+dy,x+dx
            if 0<=ny<h and 0<=nx<w and grid[ny][nx]=='.' and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny,nx))
    # all visited white pixels at border or connected to outside are background white pixels
    bg_pixels = set()
    for y in range(h):
        for x in range(w):
            if visited[y][x]:
                bg_pixels.add((y,x))
    return bg_pixels

# Determine background component index: the white component containing any bg pixel
def get_background_index(components,colors,bg_pixels):
    for i,(c,color) in enumerate(zip(components,colors)):
        if color == '.' and not c.isdisjoint(bg_pixels):
            return i
    return -1

# Check if two sets surrounds each other by the problem definition
# C1 surrounds C2 means in the modified image (only pixels inside C1 or C2 keep colors)
#   - colors outside C1 and C2 changed to that of C2
#   - background color changed to C2 color if neither is background
#   - is C2 included in background or not in modified image
def surrounds(h,w,components,colors,comp_map,idx1,idx2,background_idx):
    C1 = components[idx1]
    C2 = components[idx2]
    color1 = colors[idx1]
    color2 = colors[idx2]
    # If idx1 or idx2 is background component, do not surround
    # Actually problem says: neither C1 nor C2 should be background component to consider modified image background conversion
    is_bg1 = (idx1 == background_idx)
    is_bg2 = (idx2 == background_idx)

    # Construct modified image pixels colors (only inside C1 or C2 keep original color)
    # All other pixels changed to color of C2
    # background component color also changed to color2, if neither C1 nor C2 is background
    # Construct modified image color map efficiently:
    # for each pixel:
    #   if in C1 or C2: keep original color
    #   else: color2

    # Build set of C1 and C2 pixels for quick lookup
    setC1 = C1
    setC2 = C2

    # Create an array indicating pixels color in modified image
    mod_color = [[color2]*w for _ in range(h)]
    for (y,x) in setC1:
        mod_color[y][x] = color1
    for (y,x) in setC2:
        mod_color[y][x] = color2

    # Identify connected white components in modified image with normal connectivity (4-dir) for white and (8-dir) for black
    # But we only need to know if pixels of C2 are connected to outside or NOT

    # To check if C2 pixels are included in background in modified image:
    # We find white connected component in modified image connected to outside (background)
    # Then if any pixel of C2 belongs to that background component, C2 is in background.

    # So find background pixels in modified image: white pixels connected to outside
    # Since outside is white, but in modified image some pixels may be black => We treat outside as white pixels.

    # First, get background pixels in modified image:
    visited = [[False]*w for _ in range(h)]
    from collections import deque
    q = deque()

    def is_white(c):
        return c=='.'

    # add border whites
    for x in range(w):
        if is_white(mod_color[0][x]) and not visited[0][x]:
            q.append((0,x))
            visited[0][x] = True
        if is_white(mod_color[h-1][x]) and not visited[h-1][x]:
            q.append((h-1,x))
            visited[h-1][x] = True
    for y in range(h):
        if is_white(mod_color[y][0]) and not visited[y][0]:
            q.append((y,0))
            visited[y][0] = True
        if is_white(mod_color[y][w-1]) and not visited[y][w-1]:
            q.append((y,w-1))
            visited[y][w-1] = True
    # BFS 4 directions for white connectedness
    while q:
        y,x = q.popleft()
        for dy,dx in WHITE_DIRS:
            ny,nx = y+dy,x+dx
            if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and is_white(mod_color[ny][nx]):
                visited[ny][nx] = True
                q.append((ny,nx))
    # Pixels visited == background white pixels in modified image

    # Check if any pixel of C2 is in background pixels
    # If yes, C1 does NOT surround C2 (definition)
    # If no, C1 surrounds C2 (definition)
    for (y,x) in setC2:
        if is_white(mod_color[y][x]) and visited[y][x]:
            return False
    # If C2 is black, background pixels are white so no pixel of C2 can be in background
    # So we only need to check if any C2 white pixels are in background pixels
    # So we also check if any black pixels of C2 are adjacent to background white pixels through toggling

    # Wait: The specification says "if neither C1 nor C2 is background component,
    # the color of the background component is changed to that of C2".
    # We handled this by making "outside" white pixels colored C2's color instead of white?

    # Actually in method, we recolored all out of C1 or C2 pixels as color2.
    # So outside is transformed to C2 color, so outside is either white or black, depends on color2.

    # This is already done.

    # So the above background BFS uses white pixels; does outside pixels have color white in modified image?
    # If C2 is black component, outside pixels get color black in modified image, i.e. no white pixels outside, no background white connected component
    # Then C2 is "connected to background" if any of its pixels connected to outside in the colored image?

    # So we must process the background in modified image as the connected component including pixels outside the image.
    # That is pixels of outside (outside image space) color2.

    # To model this precisely, we consider the neighbor connectivity.

    # If color2 is white '.', BFS background from outside works directly as above (BFS over white).

    # If color2 is black '#', no white pixels outside, so no BFS can start on white pixels for background.
    # So background component is all pixels outside image, color black.

    # In that case, white component background doesn't exist? But background component always exist.

    # According to problem definitions, white connected components are connected 4 directions,
    # black connected components 8 directions.

    # Background component is connected component including outside pixels.

    # So in modified image, background component is the component of color2 connected to outside.

    # So if color2 == '#', background component is black connected component connected to outside.

    # So need to BFS for color2 pixels connected to outside, connected with corresponding connectivity:

    conns = WHITE_DIRS if color2 == '.' else BLACK_DIRS
    visited = [[False]*w for _ in range(h)]
    q = deque()
    # Outside pixels: all outside image points -> simulate by adding border pixels with color color2
    # Find all pixels of color2 at the border (since these connect to outside color2 color)
    for i in range(h):
        if mod_color[i][0] == color2:
            q.append((i,0))
            visited[i][0] = True
        if mod_color[i][w-1] == color2:
            if not visited[i][w-1]:
                q.append((i,w-1))
                visited[i][w-1] = True
    for j in range(w):
        if mod_color[0][j] == color2:
            if not visited[0][j]:
                q.append((0,j))
                visited[0][j] = True
        if mod_color[h-1][j] == color2:
            if not visited[h-1][j]:
                q.append((h-1,j))
                visited[h-1][j] = True
    while q:
        y,x = q.popleft()
        for dy,dx in conns:
            ny,nx = y+dy,x+dx
            if 0<=ny<h and 0<=nx<w:
                if not visited[ny][nx] and mod_color[ny][nx] == color2:
                    visited[ny][nx] = True
                    q.append((ny,nx))

    # Now, background component is all visited pixels.

    # Check if any pixel of C2 is in background component
    for (y,x) in setC2:
        if visited[y][x]:
            return False
    # If no pixels of C2 are in background, then C1 surrounds C2
    return True

# Build graph of surround relations for an image: adjacency matrix where relation[i][j]=True if component i surrounds j
def build_surround_graph(h,w,components,colors,comp_map,background_idx):
    n = len(components)
    rel = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            # Only consider pairs of opposite colors
            if colors[i] != colors[j]:
                # Check surround relation
                if surrounds(h,w,components,colors,comp_map,i,j,background_idx):
                    rel[i][j] = True
    return rel

# Try to find a bijection f : S -> S' preserving colors and surround relations
# S and S' components
# colors, colors'
# rel, rel' adjacency matrix for surround relations
# Backtracking search for matching, exploiting colors
def check_isomorphism(components1,colors1,rel1,components2,colors2,rel2):
    n = len(components1)
    # Quick color count check
    from collections import Counter
    ccount1 = Counter(colors1)
    ccount2 = Counter(colors2)
    if ccount1 != ccount2:
        return False

    # For each component in img1, possible matches in img2 with the same color
    color_to_indices2 = {}
    for i,c in enumerate(colors2):
        color_to_indices2.setdefault(c,[]).append(i)
    # Prepare candidates list for each component in img1
    candidates = []
    for i,c in enumerate(colors1):
        candidates.append(color_to_indices2[c][:])

    # We will assign f[i] = j meaning component i in image1 maps to component j in image2
    f = [-1]*n
    used = [False]*n

    def consistent(i,j):
        # j candidate for i
        # check color already done by candidates filter
        # check surround relations with already assigned components
        for x in range(i):
            if f[x] == -1:
                continue
            # rel1[x][i] == True <=> rel2[f[x]][j] == True
            if rel1[x][i] != rel2[f[x]][j]:
                return False
            # rel1[i][x] == True <=> rel2[j][f[x]] == True
            if rel1[i][x] != rel2[j][f[x]]:
                return False
        return True

    def dfs(i):
        if i==n:
            return True
        for j in candidates[i]:
            if not used[j] and consistent(i,j):
                f[i] = j
                used[j] = True
                if dfs(i+1):
                    return True
                f[i] = -1
                used[j] = False
        return False

    return dfs(0)

def solve():
    while True:
        h1,w1,grid1 = read_image()
        if h1 is None:
            break
        h2,w2,grid2 = read_image()
        if h2 is None:
            break

        # Process image 1
        components1,colors1,comp_map1 = find_all_components(h1,w1,grid1)
        bg_pixels1 = find_background_component(h1,w1,grid1)
        bg_idx1 = get_background_index(components1,colors1,bg_pixels1)
        rel1 = build_surround_graph(h1,w1,components1,colors1,comp_map1,bg_idx1)

        # Process image 2
        components2,colors2,comp_map2 = find_all_components(h2,w2,grid2)
        bg_pixels2 = find_background_component(h2,w2,grid2)
        bg_idx2 = get_background_index(components2,colors2,bg_pixels2)
        rel2 = build_surround_graph(h2,w2,components2,colors2,comp_map2,bg_idx2)

        # Check same number of components
        if len(components1) != len(components2):
            print("no")
            continue

        # Check isomorphism
        if check_isomorphism(components1,colors1,rel1,components2,colors2,rel2):
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    solve()