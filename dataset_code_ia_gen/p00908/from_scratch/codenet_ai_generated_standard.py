from collections import deque

def solve_puzzle(H, W, grid):
    # Parse input grid, find king position, pawns, obstacles, and open squares
    # King is 2x2 squares marked 'X', pawns 'o', obstacles '*', open '.'
    # Exactly two open squares; moves slide king or pawns into open squares
    
    obstacles = set()
    pawns = set()
    open_squares = set()
    king_coords = set()
    
    for r in range(H):
        for c in range(W):
            ch = grid[r][c]
            if ch == '*':
                obstacles.add((r,c))
            elif ch == 'o':
                pawns.add((r,c))
            elif ch == '.':
                open_squares.add((r,c))
            elif ch == 'X':
                king_coords.add((r,c))
    
    # Identify top-left corner of king (2x2 'X')
    # King is always a 2x2 block of 'X's adjacent squares
    # We find minimal (r,c) of king_coords, and ensure the other three squares form a 2x2
    kr = min(p[0] for p in king_coords)
    kc = min(p[1] for p in king_coords)
    king = (kr, kc)  # position of king is top-left corner of 2x2 block
    
    # Validate king shape:
    king_set = {(kr, kc), (kr, kc+1), (kr+1, kc), (kr+1, kc+1)}
    if king_set != king_coords:
        # The input is invalid, but per problem statement this won't happen
        return -1

    # We track king position + pawns positions as state
    # State structure: (king_r, king_c, frozenset of pawns positions)
    # Open squares = exactly two open squares, which define empty spaces we can move into.
    # As pawns and king move into open squares, open squares move correspondingly.
    
    # Directions for adjacency
    DIRS = [(-1,0),(1,0),(0,-1),(0,1)]
    
    # Function to check if position is inside board
    def in_board(r,c):
        return 0 <= r < H and 0 <= c < W
    
    # Check if a position is free (not obstacle, not currently occupied by a pawn or king)
    def occupied(r,c, king_pos, pawns_set):
        if (r,c) in obstacles:
            return True
        # Check if in king 2x2 block
        kr,kc = king_pos
        if kr <= r <= kr+1 and kc <= c <= kc+1:
            return True
        if (r,c) in pawns_set:
            return True
        return False

    # Check if king can move in direction: king slides if both squares along edge move into open squares
    # For direction d, the two edge squares must be adjacent to two open squares
    # open squares are exactly two squares not occupied by pawns nor king nor obstacles
    # So open squares = ((H*W) - obstacles - pawns - king squares)
    # We'll recompute open squares after each move. Moving a pawn or king updates opens
    # But instead of tracking open squares, we can track king and pawns, the rest squares are known
    
    def king_can_move(king_pos, pawns_set, d):
        kr,kc = king_pos
        dr, dc = d
        nr, nc = kr + dr, kc + dc
        # new king squares
        new_squares = {(nr, nc), (nr, nc+1), (nr+1, nc), (nr+1, nc+1)}
        # must be inside board
        for (r,c) in new_squares:
            if not in_board(r,c):
                return False
            if (r,c) in obstacles:
                return False
            if (r,c) in pawns_set:
                return False
        # Need to check that the move is valid: the edge moved along must be adjacent to exactly two open squares
        # Actually the problem states:
        # If a whole edge of the king piece is adjacent to two open squares, we can slide the king piece there.
        # The "two open squares" are exactly the two empty squares outside of king and pawns and obstacles.
        # Since number of open squares is always 2, and moving king consumes those squares for king's new position,
        # the two squares adjacent along movement edge must be those two open squares.
        
        # Identify which edge moves in direction d:
        # For (dr, dc):
        # If dr == -1 (up): edge squares are top row (kr,kc),(kr,kc+1)
        # If dr == 1 (down): bottom row (kr+1,kc),(kr+1,kc+1)
        # If dc == -1 (left): left column (kr,kc),(kr+1,kc)
        # If dc == 1 (right): right column (kr,kc+1),(kr+1,kc+1)
        
        if dr == -1 and dc == 0:
            edge = {(kr, kc), (kr, kc+1)}
            adj = {(kr-1, kc), (kr-1, kc+1)}
        elif dr == 1 and dc == 0:
            edge = {(kr+1, kc), (kr+1, kc+1)}
            adj = {(kr+2, kc), (kr+2, kc+1)}
        elif dr == 0 and dc == -1:
            edge = {(kr, kc), (kr+1, kc)}
            adj = {(kr, kc-1), (kr+1, kc-1)}
        elif dr == 0 and dc == 1:
            edge = {(kr, kc+1), (kr+1, kc+1)}
            adj = {(kr, kc+2), (kr+1, kc+2)}
        else:
            return False
        
        # adj must be inside board to be valid
        for (r,c) in adj:
            if not in_board(r,c):
                return False
            if (r,c) in obstacles:
                return False

        # The two adj squares are the two open squares currently
        # Let's find open squares given king and pawns positions:
        occupied_positions = set(pawns_set).union(king_set)
        occupied_positions = set(pawns_set)
        occupied_positions.update(new_squares)
        # but the king hasn't moved yet; we want open squares before moving:
        current_occupied = pawns_set.union(king_coords).union(obstacles)
        empty_squares = {(r,c) for r in range(H) for c in range(W)} - current_occupied
        
        # Exactly two open squares before move, must be adj squares from edge:
        if empty_squares != set(adj):
            return False
        return True
    
    # Moves for pawns: can move into adjacent open square (one of the two open squares)
    def pawn_can_move(pos, king_pos, pawns_set, d):
        r,c = pos
        dr, dc = d
        nr, nc = r + dr, c + dc
        if not in_board(nr,nc):
            return False
        if (nr, nc) in obstacles:
            return False
        # The two open squares before move are exactly the two squares not occupied by king, pawns, obstacles
        current_occupied = pawns_set.union(king_coords).union(obstacles)
        empty_squares = {(rr,cc) for rr in range(H) for cc in range(W)} - current_occupied
        # To move pawn into (nr,nc), that square must be one of these two open squares, and adjacent to pawn
        if (nr,nc) not in empty_squares:
            return False
        # Also, pawn must be adjacent to open square:
        if abs(nr - r) + abs(nc - c) != 1:
            return False
        # Only one move at a time, so it's allowed:
        return True
    
    # Since number of open squares is always two, after each move open squares move accordingly.
    # On sliding a pawn into open square, the old pawn position becomes an open square.
    # On sliding the king, the two squares that disappear from king become open squares.
    
    # So given king_pos and pawns_set, the open squares are defined by the rest:
    # empty_squares = all squares - obstacles - king squares - pawns
    
    # We'll represent state by king_pos and pawns_set
    
    start_state = (king, frozenset(pawns))
    visited = set()
    visited.add(start_state)
    queue = deque([(start_state, 0)])
    
    while queue:
        (kpos, ps), moves = queue.popleft()
        kr, kc = kpos
        # Check if king is at top-left corner (0,0)
        if (kr, kc) == (0,0):
            return moves
        
        # Current king squares
        king_squares = {(kr, kc), (kr, kc+1), (kr+1, kc), (kr+1, kc+1)}
        current_occupied = ps.union(king_squares).union(obstacles)
        empty_squares = {(r,c) for r in range(H) for c in range(W)} - current_occupied
        
        # Try to move king in each direction
        for d in DIRS:
            if king_can_move(kpos, ps, d):
                dr, dc = d
                new_king_pos = (kr + dr, kc + dc)
                # After moving king, the open squares are the two squares that used to be king squares and are now outside king
                # Actually, open squares after move = positions vacated by king + positions previously open squares moved into king
                # But according to definition open squares correspond to empty squares not occupied by king, pawns, obstacles
                # So the new open squares are positions vacated by king when it moved
                
                # The two old king squares that the king left become open squares
                # Identify which two squares are vacated:
                # old king squares: king_squares
                # new king squares: new_king_squares
                new_king_squares = {(new_king_pos[0], new_king_pos[1]), (new_king_pos[0], new_king_pos[1]+1),
                                    (new_king_pos[0]+1, new_king_pos[1]), (new_king_pos[0]+1, new_king_pos[1]+1)}
                vacated = king_squares - new_king_squares
                if len(vacated) != 2:
                    continue
                
                # New open squares must be exactly these vacated squares
                # For new pawns set unchanged
                
                new_state = (new_king_pos, ps)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves+1))
        
        # Try to move each pawn if it can move into an open square
        for p in ps:
            pr, pc = p
            for d in DIRS:
                dr, dc = d
                nr, nc = pr + dr, pc + dc
                # Pawn can move into open square only
                if (nr, nc) in empty_squares and abs(nr - pr) + abs(nc - pc) == 1:
                    # After pawn moves, the pawn vacates old square, which becomes open square
                    # The open squares shift accordingly
                    
                    # new pawns set: remove old, add new
                    new_pawns = set(ps)
                    new_pawns.remove(p)
                    new_pawns.add((nr,nc))
                    
                    # Open squares after move are old pawn position + the other old open square besides the move target
                    # old open squares = empty_squares (two squares)
                    # one open square was target (nr,nc), the other is the other square in empty_squares
                    other_open = empty_squares - {(nr,nc)}
                    if len(other_open) != 1:
                        continue
                    new_state = (kpos, frozenset(new_pawns))
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, moves+1))
    
    return -1

def main():
    import sys
    input = sys.stdin.readline
    while True:
        line = ''
        while line.strip() == '':
            line = input()
            if not line:
                return
        H, W = map(int, line.split())
        if H == 0 and W == 0:
            break
        grid = [input().rstrip('\n') for _ in range(H)]
        print(solve_puzzle(H, W, grid))

if __name__ == "__main__":
    main()