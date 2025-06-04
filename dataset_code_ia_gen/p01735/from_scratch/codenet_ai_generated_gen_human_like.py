import sys
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
children = []
for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    k = line[0]
    if k > 0:
        children.append(line[1:])
    else:
        children.append([])

# We want to compute min and max number of leaf evaluations
# Algorithm: simulate negamax with arbitrary order of children
# Since negamax returns max of (-child), the pruning depends on order.
# We compute min and max leaf counts by trying best/worst order of children.
# Use memoization (dp) with alpha, beta parameters is impossible due to range;
# Instead, at each node, we compute min/max number of leaves given alpha, beta,
# but since alpha and beta depend on path, we simulate all orders and choose min/max.

# Because of constraints, we use a simplified approach:
# For min leaves:
# - order children to maximize pruning (best order)
# For max leaves:
# - order children to minimize pruning (worst order)

# At leaf: one evaluation
# At internal node:
# - evaluate children in some order
# - accumulate leaf count
# - prune if val >= beta

# We will implement two functions for min and max counts.

def negamax_counts(node, alpha, beta, children_order):
    # node: current node index 0-based
    # alpha, beta: current alpha, beta values
    # children_order: list of children indices in the order we evaluate

    # leaf node
    if len(children[node]) == 0:
        return 1  # one leaf evaluation

    leaf_counts = 0
    curr_alpha = alpha
    for c in children_order:
        val = -negamax_counts(c, -beta, -curr_alpha, sorted_children_minmax[c])
        leaf_counts += leaves_min_max[c][val == leaves_min_max[c][2]]  # accumulate evaluated leaves for child (to be updated later)
        if val >= beta:
            return leaf_counts
        if val > curr_alpha:
            curr_alpha = val
    return leaf_counts

# Problem is that in negamax, value depends on child values, we need to know value to choose prune.

# Alternate approach:
# We precompute for every node:
# - its negamax value (given in p if leaf, else computed)
# - minimum and maximum number of leaves evaluations with best and worst order of children

# We do bottom-up DP:

from functools import lru_cache

@lru_cache(None)
def negamax_value(u):
    if not children[u]:
        return p[u]
    vals = []
    for c in children[u]:
        val = negamax_value(c)
        vals.append(-val)
    return max(vals)

# For computing number of leaves in min and max order:

def dfs(u):
    if not children[u]:
        # leaf node, value is p[u], leaf count is 1
        return p[u], 1, 1  # val, min_leaves, max_leaves
    child_data = []
    for c in children[u]:
        val_c, min_c, max_c = dfs(c)
        child_data.append(( -val_c, c, min_c, max_c ))  # negated val (value returned by child negamax)
    # Now evaluate min leaves by best order:
    # Best order: sort children by descending negated_val to prune earlier
    child_data_min = sorted(child_data, key=lambda x: x[0], reverse=True)
    # Worst order: sort children by ascending negated_val to prune later
    child_data_max = sorted(child_data, key=lambda x: x[0])

    # Compute min_leaves
    alpha = -10**10
    beta = 10**10
    leaves_min = 0
    curr_alpha = alpha
    for val, c, min_c, max_c in child_data_min:
        leaves_min += min_c
        if val >= beta:
            break
        if val > curr_alpha:
            curr_alpha = val

    # Compute max_leaves
    alpha = -10**10
    beta = 10**10
    leaves_max = 0
    curr_alpha = alpha
    for val, c, min_c, max_c in child_data_max:
        leaves_max += max_c
        if val >= beta:
            break
        if val > curr_alpha:
            curr_alpha = val

    val_u = max(x[0] for x in child_data_min)
    return -val_u, leaves_min, leaves_max

val_root, min_eval, max_eval = dfs(0)

print(min_eval, max_eval)