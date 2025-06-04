import sys
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

# Read children information
children = []
for _ in range(n):
    line = sys.stdin.readline().split()
    k = int(line[0])
    if k == 0:
        children.append([])
    else:
        children.append([int(x)-1 for x in line[1:]])

# Memoization dictionaries indexed by (node, alpha, beta) are impossible because alpha, beta vary widely.
# We will instead compute results bottom-up.

# But the problem requires simulating negamax with alpha-beta pruning with arbitrary ordering of children.
# We want to find minimal and maximal number of leaf evaluations done by choosing the best order.

# Key points:
# For leaves:
#   Value is known (p[node])
#   Leaf evaluations count is 1 always
# For non-leaf nodes:
#   p[node] = 0 always (given by problem)
#   Value is max of (- value(child)) over children
# We want to simulate negamax with alpha-beta pruning.
# negamax(node, alpha, beta) returns best value (an int) and counts number of leaf evaluations.
# Because order of children affects pruning, we want minimal and maximal leaf counts over all permutations.

# We solve this by dynamic programming bottom-up:
# For each node we compute:
# - Its value (the node value)
# - Minimal number of leaf evaluations needed to compute it
# - Maximal number of leaf evaluations needed to compute it

# But since evaluation depends on alpha and beta, and these change over recursion,
# we cannot consider only node to compute the pruning counts.

# Alternative:
# Because alpha-beta depends on alpha, beta dynamic per call,
# but the root call is negamax(0, -inf, +inf)

# The key paper or reasoning is: the child nodes can be evaluated in any order,
# we want minimal and maximal leaf count over all possible orderings.

# Observation:
# We can solve this top-down with memoization:
# For each node, if leaf: return (value, leaf_count=1)
# If non-leaf:
#   We do all permutations of children and simulate
#   But that is too many permutations (up to 5 children => 120 permutations)
#   So we devise a DP/memo approach:
#   The algorithm to explore children:
#    for each child in order:
#       val := -negamax(child, -beta, -alpha)
#       if val >= beta: prune and return val
#       if val > alpha: alpha = val
#    return alpha

# Since we want minimal and maximal number of leaves evaluated over all child orderings, for fixed alpha, beta:
# We try all orders and take min and max counts of pruning.

# But alpha, beta vary widely.
# The trick:
# Actually, the value returned for each node is always fixed regardless of order because p is fixed.
# Because negamax chooses max of (-value(child)) and values don't change whatever the order,
# the value returned for a node is fixed.

# So for each node, compute its value first:
# If leaf: value = p[node]
# Else: value = max( - value(child) for child in children )
# Memoize values.

# With values known, we can explore the minimal and maximal leaf evaluation counts
# by simulating alpha-beta pruning where pruning depends on pruning condition val >= beta.
# Since order of children affects pruning, we select order to minimize or maximize leaf evaluations.

# Approach:
# For each node, define a function dfs(alpha, beta) returning (value,node), (min_leaf_count), (max_leaf_count)
# But alpha-beta bounds change continuously, so too many to memoize.

# Alternative:
# Because values are integral from -10000 to 10000, only few distinct values for alpha and beta.
# We can precompute values of children, sort them in order of values decreasing.
# We attempt to find minimal and maximal leaf counts by exploring all permutations of children:
# For pruning:
#   prune if val >= beta
# Explore all permutations:

# Since max 5 children => 120 permutations max, feasible to try all.

# At each node:
#   For minimal leaf count:
#      try child orders in all permutations and simulate pruning, pick minimal leaf count
#   For maximal leaf count:
#      pick maximum leaf count over permutations.

# The problem size n=100 and max 5 children, so this is feasible.

from itertools import permutations

# Memoize node values
val_cache = [None]*n

def calc_value(u):
    # Compute node value recursively
    if val_cache[u] is not None:
        return val_cache[u]
    if len(children[u])==0:
        val_cache[u] = p[u]
        return val_cache[u]
    best = -1000000000
    for c in children[u]:
        cval = calc_value(c)
        v = - cval
        if v > best:
            best = v
    val_cache[u] = best
    return best

for i in range(n):
    calc_value(i)

# Now simulate negamax with alpha-beta pruning and count leaf evaluations for a given order of children
def negamax_sim(u, alpha, beta, order):
    # returns (value, leaf_evals)
    if len(children[u])==0:
        # leaf
        return p[u], 1
    val = -1000000000
    leaf_count = 0
    for c in order:
        v, cnt = negamax_sim(c, -beta, -alpha, get_order_for_node[c])
        v = -v
        leaf_count += cnt
        if v >= beta:
            # prune
            val = v
            return val, leaf_count
        if v > alpha:
            alpha = v
            val = v
    return val, leaf_count

# But get_order_for_node is needed for child nodes.
# To handle this, we will do it recursively:
# To find minimal leaf count:
# - for each node, try all permutations of children
# - for each permutation, sum leaf counts of negamax calls on children (which are recursively computed minimal or maximal)

# A clean approach:

# We memoize minimal and maximal leaf counts for each node.

# Because we want minimal leaf counts for root, we find minimal leaf counts for children first.

# When recursion is called, and order is chosen, each child's leaf counts used must be minimal or maximal accordingly.

# So we define:

# For all nodes:
# we want to compute minimal and maximal leaf counts.
# For leaves:
#   min = max = 1
# For non-leaf:
#   For "min" leaf count:

#   For all permutations:
#     simulate negamax pruning using minimal leaf counts for subcalls
#     choose minimal sum leaf counts over all permutations

#   Similarly for maximal

# We implement these dfs with memoization on node id only because values are fixed.

# We define functions:

min_leaf_cache = [None]*n
max_leaf_cache = [None]*n

def min_leaf_count(u, alpha, beta):
    # returns minimal leaf count to evaluate node u with alpha-beta bounds alpha,beta
    # Since alpha-beta depends on bounds, and they change,
    # To avoid complexity, we use:
    # We always start from root with alpha=-inf, beta = +inf,
    # and since negamax returns fixed value for each node independently, we can
    # implement a function that tries all permutations on node children to get minimal leaf count.

    # Since alpha and beta changes complicatedly, we ignore alpha,beta in parameters,
    # because those parameters affect pruning and order selection.
    # To correctly simulate alpha-beta pruning, we implement a helper function that simulates with pruning.

    # Actually, in min_leaf_count, we want minimal leaf count starting with alpha,beta
    # but in problem it's always called with alpha=-inf, beta=+inf at root
    # So parameters can be ignored at this stage, we simulate pruning per order.

    # We'll implement a helper simulate_pruning(u, alpha, beta, order, leaf_count_cache) to simulate leaf counts given order.

    # At this stage, to avoid complicated parameter passing, we'll implement a helper in the global scope.

    raise Exception('Do not call min_leaf_count with alpha and beta, use min/max_leaf_count_general')

def max_leaf_count(u, alpha, beta):
    raise Exception('Do not call max_leaf_count with alpha and beta, use min/max_leaf_count_general')

# Implement simulate pruning count for a given order of children for node u
def simulate_pruning(u, alpha, beta, order, leaf_count_func):
    # leaf_count_func: function to get leaf count for a child node, either minimal or maximal
    # returns leaf counts when evaluating node u with given order and alpha-beta

    if len(children[u])==0:
        # leaf node, leaf count is 1
        return 1

    leaf_sum = 0
    for c in order:
        # recursive call for child
        leaf_sum += leaf_count_func(c)
        v = - val_cache[c]
        if v >= beta:
            return leaf_sum  # prune
        if v > alpha:
            alpha = v
    return leaf_sum

# Since leaf_count_func requires minimal or maximal leaf counts for child nodes,
# we must define min_leaf_count(u) and max_leaf_count(u) functions that compute those values recursively.

def min_leaf_count(u):
    if min_leaf_cache[u] is not None:
        return min_leaf_cache[u]
    if len(children[u]) == 0:
        min_leaf_cache[u] = 1
        return 1
    res = 10**9
    ch = children[u]
    # try all permutations
    for order in permutations(ch):
        leaf_count = simulate_pruning(u, -1000000000, 1000000000, order, min_leaf_count)
        if leaf_count < res:
            res = leaf_count
    min_leaf_cache[u] = res
    return res

def max_leaf_count(u):
    if max_leaf_cache[u] is not None:
        return max_leaf_cache[u]
    if len(children[u]) == 0:
        max_leaf_cache[u] = 1
        return 1
    res = 0
    ch = children[u]
    for order in permutations(ch):
        leaf_count = simulate_pruning(u, -1000000000, 1000000000, order, max_leaf_count)
        if leaf_count > res:
            res = leaf_count
    max_leaf_cache[u] = res
    return res

# Print minimal and maximal leaf counts on root node 0
print(min_leaf_count(0), max_leaf_count(0))