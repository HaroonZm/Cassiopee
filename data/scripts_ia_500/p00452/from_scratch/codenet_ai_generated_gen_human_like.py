import sys

def main():
    input = sys.stdin.readline
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        points = [int(input()) for _ in range(N)]

        # dp[s] = True if it is possible to get sum s by throwing up to 4 darts
        dp = [False] * (M + 1)
        dp[0] = True

        for _ in range(4):  # up to 4 throws
            next_dp = dp[:]
            for p in points:
                for s in range(M - p + 1):
                    if dp[s]:
                        next_dp[s + p] = True
            dp = next_dp

        # find the maximum score <= M
        for score in range(M, -1, -1):
            if dp[score]:
                print(score)
                break

if __name__ == "__main__":
    main()