import sys
from itertools import combinations

def can_make_sum(cards, K):
    sums = set([0])
    for c in cards:
        new_sums = set()
        for s in sums:
            new_sums.add(s)
            new_sums.add(s + c)
        sums = new_sums
        if K in sums:
            return True
    return False

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

for r in range(N+1):
    for eat_cards in combinations(range(N), r):
        remain = [A[i] for i in range(N) if i not in eat_cards]
        if not can_make_sum(remain, K):
            print(r)
            sys.exit()