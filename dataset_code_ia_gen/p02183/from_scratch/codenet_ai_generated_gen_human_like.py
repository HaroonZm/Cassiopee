from sys import stdin
from itertools import combinations

H, W = 4, 10

def read_tetromino():
    h, w = map(int, stdin.readline().split())
    shape = [stdin.readline().strip() for _ in range(h)]
    blocks = []
    for r in range(h):
        for c in range(w):
            if shape[r][c] == '#':
                blocks.append((r, c))
    # Normalize positions to top-left-most block at (0,0)
    min_r = min(b[0] for b in blocks)
    min_c = min(b[1] for b in blocks)
    norm_blocks = [(r - min_r, c - min_c) for r,c in blocks]
    return (h, w, norm_blocks)

# Read 4 tetrominos
tetrominos = [read_tetromino() for _ in range(4)]

n = int(stdin.readline())
boards = []
for _ in range(n):
    board = [stdin.readline().strip() for __ in range(H)]
    boards.append(board)

def can_place(tetro_blocks, br, bc):
    for dr, dc in tetro_blocks:
        r, c = br + dr, bc + dc
        if not (0 <= r < H and 0 <= c < W):
            return False
    return True

def board_mask(board):
    mask = 0
    for r in range(H):
        for c in range(W):
            if board[r][c] == '#':
                mask |= 1 << (r*W + c)
    return mask

def tetro_masks(tetro):
    h, w, blocks = tetro
    positions = []
    for r in range(H - h + 1):
        for c in range(W - w + 1):
            pos_mask = 0
            for dr, dc in blocks:
                rr, cc = r+dr, c+dc
                pos_mask |= 1 << (rr*W + cc)
            positions.append(pos_mask)
    return positions

# Precompute all placement masks for each tetromino
tetro_pos_masks = [tetro_masks(t) for t in tetrominos]

full_board_mask = (1 << (H*W)) - 1

res = []
for board in boards:
    bmask = board_mask(board)
    # We must cover exactly all # positions on board with 3 tetrominos chosen from 4
    # Try all combinations of 3 distinct tetrominos
    found = False
    for comb in combinations(range(4), 3):
        # For each of these 3 tetros, try all placements and check if their union covers board_mask exactly, with no overlap
        m1_list = tetro_pos_masks[comb[0]]
        m2_list = tetro_pos_masks[comb[1]]
        m3_list = tetro_pos_masks[comb[2]]
        # We try all placements triple nested with pruning by masks
        for m1 in m1_list:
            if (m1 & bmask) != m1:
                continue
            for m2 in m2_list:
                if (m2 & bmask) != m2:
                    continue
                if m1 & m2:
                    continue
                union12 = m1 | m2
                if union12 == bmask:
                    # Already cover full board with two tetrominos? No because only 28 blocks = 7*4 -> need 3 tetrominos to make 28 blocks total
                    # So skip
                    continue
                for m3 in m3_list:
                    if (m3 & bmask) != m3:
                        continue
                    if m3 & union12:
                        continue
                    union123 = union12 | m3
                    if union123 == bmask:
                        found = True
                        break
                if found:
                    break
            if found:
                break
        if found:
            break
    res.append("Yes" if found else "No")

print('\n'.join(res))