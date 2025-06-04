import sys
from itertools import islice, accumulate
from operator import itemgetter

def main():
    readline = sys.stdin.readline
    t = int(readline())
    for _ in range(t):
        n, k = map(int, readline().split())
        houses = list(map(int, readline().split()))

        if k >= n:
            print(0)
            continue

        # Calculate segment lengths between adjacent houses, indexed
        gaps = [(houses[i+1] - houses[i], i) for i in range(n-1)]
        # Select k-1 largest gaps to partition
        cuts = sorted(gaps, reverse=True, key=itemgetter(0))[:k-1]
        # Find partition indices sorted
        split_indices = sorted(i for _, i in cuts)

        # Use accumulate and islice for functional style
        indices = [0] + [idx + 1 for idx in split_indices] + [n]
        cable_length = sum(houses[indices[i+1] - 1] - houses[indices[i]] for i in range(k))
        print(cable_length)

if __name__ == '__main__':
    main()