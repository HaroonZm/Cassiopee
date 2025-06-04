def main():
    import sys
    sys.setrecursionlimit(10**7)

    input = sys.stdin.readline

    # T: number of datasets
    T = int(input())

    for _ in range(T):
        gx, gy = map(int, input().split())  # secret place coordinates

        p = int(input())  # number of edges with matatabi

        # We'll mark edges where passage is forbidden.
        # Since city is grid, edges are between integer coordinates (x,y) and (x+1,y) or (x,y+1).
        # We create two separate sets for forbidden edges:
        # 1) horizontal edges: ((x,y),(x+1,y))
        # 2) vertical edges: ((x,y),(x,y+1))

        forbidden = set()

        for __ in range(p):
            x1, y1, x2, y2 = map(int, input().split())
            # Store edges in sorted order to avoid duplicates and for easy matching
            if (x1, y1) < (x2, y2):
                forbidden.add(((x1, y1), (x2, y2)))
            else:
                forbidden.add(((x2, y2), (x1, y1)))

        # Since Hokusai wants to go from (0,0) to (gx,gy)
        # and never move away from the target, i.e. x and y never decrease
        # So possible moves at each step: move right (x+1,y) or move up (x,y+1)

        # Use DP: dp[x][y] = number of possible paths from (0,0) to (x,y)
        dp = [[0] * (gy + 1) for _ in range(gx + 1)]
        dp[0][0] = 1

        for x in range(gx + 1):
            for y in range(gy + 1):
                if x == 0 and y == 0:
                    continue
                paths = 0
                # from left (x-1, y) -> (x, y)
                if x > 0:
                    edge = ((x-1, y), (x, y))
                    if edge not in forbidden:
                        paths += dp[x - 1][y]
                # from down (x, y-1) -> (x, y)
                if y > 0:
                    edge = ((x, y-1), (x, y))
                    if edge not in forbidden:
                        paths += dp[x][y - 1]
                dp[x][y] = paths

        if dp[gx][gy] == 0:
            print("Miserable Hokusai!")
        else:
            print(dp[gx][gy])

if __name__ == "__main__":
    main()