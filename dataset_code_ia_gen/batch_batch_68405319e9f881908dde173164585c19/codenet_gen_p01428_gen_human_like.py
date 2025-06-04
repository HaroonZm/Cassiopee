DIRS = [(-1,-1), (-1,0), (-1,1),
        (0,-1),          (0,1),
        (1,-1),  (1,0),  (1,1)]

def in_bounds(r,c):
    return 0 <= r < 8 and 0 <= c < 8

def opponent(player):
    return 'x' if player == 'o' else 'o'

def flips(board, r, c, player):
    if board[r][c] != '.':
        return []
    opp = opponent(player)
    flipped = []
    for dr, dc in DIRS:
        path = []
        nr, nc = r+dr, c+dc
        while in_bounds(nr,nc) and board[nr][nc] == opp:
            path.append((nr,nc))
            nr += dr
            nc += dc
        if path and in_bounds(nr,nc) and board[nr][nc] == player:
            flipped.extend(path)
    return flipped

def max_flip_positions(board, player):
    maxflips = 0
    candidates = []
    for r in range(8):
        for c in range(8):
            f = flips(board, r, c, player)
            if f:
                if len(f) > maxflips:
                    maxflips = len(f)
                    candidates = [(r,c)]
                elif len(f) == maxflips:
                    candidates.append((r,c))
    return maxflips, candidates

def play_turn(board, player):
    maxflips, candidates = max_flip_positions(board, player)
    if maxflips == 0:
        return False
    if player == 'o':
        # choose uppermost, then leftmost
        candidates.sort(key=lambda x: (x[0], x[1]))
    else:
        # player == 'x': choose downmost, then rightmost
        candidates.sort(key=lambda x: (-x[0], -x[1]))
    r, c = candidates[0]
    f = flips(board, r, c, player)
    board[r][c] = player
    for fr, fc in f:
        board[fr][fc] = player
    return True

board = [list(input()) for _ in range(8)]
turn_player = 'o'  # start with Mami who places chocolate cookie 'o'
while True:
    moved = play_turn(board, turn_player)
    turn_player = opponent(turn_player)
    if not moved:
        moved2 = play_turn(board, turn_player)
        if not moved2:
            break
        turn_player = opponent(turn_player)

for row in board:
    print(''.join(row))