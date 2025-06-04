H,W = map(int,input().split())
board = [list(input()) for _ in range(H)]
Q = int(input())
operations = [tuple(map(int,input().split())) for _ in range(Q)]

# directions for neighbors in a hex grid depending on row parity
def neighbors(x,y):
    # even rows (y even)
    if y % 2 == 0:
        return [(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y)]
    else:
        # odd rows (y odd)
        return [(x-1,y-1),(x,y-1),(x+1,y),(x,y+1),(x-1,y+1),(x-1,y)]

def inside(x,y):
    return 0 <= x < W and 0 <= y < H

def rotate_clockwise(cx,cy):
    # get neighbors coords
    ns = neighbors(cx,cy)
    # check all exist
    cells = [(cx,cy)] + ns
    for x,y in cells:
        if not inside(x,y):
            return
    # save colors of 6 neighbors
    colors = []
    for nx,ny in ns:
        colors.append(board[ny][nx])
    # rotate colors clockwise: put last at first
    colors = [colors[-1]] + colors[:-1]
    # put back rotated colors
    for i,(nx,ny) in enumerate(ns):
        board[ny][nx] = colors[i]

def fall_once():
    # try to apply one fall on the board
    changed = False
    # copy board to check movements
    new_board = [row[:] for row in board]

    # For each cell with a block, try to fall following the rule in Fig.3 (A->C if B,D empty)
    # For each hex cell, neighbors 0-5 as in neighbors()
    # Fig.3 shows: A at center, B and D are neighbors on 2 directions left and right (according to fig)
    # We interpret accordingly:
    # we'll check each block if it can fall to C position:
    # The falling rule: from A to C if B and D are empty (or non existent), and C exists
    # Here,
    # A is (x,y)
    # B and D are neighbors at indices 0 and 4 in neighbors list (i.e. neighbors[0], neighbors[4])
    # C is neighbors[3]
    for y in range(H):
        for x in range(W):
            A = board[y][x]
            if A == '.':
                continue
            ns = neighbors(x,y)
            # check positions B,D,C
            # B=ns[0], C=ns[3], D=ns[4]
            # check existence
            if not inside(*ns[3]):
                # if no C cell, no fall
                continue
            # if B or D out of board, consider empty
            B_empty = True
            if inside(*ns[0]):
                B_empty = board[ns[0][1]][ns[0][0]] == '.'
            D_empty = True
            if inside(*ns[4]):
                D_empty = board[ns[4][1]][ns[4][0]] == '.'
            # check C empty? no, it will be replaced by A, so no need to check if empty
            C_empty = board[ns[3][1]][ns[3][0]] == '.'
            if B_empty and D_empty and C_empty:
                # fall
                new_board[y][x] = '.'
                new_board[ns[3][1]][ns[3][0]] = A
                changed = True
    for y in range(H):
        for x in range(W):
            board[y][x] = new_board[y][x]
    return changed

def erase_same_color():
    # find connected components of same color with size >=3 and erase them
    visited = [[False]*W for _ in range(H)]
    to_erase = set()

    # neighbors for connectivity (6 directions)
    def adj(x,y):
        res = []
        for nx,ny in neighbors(x,y):
            if inside(nx,ny):
                res.append((nx,ny))
        return res

    for y in range(H):
        for x in range(W):
            if board[y][x] == '.' or visited[y][x]:
                continue
            color = board[y][x]
            stack = [(x,y)]
            comp = []
            visited[y][x] = True
            while stack:
                cx,cy = stack.pop()
                comp.append((cx,cy))
                for nx,ny in adj(cx,cy):
                    if not visited[ny][nx] and board[ny][nx] == color:
                        visited[ny][nx] = True
                        stack.append((nx,ny))
            if len(comp) >= 3:
                for pos in comp:
                    to_erase.add(pos)
    for x,y in to_erase:
        board[y][x] = '.'
    return len(to_erase) > 0

# convert initial board to have '.' for no block? No, initially all blocks exist.
# But problem statement says '.' means no block, so initial board always has blocks

# First, do the fall + erase process at initial state before operations
while True:
    changed1 = False
    while fall_once():
        changed1 = True
    changed2 = erase_same_color()
    if not changed1 and not changed2:
        break

for (cx,cy) in operations:
    rotate_clockwise(cx,cy)
    # after each rotation, run fall & erase until no change
    while True:
        changed1 = False
        while fall_once():
            changed1 = True
        changed2 = erase_same_color()
        if not changed1 and not changed2:
            break

for y in range(H):
    print(''.join(board[y]))