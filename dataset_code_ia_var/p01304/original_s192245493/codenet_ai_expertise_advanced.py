from sys import stdin
from collections import defaultdict

def main():
    input_iter = iter(stdin.read().split())
    next_int = lambda: int(next(input_iter))

    for _ in range(next_int()):
        gx, gy = next_int(), next_int()
        p = next_int()
        mat = [tuple(next_int() for _ in range(4)) for _ in range(p)]

        # Use sets for O(1) forbidden edge check
        forbidden = set()
        x0, y0 = gx, gy
        for x1, y1, x2, y2 in mat:
            forbidden.add( (x1, y1, x2, y2) )
            forbidden.add( (x2, y2, x1, y1) )
            if x1 + x2 == 0:
                y0 = min(y0, min(y1, y2))
            if y1 + y2 == 0:
                x0 = min(x0, min(x1, x2))

        dp = [ [0]*(gy+1) for _ in range(gx+1) ]
        for i in range(x0+1):
            dp[i][0] = 1
        for i in range(y0+1):
            dp[0][i] = 1

        for x in range(1, gx+1):
            for y in range(1, gy+1):
                val = 0
                if (x-1, y, x, y) not in forbidden:
                    val += dp[x-1][y]
                if (x, y-1, x, y) not in forbidden:
                    val += dp[x][y-1]
                dp[x][y] = val

        print(dp[gx][gy] or "Miserable Hokusai!")

if __name__ == "__main__":
    main()