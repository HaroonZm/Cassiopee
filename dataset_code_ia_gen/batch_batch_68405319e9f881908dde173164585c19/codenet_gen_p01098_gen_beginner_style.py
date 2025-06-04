import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline()

def neighbors_white(y,x,h,w):
    for ny,nx in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
        if 0<=ny<h and 0<=nx<w:
            yield ny,nx

def neighbors_black(y,x,h,w):
    for ny,nx in [(y-1,x-1),(y-1,x),(y-1,x+1),
                  (y,x-1),(y,x+1),
                  (y+1,x-1),(y+1,x),(y+1,x+1)]:
        if 0<=ny<h and 0<=nx<w:
            yield ny,nx

def find_components(image,h,w):
    color_map = {}
    comp_id = 1
    comps = {}
    visited = [[False]*w for _ in range(h)]
    # get background component id (white connected to border)
    # flood fill white from border pixels
    from collections import deque
    background = set()
    q = deque()
    for i in range(h):
        if image[i][0]=='.':
            q.append((i,0))
            background.add((i,0))
        if image[i][w-1]=='.':
            q.append((i,w-1))
            background.add((i,w-1))
    for j in range(w):
        if image[0][j]=='.':
            q.append((0,j))
            background.add((0,j))
        if image[h-1][j]=='.':
            q.append((h-1,j))
            background.add((h-1,j))
    while q:
        y,x = q.popleft()
        for ny,nx in neighbors_white(y,x,h,w):
            if image[ny][nx]=='.' and (ny,nx) not in background:
                background.add((ny,nx))
                q.append((ny,nx))
    comp_info = []
    comp_map = [[0]*w for _ in range(h)]
    # mark background component first with id 0
    for (y,x) in background:
        comp_map[y][x] = 0
    # Now find white and black components (except background) and assign ids starting from 1
    def dfs_white(sy,sx,cid):
        stack = [(sy,sx)]
        comp_pixels = []
        visited[sy][sx] = True
        comp_map[sy][sx] = cid
        comp_pixels.append((sy,sx))
        while stack:
            y,x = stack.pop()
            for ny,nx in neighbors_white(y,x,h,w):
                if not visited[ny][nx] and image[ny][nx]=='.' and (ny,nx) not in background:
                    visited[ny][nx] = True
                    comp_map[ny][nx] = cid
                    comp_pixels.append((ny,nx))
                    stack.append((ny,nx))
        return comp_pixels
    def dfs_black(sy,sx,cid):
        stack = [(sy,sx)]
        comp_pixels = []
        visited[sy][sx] = True
        comp_map[sy][sx] = cid
        comp_pixels.append((sy,sx))
        while stack:
            y,x = stack.pop()
            for ny,nx in neighbors_black(y,x,h,w):
                if not visited[ny][nx] and image[ny][nx]=='#':
                    visited[ny][nx] = True
                    comp_map[ny][nx] = cid
                    comp_pixels.append((ny,nx))
                    stack.append((ny,nx))
        return comp_pixels
    cid = 1
    # reset visited for non-background pixels
    for y in range(h):
        for x in range(w):
            if (y,x) not in background:
                visited[y][x] = False
    for y in range(h):
        for x in range(w):
            if not visited[y][x] and comp_map[y][x]==0 and image[y][x]=='.':
                # white non background component
                comp_pixels = dfs_white(y,x,cid)
                comp_info.append((cid,'.',comp_pixels))
                cid+=1
            elif not visited[y][x] and image[y][x]=='#':
                comp_pixels = dfs_black(y,x,cid)
                comp_info.append((cid,'#',comp_pixels))
                cid+=1
    # background component info with id 0
    background_pixels = list(background)
    comp_info = [(0,'.',background_pixels)] + comp_info
    return comp_info, comp_map

def is_surrounding(c1,c2,comp_info,comp_map,h,w):
    # c1 and c2 are component ids, colors differ
    # create modified image where all pixels outside c1 and c2 are replaced by c2's color
    # then find background component in that modified image
    # and check if c2 pixels are in background or not
    color_c1 = None
    color_c2 = None
    for cid,color,pixels in comp_info:
        if cid==c1:
            color_c1 = color
        if cid==c2:
            color_c2 = color
    if color_c1 is None or color_c2 is None:
        return False
    # build modified image
    modified = [[color_c2]*w for _ in range(h)]
    for cid,color,pixels in comp_info:
        if cid==c1 or cid==c2:
            for (y,x) in pixels:
                modified[y][x] = color
    # find background component in modified image by flood fill white from borders if color_c2=='.'
    from collections import deque
    visited = [[False]*w for _ in range(h)]
    q = deque()
    color_bg = color_c2
    background_pixels = set()
    def neighbors_mod(y,x):
        # neighborhood depends on color: white connectedness 4-neighbors, black 8-neighbors
        if color_bg=='.':
            for ny,nx in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
                if 0<=ny<h and 0<=nx<w:
                    yield ny,nx
        else:
            for ny,nx in [(y-1,x-1),(y-1,x),(y-1,x+1),
                          (y,x-1),(y,x+1),
                          (y+1,x-1),(y+1,x),(y+1,x+1)]:
                if 0<=ny<h and 0<=nx<w:
                    yield ny,nx
    # start from outside pixels depending on color
    # all border pixels which have color_bg
    for i in range(h):
        if modified[i][0]==color_bg:
            visited[i][0] = True
            q.append((i,0))
            background_pixels.add((i,0))
        if modified[i][w-1]==color_bg:
            visited[i][w-1] = True
            q.append((i,w-1))
            background_pixels.add((i,w-1))
    for j in range(w):
        if modified[0][j]==color_bg:
            visited[0][j] = True
            q.append((0,j))
            background_pixels.add((0,j))
        if modified[h-1][j]==color_bg:
            visited[h-1][j] = True
            q.append((h-1,j))
            background_pixels.add((h-1,j))
    while q:
        y,x = q.popleft()
        for ny,nx in neighbors_mod(y,x):
            if not visited[ny][nx] and modified[ny][nx]==color_bg:
                visited[ny][nx] = True
                q.append((ny,nx))
                background_pixels.add((ny,nx))
    # check if pixels of c2 are included in background component
    for (y,x) in comp_info[c2][2]:
        if (y,x) in background_pixels:
            return False
    return True

def read_image():
    h,w = map(int,input().split())
    if h==0 and w==0:
        return None,None,None
    img = []
    for _ in range(h):
        line = input().rstrip('\n')
        img.append(line)
    return h,w,img

def surrounding_relation(comp_info,comp_map,h,w):
    # build dictionary cid->color
    c_colors = {}
    for cid,color,pixels in comp_info:
        c_colors[cid] = color
    n = len(comp_info)
    # skip background component id=0 for some checks, but keep it
    # build around matrix: surrounding[c1][c2] True if c1 surrounds c2
    surrounding = {}
    for i in range(n):
        id1 = comp_info[i][0]
        surrounding[id1] = {}
        for j in range(n):
            id2 = comp_info[j][0]
            if id1 == id2:
                surrounding[id1][id2] = False
            elif c_colors[id1] != c_colors[id2]: # only between components of opposite colors
                # background component (id=0) cannot be checked if one is background?
                # by definition, c1 and c2 can't be background component (if either is background, surround is false)
                if id1==0 or id2==0:
                    surrounding[id1][id2] = False
                else:
                    surrounding[id1][id2] = is_surrounding(id1,id2,comp_info,comp_map,h,w)
            else:
                surrounding[id1][id2] = False
    return surrounding

def same_character(h1,w1,img1,h2,w2,img2):
    comp_info_1, comp_map_1 = find_components(img1,h1,w1)
    comp_info_2, comp_map_2 = find_components(img2,h2,w2)
    if len(comp_info_1) != len(comp_info_2):
        return False
    # components are numbered but may be in different order
    # first check color counts
    ccount1 = {}
    for cid,color,pixels in comp_info_1:
        ccount1[color] = ccount1.get(color,0)+1
    ccount2 = {}
    for cid,color,pixels in comp_info_2:
        ccount2[color] = ccount2.get(color,0)+1
    if ccount1 != ccount2:
        return False
    n = len(comp_info_1)
    # build surrounding relations
    sur1 = surrounding_relation(comp_info_1,comp_map_1,h1,w1)
    sur2 = surrounding_relation(comp_info_2,comp_map_2,h2,w2)
    # try all possible bijections matching colors of connected components
    from itertools import permutations
    # prepare lists per color to reduce search space
    list1 = {}
    list2 = {}
    for cid,color,pixels in comp_info_1:
        list1.setdefault(color,[]).append(cid)
    for cid,color,pixels in comp_info_2:
        list2.setdefault(color,[]).append(cid)
    # for each color, consider permutations of components of that color
    import itertools
    colors = list(list1.keys())
    # generate all mappings color-wise and combine
    candidates = [[]]
    for color in colors:
        c1list = list1[color]
        c2list = list2[color]
        perms = list(itertools.permutations(c2list))
        new_candidates = []
        for cand in candidates:
            for perm in perms:
                new_candidates.append(cand+list(zip(c1list,perm)))
        candidates = new_candidates
    # candidates is huge but, as beginner code, we keep it this way, may time out
    for mapping in candidates:
        mp = {}
        for c1,c2 in mapping:
            mp[c1]=c2
        # check surrounding equivalence for all pairs
        ok = True
        for i in range(n):
            for j in range(n):
                cid1 = comp_info_1[i][0]
                cid2 = comp_info_1[j][0]
                # relation in image1
                rel1 = sur1[cid1][cid2]
                # corresponding mapped cids
                mcid1 = mp[cid1]
                mcid2 = mp[cid2]
                rel2 = sur2[mcid1][mcid2]
                if rel1 != rel2:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return True
    return False

while True:
    h1,w1,img1 = read_image()
    if h1 is None:
        break
    h2,w2,img2 = read_image()
    if h2 is None:
        break
    if same_character(h1,w1,img1,h2,w2,img2):
        print("yes")
    else:
        print("no")