from collections import deque

def solve():
    while True:
        W, H = map(int, input().split())
        if W == 0 and H == 0:
            break

        roomL = []
        roomR = []
        for _ in range(H):
            l, r = input().split()
            roomL.append(list(l))
            roomR.append(list(r))

        # Find initial positions and goals
        startL = None
        startR = None
        goalL = None
        goalR = None
        for y in range(H):
            for x in range(W):
                cL = roomL[y][x]
                cR = roomR[y][x]
                if cL == 'L':
                    startL = (y,x)
                    roomL[y][x] = '.'
                elif cL == '%':
                    goalL = (y,x)
                if cR == 'R':
                    startR = (y,x)
                    roomR[y][x] = '.'
                elif cR == '%':
                    goalR = (y,x)

        # BFS over states: (posL, posR)
        # moves: N S E W
        moves = [(-1,0),(1,0),(0,-1),(0,1)]

        visited = set()
        queue = deque()
        queue.append( (startL, startR) )
        visited.add( (startL, startR) )

        def is_open(room, y, x):
            return 0 <= y < H and 0 <= x < W and room[y][x] != '#'

        can_open = False
        while queue:
            (ly, lx), (ry, rx) = queue.popleft()

            if (ly, lx) == goalL and (ry, rx) == goalR:
                can_open = True
                break

            for dy, dx in moves:
                nly, nlx = ly + dy, lx + dx
                nry, nrx = ry + dy, rx + dx

                # For left room, if next cell is wall or outside, Len stays
                if not is_open(roomL, nly, nlx):
                    nly, nlx = ly, lx
                # For right room, similar for Rin
                if not is_open(roomR, nry, nrx):
                    nry, nrx = ry, rx

                next_state = ((nly, nlx), (nry, nrx))
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)

        print("Yes" if can_open else "No")

if __name__ == "__main__":
    solve()