def rotate(block):
    H = len(block)
    W = len(block[0])
    new_block = []
    for c in range(W):
        new_row = ''
        for r in range(H-1, -1, -1):
            new_row += block[r][c]
        new_block.append(new_row)
    return new_block

def get_tiles(block):
    tiles = []
    for r in range(len(block)):
        for c in range(len(block[0])):
            if block[r][c] == '#':
                tiles.append((r,c))
    return tiles

def can_place(board, block_tiles, start_r, start_c):
    H = len(board)
    W = len(board[0])
    for (br, bc) in block_tiles:
        r = start_r + br
        c = start_c + bc
        if r < 0 or r >= H or c < 0 or c >= W:
            return False
        if board[r][c] == '#':
            return False
    return True

def place_block(board, block_tiles, start_r, start_c):
    new_board = [list(row) for row in board]
    for (br, bc) in block_tiles:
        r = start_r + br
        c = start_c + bc
        new_board[r][c] = '#'
    return [''.join(row) for row in new_board]

def count_full_lines(board):
    count = 0
    for row in board:
        if all(ch == '#' for ch in row):
            count += 1
    return count

N = int(input())
for _ in range(N):
    # Read block
    BH, BW = map(int, input().split())
    block = [input() for _ in range(BH)]

    # Read board
    BH2, BW2 = map(int, input().split())
    board = [input() for _ in range(BH2)]

    # Generate all rotations of block (max 4)
    rotations = []
    current = block
    for _r in range(4):
        # Normalize block to top-left position (remove empty rows and columns)
        rows = [row for row in current if '#' in row]
        min_col = None
        max_col = -1
        for row in rows:
            for i, ch in enumerate(row):
                if ch == '#':
                    if min_col is None or i < min_col:
                        min_col = i
                    if i > max_col:
                        max_col = i
        new_block = []
        for row in rows:
            new_block.append(row[min_col:max_col+1])
        current = new_block

        # Avoid adding duplicates
        if current not in rotations:
            rotations.append(current)
        current = rotate(current)

    max_score = -1
    for rblock in rotations:
        block_tiles = get_tiles(rblock)
        BH_rot = len(rblock)
        BW_rot = len(rblock[0])
        for sr in range(BH2 - BH_rot +1):
            for sc in range(BW2 - BW_rot +1):
                if can_place(board, block_tiles, sr, sc):
                    new_board = place_block(board, block_tiles, sr, sc)
                    score = count_full_lines(new_board)
                    if score > max_score:
                        max_score = score
    print(max_score)