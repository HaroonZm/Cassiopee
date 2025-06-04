def petoris():
    import sys

    input = sys.stdin.readline

    def rotate(shape):
        # Rotate a shape 90 degrees clockwise
        H, W = len(shape), len(shape[0])
        rotated = []
        for c in range(W):
            new_row = ''.join(shape[H - 1 - r][c] for r in range(H))
            rotated.append(new_row)
        return rotated

    def trim(shape):
        # Remove empty rows and columns around the shape
        rows = len(shape)
        cols = len(shape[0])
        top, bottom = 0, rows - 1
        while top <= bottom and all(c == '.' for c in shape[top]):
            top += 1
        while bottom >= top and all(c == '.' for c in shape[bottom]):
            bottom -= 1
        if top > bottom:
            return []

        left, right = 0, cols - 1
        while left <= right and all(shape[r][left] == '.' for r in range(top, bottom + 1)):
            left += 1
        while right >= left and all(shape[r][right] == '.' for r in range(top, bottom + 1)):
            right -= 1
        if left > right:
            return []

        return [shape[r][left:right + 1] for r in range(top, bottom + 1)]

    def shape_to_coords(shape):
        # Convert shape to list of coordinates of '#' relative to (0,0)
        coords = []
        for r, row in enumerate(shape):
            for c, ch in enumerate(row):
                if ch == '#':
                    coords.append((r, c))
        return coords

    N = int(input())

    for _ in range(N):
        # Read block shape
        Hb, Wb = map(int, input().split())
        block = [input().rstrip('\n') for __ in range(Hb)]
        block = trim(block)  # trim block shape
        # Generate all 4 rotated variants of the block
        variants = []
        base = block
        for __ in range(4):
            # trim each rotation to remove surrounding empty rows and columns
            base = trim(base)
            if base not in variants:
                variants.append(base)
            base = rotate(base)

        # Read board
        Hb_, Wb_ = map(int, input().split())
        board = [list(input().rstrip('\n')) for __ in range(Hb_)]
        board_rows = Hb_
        board_cols = Wb_

        def can_place(r0, c0, variant_coords):
            # Check if block can be placed at (r0, c0) on board without collision and inside the board
            for (r, c) in variant_coords:
                rr = r0 + r
                cc = c0 + c
                if rr < 0 or rr >= board_rows or cc < 0 or cc >= board_cols:
                    return False
                if board[rr][cc] == '#':
                    return False
            return True

        def place_block(r0, c0, variant_coords):
            # Place block on board copy and return this new board
            new_board = [row[:] for row in board]
            for (r, c) in variant_coords:
                rr = r0 + r
                cc = c0 + c
                new_board[rr][cc] = '#'
            return new_board

        def count_full_rows(b):
            # Count how many full rows (all '#') in this board
            cnt = 0
            for row in b:
                if all(ch == '#' for ch in row):
                    cnt += 1
            return cnt

        max_score = -1
        # Try to place the block in all possible positions and rotations
        for variant in variants:
            coords = shape_to_coords(variant)
            h_var = len(variant)
            w_var = len(variant[0])
            # Try all top-left positions (r0,c0)
            for r0 in range(board_rows - h_var + 1):
                for c0 in range(board_cols - w_var + 1):
                    if can_place(r0, c0, coords):
                        new_board = place_block(r0, c0, coords)
                        score = count_full_rows(new_board)
                        if score > max_score:
                            max_score = score

        print(max_score)

petoris()