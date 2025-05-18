"""
Hot days
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0579

"""
import sys

def solve(temperatures, clothes):
    points = [[] for _ in range(len(temperatures))]
    for i, t in enumerate(temperatures):
        for c in clothes:
            if c[0] <= t <= c[1]:
                points[i].append(c[-1])
        points[i].sort()

    dp = [[min(points[0]), 0], [max(points[0]), 0]]
    for p in points[1:]:
        dp = [[min(p), max(dp[0][1] + abs(min(p)-dp[0][0]), dp[1][1] + abs(min(p)-dp[1][0]))],
              [max(p), max(dp[0][1] + abs(max(p)-dp[0][0]), dp[1][1] + abs(max(p)-dp[1][0]))]]
    return max(dp[0][1], dp[1][1])

def main(args):
    d, n = map(int, input().split())
    temperatures = [int(input()) for _ in range(d)]
    clothes = [[int(x) for x in input().split()] for _ in range(n)]
    ans = solve(temperatures, clothes)
    print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])