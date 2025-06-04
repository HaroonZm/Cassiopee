import sys
from itertools import combinations

def main():
    input = sys.stdin.readline
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    card_sum = sum(A)
    if card_sum < K:
        print(0)
        return
    # if any Ai == K, eating that card alone suffices
    if K in A:
        print(1)
        return

    # To block sum K, the remaining cards after eating certain cards must have no subset summing to K
    # We try to eat minimal number of cards, so enumerate subsets of cards to eat from size 0 to N

    # Precompute all subsets sums for each remainder subset is expensive but manageable because N <= 20

    # We'll try from 0 to N cards to eat
    # For each subset of eaten cards, check if sum K is achievable in the remaining cards

    # Use meet in the middle approach to speed up subset sums check
    # But since we only need to check existence of subset summing to K, a DP subset sum will suffice

    # Let's create an efficient function to check if sum K is possible in a list

    def can_make_sum(arr, target):
        possible = set([0])
        for x in arr:
            new_possible = possible.copy()
            for s in possible:
                ns = s+x
                if ns == target:
                    return True
                if ns < target:
                    new_possible.add(ns)
            possible = new_possible
        return False

    for eaten_count in range(N+1):
        for eaten in combinations(range(N), eaten_count):
            rem = [A[i] for i in range(N) if i not in eaten]
            if not can_make_sum(rem, K):
                print(eaten_count)
                return

main()