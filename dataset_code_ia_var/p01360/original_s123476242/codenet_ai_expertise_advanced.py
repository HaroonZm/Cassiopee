from sys import stdin
from functools import partial

def solve(line: str):
    length = len(line)
    INF = float('inf')
    # Use 2 rolling rows, each 2x3x3 array (boolean and left/right bounds)
    dp = [[[ [INF]*3 for _ in range(3) ] for _ in range(2)] for _ in range(2)]
    for k in range(2):
        dp[1][k][0][2] = 0

    for i, ch in enumerate(line):
        curr, next_ = i % 2, (i+1) % 2
        pos = (int(ch)+2)%3
        get = dp[next_]
        put = dp[curr]
        # Vectorized update over all states
        for l in range(3):
            for r in range(3):
                # Left move allowed
                if l <= pos:
                    put[1][l][pos] = min(put[1][l][pos], min(get[0][l][r], get[1][l][r]+1))
                # Right move allowed
                if pos <= r:
                    put[0][pos][r] = min(put[0][pos][r], min(get[1][l][r], get[0][l][r]+1))
        # Reset next_ slice to INF for next round (fast slice assignment)
        for j in range(2): 
            for l in range(3):
                for r in range(3):
                    dp[next_][j][l][r] = INF

    ans = min(
        dp[(length-1)%2][j][l][r]
        for j in range(2)
        for l in range(3)
        for r in range(3)
    )
    print(ans)

def main():
    for line in map(str.rstrip, stdin):
        if line == "#":
            break
        solve(line)

if __name__ == "__main__":
    main()