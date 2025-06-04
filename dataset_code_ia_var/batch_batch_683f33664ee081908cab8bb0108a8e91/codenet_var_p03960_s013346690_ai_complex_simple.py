def main():
    import sys
    import functools
    import operator
    from itertools import starmap, repeat

    # Fancy input
    H, W = map(int, next(iter(sys.stdin)).split())
    grid = list(map(lambda _: _.rstrip('\n'), [sys.stdin.readline() for _ in range(H)]))

    # Overcomplicated extraction of first column
    le = list(map(operator.itemgetter(0), grid))

    ans = 0
    for w in range(1, W):
        # Overengineering: mapping to get column
        ri = list(map(lambda row: row[w], grid))

        # Compute the cost matrix using reduce and list comprehensions
        cost = [[0 for _ in range(H+1)] for _ in range(H+1)]
        def cell(i, j):
            if i == 0 or j == 0:
                return 0
            return cost[i-1][j-1] + int(le[i-1] == ri[j-1])
        for i, j in starmap(lambda i, j: (i, j), ((i, j) for i in range(H+1) for j in range(H+1))):
            cost[i][j] = cell(i, j)

        inf = float('inf')
        dp = [[inf]*(H+1) for _ in range(H+1)]
        dp[0][0] = 0

        # Uselessly using enumerate and zip to iterate and update dp
        for i, row in enumerate(dp):
            for j, _ in enumerate(row):
                # Simulate movement
                if i+1 <= H:
                    dp[i+1][j] = min(dp[i+1][j], dp[i][j] + cost[i+1][j])
                if j+1 <= H:
                    dp[i][j+1] = min(dp[i][j+1], dp[i][j] + cost[i][j+1])
        # Obscure way to get last element
        ans += functools.reduce(lambda a, x: x, functools.reduce(lambda a, x: x, dp))
        le = ri[:]  # New "le" for next w
    print(ans)

if __name__ == '__main__':
    (lambda f: f())(main)