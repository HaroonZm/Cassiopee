import sys
from collections import deque

sys_readline = sys.stdin.readline
sys_write = sys.stdout.write

DIRS_BASE = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
DIRS_SET = []
for dirs_k in range(6):
    dirs_states = []
    for pos_y in range(dirs_k):
        for pos_x in range(dirs_k):
            mask_val = 0
            for dir_dx, dir_dy in DIRS_BASE:
                adj_x = pos_x + dir_dx
                adj_y = pos_y + dir_dy
                if not (0 <= adj_x < dirs_k and 0 <= adj_y < dirs_k):
                    continue
                mask_val |= 1 << (adj_y * dirs_k + adj_x)
            dirs_states.append(mask_val)
    DIRS_SET.append(dirs_states)

BITCOUNT_SIZE = (1 << 16)
BITCOUNT_LOOKUP = [0] * BITCOUNT_SIZE
for bitcount_idx in range(1, BITCOUNT_SIZE):
    BITCOUNT_LOOKUP[bitcount_idx] = BITCOUNT_LOOKUP[bitcount_idx ^ (bitcount_idx & -bitcount_idx)] + 1

def main_solver():
    grid_size = int(sys_readline())
    if grid_size == 0:
        return False
    move_dirs = DIRS_BASE
    adj_masks = DIRS_SET[grid_size]
    board_state = 0
    player_x, player_y = -1, -1
    for row_idx in range(grid_size):
        input_line = sys_readline().strip()
        for col_idx, cell_val in enumerate(input_line):
            if cell_val == '#':
                board_state |= 1 << (grid_size * row_idx + col_idx)
            elif cell_val == '@':
                player_x = col_idx
                player_y = row_idx
    visited_states = {(board_state, player_x, player_y): 0}
    bfs_queue = deque([(board_state, player_x, player_y)])
    while bfs_queue:
        curr_state, curr_x, curr_y = state_key = bfs_queue.popleft()
        curr_dist = visited_states[state_key]
        if curr_state == 0:
            sys_write(f"{curr_dist}\n")
            break
        for dir_dx, dir_dy in move_dirs:
            next_x = curr_x + dir_dx
            next_y = curr_y + dir_dy
            if not (0 <= next_x < grid_size and 0 <= next_y < grid_size):
                continue
            player_bit = 1 << (next_y * grid_size + next_x)
            if curr_state & player_bit:
                continue
            curr_state ^= player_bit
            next_state = 0
            for pos_idx in range(grid_size * grid_size):
                neighbors = curr_state & adj_masks[pos_idx]
                if curr_state & (1 << pos_idx):
                    if neighbors and 2 <= BITCOUNT_LOOKUP[neighbors // (neighbors & -neighbors)] <= 3:
                        next_state |= 1 << pos_idx
                else:
                    if neighbors and BITCOUNT_LOOKUP[neighbors // (neighbors & -neighbors)] == 3:
                        next_state |= 1 << pos_idx
            if next_state & player_bit:
                next_state ^= player_bit
            next_key = (next_state, next_x, next_y)
            if next_key not in visited_states:
                visited_states[next_key] = curr_dist + 1
                bfs_queue.append(next_key)
            curr_state ^= player_bit
    else:
        sys_write("-1\n")
    return True

while main_solver():
    pass