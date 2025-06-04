import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# dx, dy for Up, Down, Left, Right
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def can_escape(H,W,R,C,horz,vert):
    from collections import deque
    # visited[r][c][flip]: whether position (r,c) is visited with flip state flip
    visited = [[[False]*2 for _ in range(W)] for __ in range(H)]
    # initial flip=0 means wall state as input
    q = deque()
    q.append((R-1,C-1,0))
    visited[R-1][C-1][0] = True

    while q:
        r,c,flip = q.popleft()

        walls_now = flip

        # Check if Alice can escape from (r,c) at current flip state
        # Escape means bob can move from (r,c) through an outer edge with no wall
        # i.e. if from (r,c), in some direction d, either cell out of board and no wall
        # For each direction, check if escape possible
        # Also, if all directions blocked, no escape possible

        # Count accessible moves from (r,c) for Alice
        accessible_dirs = 0

        for i,(dr,dc) in enumerate(dirs):
            nr,nc = r+dr,c+dc

            # Determine if wall exists on edge between (r,c) and (nr,nc), respect flip
            # Edges defined by horz and vert:
            # Horizontal edges: between (r,c) and (r-1,c): horz[r][c]
            # Vertical edges: between (r,c) and (r,c-1): vert[r][c]
            #
            # up: check horz[r][c], wall present if horz[r][c]^flip==1 (if r>0)
            # down: check horz[r+1][c]
            # left: check vert[r][c]
            # right: check vert[r][c+1]

            if i==0:
                # up
                if r==0:
                    # edge out of board on top
                    wall = horz[r][c]^walls_now
                    if wall==0:
                        # escape possible
                        return True
                    else:
                        continue
                else:
                    wall = horz[r][c]^walls_now
                    if wall==1:
                        continue
            elif i==1:
                # down
                if r==H-1:
                    wall = horz[r+1][c]^walls_now
                    if wall==0:
                        return True
                    else:
                        continue
                else:
                    wall = horz[r+1][c]^walls_now
                    if wall==1:
                        continue
            elif i==2:
                # left
                if c==0:
                    wall = vert[r][c]^walls_now
                    if wall==0:
                        return True
                    else:
                        continue
                else:
                    wall = vert[r][c]^walls_now
                    if wall==1:
                        continue
            else:
                # right
                if c==W-1:
                    wall = vert[r][c+1]^walls_now
                    if wall==0:
                        return True
                    else:
                        continue
                else:
                    wall = vert[r][c+1]^walls_now
                    if wall==1:
                        continue

            # If reach here, no wall, and inside board
            accessible_dirs += 1
            if not visited[nr][nc][flip]:
                visited[nr][nc][flip] = True
                q.append((nr,nc,flip))

        # If no accessible dirs, escape impossible from here (Alice stuck)
        if accessible_dirs==0:
            # Can't move further, ignore
            pass

        # Bob's turn: can flip or not flip walls

        # Flip changes walls from flip to 1-flip
        flip2 = 1 - flip
        if not visited[r][c][flip2]:
            # Bob can flip and keep piece in same position (since Bob does not move the piece)
            # Push state with flip toggled
            visited[r][c][flip2] = True
            q.append((r,c,flip2))

    return False

while True:
    H,W,R,C = map(int,input().split())
    if H==0 and W==0 and R==0 and C==0:
        break
    horz = [list(map(int,input().split())) for _ in range(H+1)]
    vert = [list(map(int,input().split())) for _ in range(H)]
    print("Yes" if can_escape(H,W,R,C,horz,vert) else "No")