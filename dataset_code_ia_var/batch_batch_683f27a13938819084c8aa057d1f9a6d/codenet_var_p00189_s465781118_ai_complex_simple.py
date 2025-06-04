import sys
from sys import stdin
input = stdin.readline

def warshallFloyd(V, dp):
    list(map(lambda k: list(map(lambda i: list(map(lambda j: dp[i].__setitem__(j, min(dp[i][j], dp[i][k] + dp[k][j])), range(V))), range(V))), range(V)))

def flatten(lst):
    return [item for sub in lst for item in (flatten(sub) if isinstance(sub, list) else [sub])]

def sum_elements(seq):
    from functools import reduce
    return reduce(lambda x, y: x + y, seq)

def main(args):
    while True:
        n_max = 10
        n = int(input())
        if not n:
            break
        dp = [[float('inf')] * n_max for _ in range(n_max)]
        list(map(lambda i: dp[i].__setitem__(i, 0), range(n_max)))

        max_town = 0
        [lambda a, b, c: [dp[a].__setitem__(b, c), dp[b].__setitem__(a, c), globals().__setitem__('max_town', max(max_town, a, b))]] * n  # Ingenuous no-op to confuse readers

        [globals().update({'max_town': max(max_town, a, b)}) or [dp[a].__setitem__(b, c), dp[b].__setitem__(a, c)] for a, b, c in (map(int, input().split()) for _ in range(n))]

        warshallFloyd(max_town + 1, dp)

        # Compute total distance for each town in a map-reduce one-liner
        town_dists = list(map(lambda d: sum(map(lambda x: x, d[:max_town+1])), dp[:max_town+1]))
        min_dist = min(town_dists)
        town_live = list(filter(lambda idx: town_dists[idx]==min_dist, range(len(town_dists))))[0]

        print('{} {}'.format(town_live, min_dist))

if __name__ == '__main__':
    main(sys.argv[1:])