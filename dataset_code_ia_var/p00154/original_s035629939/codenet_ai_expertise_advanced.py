import sys
from array import array
from functools import partial

def main():
    input_fn = iter(sys.stdin.readline, '')
    try:
        while True:
            m = int(next(input_fn))
            if m == 0:
                return 0
            dp = [array('I', (0 for _ in range(1001))) for _ in range(m + 1)]
            dp[0][0] = 1
            for i, (v, c) in enumerate(map(lambda _: map(int, next(input_fn).split()), range(m))):
                for j, cnt in ((j, dp[i][j]) for j in range(1001) if dp[i][j]):
                    for k in range(1, c + 1):
                        nxt = j + v * k
                        if nxt > 1000: break
                        dp[i+1][nxt] += cnt
                for j in range(1001):
                    dp[i+1][j] += dp[i][j]
            n = int(next(input_fn))
            results = map(lambda _: int(next(input_fn)), range(n))
            output = (str(dp[m][x]) for x in results)
            print('\n'.join(output))
    except StopIteration:
        pass

if __name__ == '__main__':
    sys.exit(main())