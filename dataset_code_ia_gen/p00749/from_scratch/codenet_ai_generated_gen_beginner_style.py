def main():
    import sys
    sys.setrecursionlimit(10000)
    input_lines = sys.stdin.read().splitlines()
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        w_h = input_lines[idx].strip()
        idx += 1
        if w_h == "0 0":
            break
        w, h = map(int, w_h.split())
        grid = []
        for _ in range(h):
            grid.append(input_lines[idx])
            idx += 1

        # The grid has h rows and w columns, with (0,0) at bottom-left
        # but input lines are from top to bottom (y = h-1 is top)
        # Let's transform to a coordinate system: blocks at (x,y) with y from 0 at bottom
        # We invert lines to get bottom line at index 0
        grid = grid[::-1]

        # Each cell is either '.' or digit '1' to '9'
        # Pieces are groups of connected blocks with same digit and touching by sides
        visited = [[False]*w for _ in range(h)]
        pieces = []
        # Each piece: list of coordinates [(x,y)]
        def neighbors(x,y):
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < w and 0 <= ny < h:
                    yield nx, ny

        # Because two different pieces can have same digit if separated
        # So each connected component of same digit is a separate piece
        for y in range(h):
            for x in range(w):
                if grid[y][x] != '.' and not visited[y][x]:
                    digit = grid[y][x]
                    stack = [(x,y)]
                    visited[y][x] = True
                    comp = []
                    while stack:
                        cx, cy = stack.pop()
                        comp.append((cx, cy))
                        for nx, ny in neighbors(cx, cy):
                            if not visited[ny][nx] and grid[ny][nx] == digit:
                                visited[ny][nx] = True
                                stack.append((nx, ny))
                    pieces.append(comp)

        # Build a map from block to piece id
        block_to_piece = {}
        for i, piece in enumerate(pieces):
            for (x,y) in piece:
                block_to_piece[(x,y)] = i

        # Find parent piece for each piece (the one it touches below)
        # Each piece except one touches exactly one piece below or ground
        # For each piece find which piece(s) it supports or is supported by

        # piece_supports[i] = list of pieces supported by piece i (children in tree)
        piece_supports = [[] for _ in range(len(pieces))]
        # parent_of[i] = piece id of parent
        parent_of = [None]*len(pieces)

        # For each piece, find if it touches ground or piece below on bottom faces
        # bottom blocks: those with y block=0 or bottom face touches another block
        # Check blocks in piece with blocks below them
        for i, piece in enumerate(pieces):
            # For each block in piece check block below if none:
            # if y=0 => touches ground
            # else if there is a block below belonging to a different piece => that piece is parent
            parent_found = False
            for (x,y) in piece:
                if y == 0:
                    # touches ground
                    continue
                below = (x, y-1)
                if below in block_to_piece:
                    other_piece = block_to_piece[below]
                    if other_piece != i:
                        parent_of[i] = other_piece
                        piece_supports[other_piece].append(i)
                        parent_found = True
            # If no block touches another piece below, must be on ground
            if not parent_found:
                parent_of[i] = None

        # Find root piece on ground
        roots = [i for i,p in enumerate(parent_of) if p is None]

        # For center of mass calculation we need to compute recursively for each piece
        # x_L and x_R: leftmost and rightmost x coordinate of bottom touching blocks
        # M: x coordinate of accumulated center of mass (piece + all below it)

        # Calculate piece_weight and center_x for each piece and the accumulated values recursively

        # First, for each piece find its blocks
        # weight of piece = number of blocks
        # center_x_piece = average of center(x) of blocks (center at x+0.5)
        # For accumulated, weight accumulated = piece weight + sum of children weights
        # center_x_accum = weighted average center x of piece + children

        piece_weight = []
        piece_center_x = []
        # bottom blocks: blocks that touch bottom faces of this piece and the piece below or ground
        # To find x_L and x_R we need bottom blocks of the piece, i.e. blocks which are on bottom faces of piece,
        # that is blocks which have no block of this piece below them

        # find bottom blocks of each piece
        bottom_blocks = []
        for piece in pieces:
            block_set = set(piece)
            bottoms = []
            for (x,y) in piece:
                if (x,y-1) not in block_set:
                    bottoms.append((x,y))
            bottom_blocks.append(bottoms)

        for piece in pieces:
            # center_x of piece: average of block centers
            s = 0.0
            for (x,y) in piece:
                s += x + 0.5
            piece_center_x.append(s / len(piece))
            piece_weight.append(len(piece))

        # We compute accumulated center x and weight recursively
        # store results in cache
        acc_center_x = [None]*len(pieces)
        acc_weight = [None]*len(pieces)

        def dfs_acc(i):
            if acc_center_x[i] is not None:
                return acc_center_x[i], acc_weight[i]
            w_sum = piece_weight[i]
            mx_sum = piece_center_x[i]*piece_weight[i]
            for c in piece_supports[i]:
                mc, wc = dfs_acc(c)
                w_sum += wc
                mx_sum += mc*wc
            acc_weight[i] = w_sum
            acc_center_x[i] = mx_sum / w_sum
            return acc_center_x[i], acc_weight[i]

        for i in range(len(pieces)):
            dfs_acc(i)

        # Now check for stability of each piece
        # For each piece find xL and xR from bottom blocks:
        # xL = min x coordinate of leftmost block among bottom blocks of piece
        # xR = max x coordinate of rightmost block among bottom blocks of piece
        # The center M of accumulated center of mass must satisfy xL < M < xR strictly
        # If any piece fails => UNSTABLE else STABLE

        stable = True
        for i in range(len(pieces)):
            bottoms = bottom_blocks[i]
            if not bottoms:
                # no bottom blocks? should not happen but consider unstable
                stable = False
                break
            xL = min(x for (x,y) in bottoms)
            xR = max(x+1 for (x,y) in bottoms)  # right edge is x+1 because blocks occupy from x to x+1
            M = acc_center_x[i]
            if not (xL < M < xR):
                stable = False
                break

        if stable:
            print("STABLE")
        else:
            print("UNSTABLE")

if __name__ == "__main__":
    main()