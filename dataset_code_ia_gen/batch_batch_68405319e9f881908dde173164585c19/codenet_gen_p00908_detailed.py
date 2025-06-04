import sys
from collections import deque

def solve_puzzle(H, W, grid):
    # Directions for movement up, down, left, right
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    # Parse the grid to find:
    # - the king block cells (2x2, marked with 'X')
    # - the pawns positions (marked with 'o')
    # - the obstacles (marked with '*')
    # - the two open squares (marked with '.')
    obstacles = set()
    pawns = set()
    open_squares = set()
    king_cells = []

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
                king_cells.append((r,c))

    # The king occupies exactly 4 cells in a 2x2 block
    # Determine king top-left cell coordinates as a state
    # So king position state is (kr,kc) = upper left cell of king 2x2 block

    # Determine king top-left:
    # king_cells is four coordinates of king cells,
    # find minimum row and column among them:
    kr = min(r for r,c in king_cells)
    kc = min(c for r,c in king_cells)

    # Important validations:
    # king cells should form a 2x2 block, i.e.,
    # check that (kr,kc), (kr,kc+1), (kr+1,kc), (kr+1,kc+1) are all occupied by king
    expected_king_cells = {(kr,kc),(kr,kc+1),(kr+1,kc),(kr+1,kc+1)}
    if set(king_cells) != expected_king_cells:
        # Invalid input format according to problem
        return -1

    # The puzzle always have exactly two open squares
    if len(open_squares) != 2:
        return -1

    # State representation
    # We'll represent the state as (king row, king col, tuple of sorted pawns positions, tuple of two open squares sorted)
    # but open squares are fully defined by frame and pawns and king position too?
    # No, the two open squares shifts as pieces move by sliding into the squares.
    # So the open squares positions must be kept in the state, since pieces moves depend on availability of opens.
    #
    # However, since the grid is fixed, and the sets of obstacles fixed,
    # at each step the union of king + pawns + obstacles + opens = entire grid
    # So knowing king pos + pawn pos + open pos is enough.
    #
    # But open squares move dynamically. Pieces slide into open squares and open squares move to previous piece position.
    #
    # We'll store state :
    # (kr,kc,pawns frozenset, open1, open2)
    # where pawns are stored as frozenset of positions,
    # open squares as a sorted tuple ((r1,c1),(r2,c2))

    # Since open squares are always two distinct cells, sort them to keep order consistent

    # Preprocessing:
    # Construct a set of fixed obstacle squares for quick membership tests

    obstacles_set = obstacles

    # The upper-left corner position of the king is (0,0) for solved state
    goal_king = (0,0)

    # Function to check if a given cell is inside the frame
    def in_frame(r,c):
        return 0 <= r < H and 0 <= c < W

    # Function to check if 2x2 king block fits at (r,c)
    def king_fits(r,c, pawns_set):
        # Check bound
        if r < 0 or c < 0 or r+1 >= H or c+1 >= W:
            return False
        # The 4 cells must be free (occupied by king only), i.e. no obstacles or pawns
        # so these 4 cells must not be an obstacle or pawn cell
        for rr in [r,r+1]:
            for cc in [c,c+1]:
                if (rr,cc) in obstacles_set:
                    return False
                if (rr,cc) in pawns_set:
                    return False
        return True

    # Check adjacency of king edge to two open squares to move king
    # Rules say:
    # If a whole edge of the king piece (i.e. two adjacent cells forming an edge) are adjacent on the side to two open squares, we can move the king sliding one cell in that direction.
    # Means we need to check all four directions king can slide and if the two open squares adjacent at the new positions match.

    # The king moves in four directions:
    # UP: need open squares at (r-1,c) and (r-1,c+1)
    # DOWN: open squares at (r+2,c) and (r+2,c+1)
    # LEFT: open squares at (r,c-1) and (r+1,c-1)
    # RIGHT: open squares at (r,c+2) and (r+1,c+2)

    # For a king move to be valid:
    # Those new cells must be two open squares in the open squares set
    # And the king must fit in the new position (bounds, no obstacle or pawn)

    # Check possible king moves from (r,c)
    def king_moves(r,c, pawns_set, open_squares_set):
        res = []
        # UP
        if r-1 >= 0:
            if {(r-1,c),(r-1,c+1)}.issubset(open_squares_set):
                if king_fits(r-1,c,pawns_set):
                    res.append((r-1,c))
        # DOWN
        if r+2 < H:
            if {(r+2,c),(r+2,c+1)}.issubset(open_squares_set):
                if king_fits(r+1,c,pawns_set):
                    res.append((r+1,c))
        # LEFT
        if c-1 >= 0:
            if {(r,c-1),(r+1,c-1)}.issubset(open_squares_set):
                if king_fits(r,c-1,pawns_set):
                    res.append((r,c-1))
        # RIGHT
        if c+2 < W:
            if {(r,c+2),(r+1,c+2)}.issubset(open_squares_set):
                if king_fits(r,c+1,pawns_set):
                    res.append((r,c+1))
        return res

    # Pawns can move if adjacent to an open square.
    # Valid pawn moves: pawn moves into one of two open squares if adjacent (up/down/left/right)
    # When the pawn moves into an open square, the open square moves to the previous pawn position.
    # Similarly for king move: when king moves into two open squares, the new open squares become the old king block cells.

    # Generate pawn moves: for each pawn adjacent to an open square
    # For each open square adjacent to pawns, pawn can move onto that open square

    def pawn_moves(pawns_set, open_squares_set, king_r, king_c):
        moves = []
        # For each pawn
        for pr, pc in pawns_set:
            for dr,dc in directions:
                nr, nc = pr+dr, pc+dc
                # If the adjacent cell is an open square, the pawn can slide there
                if (nr,nc) in open_squares_set:
                    # Move pawn from (pr,pc) -> (nr,nc)
                    # New pawns positions: remove old, add new
                    new_pawns = pawns_set - {(pr,pc)} | {(nr,nc)}
                    # Open squares move: new open squares positions are old open squares removing moved square adding pawn old position
                    new_open = open_squares_set - {(nr,nc)} | {(pr,pc)}

                    # King position unchanged
                    moves.append( (king_r, king_c, frozenset(new_pawns), tuple(sorted(new_open))) )
        return moves

    # King sliding move:
    # When king moves to a new position (rnew,cnew), the open squares now occupy the old king cells (r,c),(r,c+1),(r+1,c),(r+1,c+1) except 2 are occupied by king in new position,
    # the two squares vacated by king become open squares.
    # The two open squares king occupied before move convert to squares now occupied by king.
    #
    # Actually, the open squares in king move correspond to the two squares the king moves into,
    # and the two open squares after move become the old king cells vacated.
    #
    # So basically we remove from open squares the two squares king slides to,
    # then add the four old king cells minus the two occupied by king in old position,
    # but open squares are always two squares, so we update open squares to those vacated by king.

    # The problem states after king moves to new position:
    # The two old king cells vacated become open squares,
    # and the two open squares occupied are no longer open.

    # We'll have to carefully update open squares accordingly:
    # Steps:
    # - old_king_cells occupied by king initially
    # - new_king_cells occupied by king after move (4 cells)
    # - open squares after move = (open_squares - new_king_cells) + (old_king_cells - new_king_cells)
    # However, new_king_cells overlap old_king_cells at no point (king fully moves)
    # So effectively:
    # open_squares after move = (open_squares - new_king_cells) + old_king_cells

    # But we know open_squares are always two cells, so old_king_cells - new_king_cells should produce two vacated cells

    # Implementing this:

    def king_slide_moves(king_r, king_c, pawns_set, open_squares_set):
        results = []
        old_king_cells = {(king_r, king_c), (king_r, king_c+1), (king_r+1, king_c), (king_r+1, king_c+1)}
        for new_r,new_c in king_moves(king_r, king_c, pawns_set, open_squares_set):
            new_king_cells = {(new_r, new_c), (new_r, new_c+1), (new_r+1, new_c), (new_r+1, new_c+1)}
            # Check pawns set do not intersect new king cells (already done in king_fits), so safe
            # Compute new open squares:
            # Remove new king cells from open squares, add old king cells
            new_open = open_squares_set - new_king_cells | (old_king_cells - new_king_cells)
            # The new open squares must have exactly two cells
            if len(new_open) != 2:
                # Defensive: if invalid, skip
                continue
            results.append((new_r,new_c,pawns_set,frozenset(new_open)))
        return results

    # Initial state creation
    initial_state = (kr,kc,frozenset(pawns),tuple(sorted(open_squares)))

    # BFS to find minimal moves
    # Use a queue and a visited set
    visited = set()
    queue = deque()
    visited.add(initial_state)
    queue.append( (initial_state, 0) )  # (state, moves)

    while queue:
        (cur_kr,cur_kc, cur_pawns, cur_open), dist = queue.popleft()
        # Check if king at goal
        if (cur_kr,cur_kc) == goal_king:
            return dist
        open_set = set(cur_open)

        # Generate all next states by sliding pawns
        for next_state in pawn_moves(cur_pawns, open_set, cur_kr, cur_kc):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, dist+1))

        # Generate all next states by sliding king
        for kr_new, kc_new, pawns_new, open_new in king_slide_moves(cur_kr, cur_kc, cur_pawns, open_set):
            state = (kr_new, kc_new, pawns_new, tuple(sorted(open_new)))
            if state not in visited:
                visited.add(state)
                queue.append((state, dist+1))

    # If BFS finishes without finding goal
    return -1

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        H,W = map(int,line.strip().split())
        if H == 0 and W == 0:
            break
        grid = [input().rstrip('\n') for _ in range(H)]
        ans = solve_puzzle(H,W,grid)
        print(ans)

if __name__ == "__main__":
    main()