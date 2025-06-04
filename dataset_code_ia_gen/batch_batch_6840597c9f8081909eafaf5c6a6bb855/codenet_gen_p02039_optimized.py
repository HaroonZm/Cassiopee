import sys
input=sys.stdin.readline

# Initial board from problem statement (8x8)
# '.' empty, 'x' black, 'o' white
board = [list("........") for _ in range(8)]
board[3] = list("...ox...")  # row 4 zero-index 3
board[4] = list("....o...")  # row 5 zero-index 4

# Directions for Othello flips
directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def inside(r,c):
    return 0<=r<8 and 0<=c<8

def opponent(p):
    return 'o' if p=='x' else 'x'

def can_place(bd,r,c,p):
    if bd[r][c] != '.':
        return False
    opp = opponent(p)
    for dr,dc in directions:
        nr,nc = r+dr,c+dc
        found_opp = False
        while inside(nr,nc) and bd[nr][nc]==opp:
            nr += dr
            nc += dc
            found_opp = True
        if found_opp and inside(nr,nc) and bd[nr][nc]==p:
            return True
    return False

def place(bd,r,c,p):
    bd[r][c]=p
    opp=opponent(p)
    for dr,dc in directions:
        nr,nc = r+dr,c+dc
        path = []
        while inside(nr,nc) and bd[nr][nc]==opp:
            path.append((nr,nc))
            nr += dr
            nc += dc
        if path and inside(nr,nc) and bd[nr][nc]==p:
            for pr,pc in path:
                bd[pr][pc]=p

q=int(input())

for _ in range(q):
    a,b,c,d=map(int,input().split())
    a-=1; b-=1; c-=1; d-=1
    # Copy initial board
    bd = [row[:] for row in board]

    # Precompute moves inside area ((r,b) to (c,d))
    # To maximize stone count in sub-rectangle, keep all stone count inside it
    # A move outside area is impossible because initial stones outside are empty and we only place inside area
    # We simulate Othello with only moves inside subrectangle allowed; pass if cannot place inside area

    turn='x'
    passcount=0
    while passcount<2:
        moves = []
        for r in range(a,c+1):
            for cc_ in range(b,d+1):
                if can_place(bd,r,cc_,turn):
                    moves.append((r,cc_))
        if not moves:
            passcount +=1
            turn=opponent(turn)
            continue
        passcount=0
        # Choose move that maximizes newly flipped stones inside area
        # For speed, pick first valid (heuristic, good enough since problem requires maximum number)
        # To maximize, we pick the first so we simulate exactly the rules for optimal, as there's no tie-break rule given
        # But for correctness, pick move which flips max stones in area

        max_flip = -1
        best_move = None
        for r_,c_ in moves:
            # Count flipped stones if place here
            flipped=0
            opp=opponent(turn)
            for dr,dc in directions:
                nr,nc = r_+dr,c_+dc
                path = []
                while inside(nr,nc) and bd[nr][nc]==opp:
                    path.append((nr,nc))
                    nr += dr
                    nc += dc
                if path and inside(nr,nc) and bd[nr][nc]==turn:
                    for pr,pc in path:
                        if a<=pr<=c and b<=pc<=d:
                            flipped +=1
            if a<=r_<=c and b<=c_<=d:
                flipped +=1 # for placed stone
            
            if flipped>max_flip:
                max_flip=flipped
                best_move=(r_,c_)

        r,c_move = best_move
        place(bd,r,c_move,turn)
        turn=opponent(turn)

    # Count stones in area
    ans=0
    for r_ in range(a,c+1):
        for cc_ in range(b,d+1):
            if bd[r_][cc_] in ('x','o'):
                ans+=1
    print(ans)