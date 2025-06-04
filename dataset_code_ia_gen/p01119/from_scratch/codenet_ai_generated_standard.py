import sys
import math

def measurable(weights):
    possible = {0}
    for w in weights:
        next_possible = set()
        for x in possible:
            next_possible.add(x+w)
            next_possible.add(abs(x-w))
            next_possible.add(x)
        possible = next_possible
    return possible

def can_measure_all(amounts, weights):
    possible = measurable(weights)
    return all(a in possible for a in amounts)

def solution():
    input = sys.stdin.readline
    while True:
        n,m = map(int,input().split())
        if n == 0 and m == 0:
            break
        amounts = list(map(int,input().split()))
        weights = list(map(int,input().split()))
        possible = measurable(weights)
        if all(a in possible for a in amounts):
            print(0)
            continue
        max_a = max(amounts)
        # attempt to find smallest w_new to add
        # since w_j ≤ 10^8 but new weight can be larger, we search upwards
        # upper bound on search: max among amounts * 2 (heuristic)
        # To speed up we can try only amounts that fail
        fail_amounts = [a for a in amounts if a not in possible]
        # To find minimal new weight:
        # We test candidate weights starting from 1 upwards
        # Testing bigger weights won't help if no solution by max_a*2
        # But as constraints are big, limit search to 2*max_a or until found
        # Also, as the sum of weights possible is large, a better approach:
        # Use BFS or dynamic programming:
        # But since weights ≤ 10 and m ≤10, size of possible set can be big.
        # So we do an efficient search using set
        # Max weight to test can be up to 2*max_a
        max_search = 2 * max_a
        # First precompute possible sums without new weight
        base_possible = measurable(weights)
        # To speed up, precompute possible sums with new weight w:
        # possible_with_w = measurable(weights+[w]) but computing from scratch is O(3^m) per w
        # Instead, use "merging" with new weight:
        # For each sum s in base_possible, possible sums with w are s, s+w, |s-w|
        # So possible_with_w = union of s, s+w, |s-w| for s in base_possible
        # Then check if all amounts in amounts are in possible_with_w
        # So we implement a fast check per candidate w
        def can_all_with_new_w(w):
            new_possible = set()
            for s in base_possible:
                new_possible.add(s)
                new_possible.add(s + w)
                new_possible.add(abs(s - w))
            return all(a in new_possible for a in amounts)
        ans = -1
        # If some amount < max in weights, we try from 1 to max_search to find minimal
        # But max_search can be large => optimize by testing only necessary w's
        # Alternative: since weights up to 10^8 and amounts up to 10^9,
        # But limit is 100 data sets, ok to do linear test up to max_search
        for w in range(1, max_search+1):
            if can_all_with_new_w(w):
                ans = w
                break
        print(ans)

if __name__ == "__main__":
    solution()