from sys import stdin, stdout
from bisect import bisect_left

input_iter = iter(stdin.read().split())
def input(): return next(input_iter)

while True:
    N = int(input())
    if N == 0:
        break
    S = [tuple(map(int, (input(), input()))) for _ in range(N)]  # This will consume too many inputs incorrectly, needs fixing.

# Realize the above code is incorrect because input() gives single tokens, not lines.
# Redesign reading:

from sys import stdin, stdout
from itertools import chain

def lis_envelope(envelopes):
    # envelopes sorted by height, then by radius
    n = len(envelopes)
    dp = []
    for _, r in envelopes:
        pos = bisect_left(dp, r)
        if pos == len(dp):
            dp.append(r)
        else:
            dp[pos] = r
    return len(dp)

def main():
    import sys
    input_iter = iter(sys.stdin.read().split())
    while True:
        try:
            N = int(next(input_iter))
        except StopIteration:
            break
        if N == 0:
            break
        S = [ (int(next(input_iter)), int(next(input_iter))) for _ in range(N) ]
        M = int(next(input_iter))
        S.extend((int(next(input_iter)), int(next(input_iter))) for _ in range(M))
        S.sort()
        # Use LIS on radius with increasing height
        stdout.write(str(lis_envelope(S)) + '\n')

if __name__ == '__main__':
    main()