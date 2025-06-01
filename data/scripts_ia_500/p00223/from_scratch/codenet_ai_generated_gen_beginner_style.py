from collections import deque

def opposite_dir(dx, dy):
    return -dx, -dy

def is_inside(x, y, W, H):
    return 1 <= x <= W and 1 <= y <= H

def main():
    while True:
        line = input().strip()
        if line == "":
            continue
        W_H = line.split()
        if len(W_H) != 2:
            continue
        W, H = map(int, W_H)
        if W == 0 and H == 0:
            break
        tx, ty = map(int, input().split())
        kx, ky = map(int, input().split())
        grid = []
        for _ in range(H):
            row = list(map(int, input().split()))
            grid.append(row)
        # Directions: East, West, South, North
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # State: positions of Takayuki (tx, ty) and Kazuyuki (kx, ky)
        # Use BFS to find shortest meeting time
        visited = set()
        # positions are 1-based, convert to zero-based for array indexing
        start = (tx, ty, kx, ky)
        queue = deque()
        queue.append((tx, ty, kx, ky, 0))
        visited.add((tx, ty, kx, ky))

        ans = "NA"
        while queue:
            tx_cur, ty_cur, kx_cur, ky_cur, time = queue.popleft()
            if time >= 100:
                break
            # If met, output time and stop
            if tx_cur == kx_cur and ty_cur == ky_cur:
                ans = str(time)
                break
            # Try all possible moves for Takayuki
            for dx, dy in directions:
                # Takayuki's next position
                ntx = tx_cur + dx
                nty = ty_cur + dy
                # Kazuyuki moves oppositely
                odx, ody = opposite_dir(dx, dy)
                nkx = kx_cur + odx
                nky = ky_cur + ody

                # Check if Takayuki's next is valid
                takayuki_valid = is_inside(ntx, nty, W, H) and grid[nty -1][ntx -1] == 0
                # Check if Kazuyuki's next is valid
                kazuyuki_valid = is_inside(nkx, nky, W, H) and grid[nky -1][nkx -1] == 0

                # If one of them is invalid, that one stays in place, other moves if valid
                if not takayuki_valid and not kazuyuki_valid:
                    # Both can't move
                    ntx, nty = tx_cur, ty_cur
                    nkx, nky = kx_cur, ky_cur
                elif not takayuki_valid and kazuyuki_valid:
                    # Takayuki stays, Kazuyuki moves
                    ntx, nty = tx_cur, ty_cur
                elif takayuki_valid and not kazuyuki_valid:
                    # Kazuyuki stays, Takayuki moves
                    nkx, nky = kx_cur, ky_cur
                # else both move as planned

                # Check if already visited
                state = (ntx, nty, nkx, nky)
                if state not in visited:
                    visited.add(state)
                    queue.append((ntx, nty, nkx, nky, time +1))
        print(ans)

if __name__ == "__main__":
    main()