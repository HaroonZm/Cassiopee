import sys
sys.setrecursionlimit(10**7)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def neighbors(x,y,w,h):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<w and 0<=ny<h:
            yield nx, ny

def main():
    input = sys.stdin.readline
    while True:
        w,h = map(int,input().split())
        if w==0 and h==0:
            break
        grid = [list(input().rstrip('\n')) for _ in range(h)]

        # Identify pieces by connectivity of blocks with same digit char
        # Since pieces labeled with digit chars can repeat but are different if not connected,
        # we assign unique piece ids to connected components of same digit chars.
        piece_id = [[-1]*w for _ in range(h)]
        current_id = 0

        for y in range(h):
            for x in range(w):
                if grid[y][x] != '.' and piece_id[y][x] == -1:
                    digit = grid[y][x]
                    stack = [(x,y)]
                    piece_id[y][x] = current_id
                    while stack:
                        cx, cy = stack.pop()
                        for nx, ny in neighbors(cx, cy, w, h):
                            if grid[ny][nx] == digit and piece_id[ny][nx] == -1:
                                piece_id[ny][nx] = current_id
                                stack.append((nx, ny))
                    current_id += 1

        n = current_id

        # For each piece, collect blocks: list of (x,y)
        blocks = [[] for _ in range(n)]
        for y in range(h):
            for x in range(w):
                pid = piece_id[y][x]
                if pid != -1:
                    blocks[pid].append( (x,y) )

        # The bottom of block (x,y=0) touches ground
        # Build graph from piece to pieces directly beneath it.
        # Since pieces stacked in a tree-like form, one piece touches ground,
        # and others touch exactly one piece beneath.
        # piece_supporters[pid]: list of piece ids directly supported by pid (on top)
        # We build reversed edges: parent->children (piece foundational supports)

        # For each piece, find which piece it directly supports or is supported by
        # Determine parent (supported piece) for each piece except root
        # For that:
        # For each block in piece, check if block under it exists and belongs to another piece
        # Then that piece is parent candidate.

        parent = [-1]*n
        children = [[] for _ in range(n)]
        for pid in range(n):
            # For each block in piece
            parents_found = set()
            for (x,y) in blocks[pid]:
                if y == 0:
                    # touches ground, no parent
                    continue
                below_pid = piece_id[y-1][x]
                if below_pid != -1 and below_pid != pid:
                    parents_found.add(below_pid)
            if len(parents_found) > 1:
                # According to problem statement, should not happen (tree-like)
                pass
            elif len(parents_found) == 1:
                p = parents_found.pop()
                parent[pid] = p
                children[p].append(pid)

        # Find root piece (which has no parent)
        root = -1
        for i in range(n):
            if parent[i] == -1:
                root = i
                break

        # We need to compute for each piece:
        # accumulated center of mass of pieces supported by it and itself:
        # Mx = total_mx / total_blocks
        # total_blocks: number of blocks in subtree
        # total_mx: sum of x-coords of centers of blocks in subtree

        # Also, for each piece, xL and xR: leftmost and rightmost x positions of bottom blocks that touch something beneath (ground or another piece)
        # Those touching blocks define the support segment, the M should lie strictly inside (xL < M < xR)

        # For each piece, find bottom blocks in it that contact ground or parent's blocks
        # For each block in piece, if y==0 -> touches ground
        # else if block below belongs to parent -> touches piece below

        # Note: support interval is defined by blocks touching below (bottom face touching ground or piece below)
        
        # We'll perform postorder DFS to compute accumulated mass and check stability bottom-up

        stable = True

        sys.setrecursionlimit(10**7)

        bottom_support = [ [] for _ in range(n) ]
        for pid in range(n):
            p = parent[pid]
            for (x,y) in blocks[pid]:
                if y == 0:
                    bottom_support[pid].append(x)
                elif parent[pid] == piece_id[y-1][x]:
                    bottom_support[pid].append(x)

        # Precompute centers of blocks of each piece: block centers x coordinate = x + 0.5
        # We store sum x+0.5 for own blocks for easier subtree aggregates
        # Subtree sum and count computed by DFS

        def dfs(pid):
            # accumulate sum_x and count from children
            own_blocks = blocks[pid]
            count = len(own_blocks)
            sum_x = sum(x+0.5 for x,y in own_blocks)
            for c in children[pid]:
                c_sum_x, c_count = dfs(c)
                sum_x += c_sum_x
                count += c_count
            # compute M for this piece
            M = sum_x / count

            # check stability
            bs = bottom_support[pid]
            if not bs:
                # no bottom support?
                # For root (ground), should have bottom blocks
                # Probably always have at least one bottom support
                # If no support, unstable
                nonlocal stable
                stable = False
                return sum_x, count
            xL = min(bs)
            xR = max(bs)+1  # x coordinate of right side of rightmost block
            # M must satisfy xL < M < xR strictly
            if not (xL < M < xR):
                stable = False
            return sum_x, count

        dfs(root)

        print("STABLE" if stable else "UNSTABLE")

if __name__ == "__main__":
    main()