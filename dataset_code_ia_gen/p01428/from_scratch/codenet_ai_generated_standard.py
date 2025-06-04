def possible_moves(board, player):
    opponent = 'x' if player == 'o' else 'o'
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    moves = []
    for r in range(8):
        for c in range(8):
            if board[r][c] != '.':
                continue
            total_flip = 0
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                count = 0
                while 0 <= nr < 8 and 0 <= nc < 8 and board[nr][nc] == opponent:
                    nr += dr
                    nc += dc
                    count += 1
                if count > 0 and 0 <= nr < 8 and 0 <= nc < 8 and board[nr][nc] == player:
                    total_flip += count
            if total_flip > 0:
                moves.append((r,c,total_flip))
    return moves

def flip_cookies(board, r, c, player):
    opponent = 'x' if player == 'o' else 'o'
    board[r][c] = player
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        to_flip = []
        while 0 <= nr < 8 and 0 <= nc < 8 and board[nr][nc] == opponent:
            to_flip.append((nr,nc))
            nr += dr
            nc += dc
        if len(to_flip) > 0 and 0 <= nr < 8 and 0 <= nc < 8 and board[nr][nc] == player:
            for fr, fc in to_flip:
                board[fr][fc] = player

board = [list(input()) for _ in range(8)]
players = ['o','x']  # Mammi starts('o'), then Charlotte('x')
turn = 0

while True:
    player = players[turn%2]
    moves = possible_moves(board, player)
    if not moves:
        moves_other = possible_moves(board, players[(turn+1)%2])
        if not moves_other:
            break
        turn += 1
        continue
    # select move
    if player == 'o':
        moves.sort(key=lambda x: (x[0], x[1], -x[2]))  # top-left priority, flip max
        max_flip = max(m[2] for m in moves)
        candidates = [m for m in moves if m[2] == max_flip]
        chosen = min(candidates,key=lambda x:(x[0],x[1]))
    else:
        moves.sort(key=lambda x: (-x[0], -x[1], -x[2]))  # bottom-right priority, flip max
        max_flip = max(m[2] for m in moves)
        candidates = [m for m in moves if m[2] == max_flip]
        chosen = max(candidates,key=lambda x:(x[0],x[1]))
    flip_cookies(board, chosen[0], chosen[1], player)
    turn += 1

for row in board:
    print(''.join(row))