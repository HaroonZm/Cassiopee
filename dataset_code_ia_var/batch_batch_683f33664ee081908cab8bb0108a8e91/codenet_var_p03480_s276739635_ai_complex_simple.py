import sys
from functools import reduce
from itertools import groupby, accumulate, chain

sys.setrecursionlimit(pow(10,8))

def main():
    S = input()
    N = len(S)
    indexes = [i+1 for i,(a,b) in enumerate(zip(S,S[1:])) if a != b]
    breaks = list(chain([0], indexes, [N]))
    spans = list(map(lambda ab: ab[1]-ab[0], zip(breaks[:-1],breaks[1:])))
    ans = max(map(lambda k: min(N - breaks[k], breaks[k+1]), range(len(breaks)-1)), default=N)
    ans = max(ans, N - breaks[-2]) if len(breaks) > 1 else N
    print(ans)
if __name__ == '__main__':
    main()