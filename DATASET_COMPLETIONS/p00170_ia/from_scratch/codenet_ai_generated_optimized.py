import sys
sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break
        items = []
        for _ in range(n):
            f,w,s = input().split()
            w = int(w)
            s = int(s)
            items.append((f,w,s))
        total_w = sum(w for _,w,_ in items)
        # DP: dp[mask] = (can_stack, total_weight, sum_iw, previous)
        # mask bit i means item i used
        # can_stack: bool if feasible
        # total_weight: sum of weights in mask
        # sum_iw: sum of i * weight_i in the stack (to compute G, order matters)
        # store sequence like dp is dictionary (mask -> (sum_w, sum_iw, previous, last))
        dp = {0:(0,0,-1,-1)}
        # To minimize G = (1*w1 + 2*w2 + ...)/total_w , we must order items to maximize sum_iw weighted by position i in stack
        # We will build stack from bottom to top, so position i=1 for bottom
        # We try to add one item on top of current stack
        for used_count in range(n):
            next_dp = {}
            for mask,state in dp.items():
                sum_w, sum_iw, prev_mask, last = state
                for i in range(n):
                    if (mask>>i)&1==0:
                        f,w,s = items[i]
                        # sum weight of items above this item = total stack weight - current item's weight and weights below it
                        # since we add on top, the item we add has no weight above it.
                        # Condition: s_i ≥ weight above it
                        # weight above = total_sum_w - sum_w (since sum_w is total weight in stack so far)
                        # Wait: We consider stacking bottom->top, when adding on top, new item's s >= 0 always holds
                        # Correct condition: For all items stacked below, their s >= weight above them
                        # But to keep feasibility, check if adding this item on top is ok:
                        # For new item: s_i >= 0 always true
                        # For items below, adding new weight on top must not violate their s_i
                        # So for all items in mask, s_i ≥ sum weights of items above them
                        # We store for each mask the minimal s_i - weight_above_i? Complex.

                        # Instead, use a recursive approach:
                        # When we add item on top, the new weight above existing stack items increases by w
                        # So we must check for all items in mask if s_i >= current above weight + w

                        # To efficiently check, we store for each state a dictionary or array of above weights per item, or store min slack?

                        # Because n ≤ 10, we can store for each dp state an array of 'remaining capacity' per item

                        # Let's store for each dp state: a list of residual capacities (s_i - weight above)

                        # But that would be huge. Instead, store per dp state, for each item in stack, the residual s_i after subtracting weight above.

                        # Since stack build order is known from prev_mask and last, we can reconstruct current order.

                        # We'll implement a recursive cache with memoization to find optimal order.

                        pass

        # Instead, implement with memoization over permutations:

def solve(items):
    from functools import lru_cache
    n = len(items)
    total_w = sum(w for _,w,_ in items)

    @lru_cache(None)
    def dfs(mask):
        if mask == (1<<n)-1:
            return (0, ())  # sum_iw=0, empty tuple stack top->bottom
        res = None
        for i in range(n):
            if (mask>>i)&1==0:
                # new mask with i added at bottom (since we build bottom up)
                next_mask = mask|(1<<i)
                # Try placing item i at bottom of stack built from dfs(mask)
                # Get dfs(mask) result: (sum_iw, sequence)
                sub_sum_iw, seq = dfs(next_mask)
                # Check feasibility:
                # weight above i = total weight of items in next_mask except i
                weight_above = sum(items[j][1] for j in range(n) if (next_mask>>j)&1 and j!=i)
                # i's strength s_i must be >= weight_above
                if items[i][2] < weight_above:
                    continue
                # For all items in seq (above i), check s_j >= sum weights above j
                # But seq is bottom to top excluding i
                # weight above j in seq increases by w_i because i is bottom
                # For each item in seq:
                # current weight above j in seq is weight_above_j
                # but now weight above j is weight_above_j + w_i
                # We must check s_j >= weight_above_j + w_i
                # This means we must track weight above each item in seq during recursion

                # To make it easier, store in dfs(mask) the stack sequence bottom->top and a list of weight_above per item

                # We'll implement a different signature:

    # We'll change dfs to return (max sum_iw, sequence) and propagate weights

    @lru_cache(None)
    def dfs2(mask, above_weight):
        # above_weight: dict of item->weight on top of this item
        if mask == (1<<n)-1:
            return (0, ())
        res = None
        for i in range(n):
            if (mask>>i)&1==0:
                # weight above i is above_weight.get(i,0)
                # When we put i on bottom, above weight above i is sum weights of items above i
                # The new above weights for items in mask will be above_weight[j]+w_i for j in mask items
                # We check s_i >= above_weight.get(i,0)
                if items[i][2] < above_weight.get(i,0):
                    continue
                # Update above_weight for items in mask: increase by w_i
                new_above_weight = {j: above_weight.get(j,0)+items[i][1] for j in range(n) if (mask>>j)&1}
                # i has no items above when placed at bottom
                new_above_weight[i] = 0
                sub_sum_iw, seq = dfs2(mask|(1<<i), tuple(sorted(new_above_weight.items())))
                if sub_sum_iw is None:
                    continue
                # Position of i is 1 + length of seq
                pos = len(seq)+1
                sum_iw = sub_sum_iw + pos*items[i][1]
                if res is None or sum_iw < res[0]:
                    continue
                if res is None or sum_iw > res[0]:
                    res = (sum_iw,(i,)+seq)
        if res is None:
            return (None, ())
        return res

    # above_weight as tuple sorted of pairs for memoization
    from collections import defaultdict
    import sys
    sys.setrecursionlimit(10**9)
    @lru_cache(None)
    def dfs3(mask, above_weight_tup):
        above_weight = dict(above_weight_tup)
        if mask == (1<<n)-1:
            return (0, ())
        res = None
        for i in range(n):
            if (mask>>i)&1==0:
                w_i = items[i][1]
                s_i = items[i][2]
                aw_i = above_weight.get(i,0)
                if s_i < aw_i:
                    continue
                new_above_weight = {}
                for j in range(n):
                    if (mask>>j)&1:
                        new_above_weight[j] = above_weight.get(j,0)+w_i
                new_above_weight[i] = 0
                next_sum_iw, seq = dfs3(mask|(1<<i), tuple(sorted(new_above_weight.items())))
                if next_sum_iw is None:
                    continue
                pos = len(seq)+1
                total_sum_iw = next_sum_iw + pos*w_i
                if res is None or total_sum_iw > res[0]:
                    res = (total_sum_iw, (i,) + seq)
        if res is None:
            return (None, ())
        return res

    ans = dfs3(0, ())
    seq = ans[1]
    # seq is tuple of indices in order bottom->top
    return [items[i][0] for i in seq]

import sys
def run():
    input=sys.stdin.readline
    while True:
        n=int(input())
        if n==0:
            break
        items=[]
        for _ in range(n):
            f,w,s = input().split()
            w=int(w)
            s=int(s)
            items.append((f,w,s))
        res = solve(items)
        for r in res:
            print(r)
run()