from collections import deque

def solve():
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        # Read wall info lines: total 2*h -1 lines
        lines = []
        for _ in range(2*h -1):
            line = input()
            # strip leading spaces and split
            parts = line.strip().split()
            lines.append(list(map(int, parts)))
        # We have:
        # Horizontal walls lines are at even indices: 0,2,4... each has w-1 integers
        # Vertical walls lines at odd indices: 1,3,5... each has w integers

        # Build graph of possible moves
        # Position: (r,c), r in [0,h-1], c in [0,w-1]
        # moves: up, down, left, right if no walls

        # easy access:
        # hor_walls[r][c] means wall between (r,c) and (r,c+1), size h x (w-1)
        # ver_walls[r][c] means wall between (r,c) and (r+1,c), size (h-1) x w

        hor_walls = [None]*h
        ver_walls = [None]*(h-1)
        # fill hor_walls from lines at even indices
        for i in range(h):
            hor_walls[i] = lines[2*i]
        # fill ver_walls from lines at odd indices
        for i in range(h-1):
            ver_walls[i] = lines[2*i+1]

        # BFS from entry to exit
        # entry: (0,0) accessible from top side (open)
        # exit: (h-1,w-1) accessible at bottom side (open)

        visited = [[False]*w for _ in range(h)]
        dist = [[0]*w for _ in range(h)]
        q = deque()
        q.append((0,0))
        visited[0][0] = True
        dist[0][0] = 1

        while q:
            r,c = q.popleft()
            if r == h-1 and c == w-1:
                # reached exit
                print(dist[r][c])
                break
            # go left
            if c > 0:
                # check wall between (r,c-1)-(r,c) horizontal wall at hor_walls[r][c-1]
                if hor_walls[r][c-1] == 0 and not visited[r][c-1]:
                    visited[r][c-1] = True
                    dist[r][c-1] = dist[r][c] +1
                    q.append((r,c-1))
            # go right
            if c < w-1:
                # wall between (r,c)-(r,c+1) hor_walls[r][c]
                if hor_walls[r][c] == 0 and not visited[r][c+1]:
                    visited[r][c+1] = True
                    dist[r][c+1] = dist[r][c] +1
                    q.append((r,c+1))
            # go up
            if r > 0:
                # wall between (r-1,c)-(r,c) vertical wall at ver_walls[r-1][c]
                if ver_walls[r-1][c] == 0 and not visited[r-1][c]:
                    visited[r-1][c] = True
                    dist[r-1][c] = dist[r][c] +1
                    q.append((r-1,c))
            # go down
            if r < h-1:
                # wall between (r,c)-(r+1,c) ver_walls[r][c]
                if ver_walls[r][c] == 0 and not visited[r+1][c]:
                    visited[r+1][c] = True
                    dist[r+1][c] = dist[r][c] +1
                    q.append((r+1,c))
        else:
            # no break -> no path
            print(0)

if __name__ == "__main__":
    solve()