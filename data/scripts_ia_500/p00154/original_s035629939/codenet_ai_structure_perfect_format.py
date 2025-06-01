import sys
from array import array

def main():
    while True:
        m = input()
        if m == 0:
            return 0
        dp = [array('I', [0] * 1001) for i in range(m + 1)]
        dp[0][0] = 1
        for i in range(m):
            v, c = map(int, input().split())
            for j in range(1001):
                for k in range(c + 1):
                    next_index = j + v * k
                    if next_index > 1000:
                        continue
                    dp[i + 1][next_index] += dp[i][j]
        n = input()
        for _ in range(n):
            x = input()
            print(dp[m][x])

if __name__ == '__main__':
    sys.exit(main())