n = int(input())
D = [list(map(int, input().split())) for i in range(n)]
# D contains n elements, each is a list of three integers [cost, order, value]

# Memoization dictionary to store results of subproblems:
# Key: (state, pos) where state is a bitmask representing visited nodes,
# and pos is the current position.
# Value: tuple (minimum_cost, order_tuple)
# Initialize with all nodes visited (2**n - 1) and position i having cost 0 and empty order.
memo = {(2**n - 1, i): (0, ()) for i in range(n)}

def dfs(state, pos, w):
    """
    Recursive depth-first search with memoization to find the minimal cost path.

    Args:
        state (int): Bitmask representing which nodes have been visited.
        pos (int): Current node index.
        w (int): Accumulated weight factor affecting cost calculation.

    Returns:
        tuple: (minimum_cost, tuple_of_order) for the best path starting from current state.
    """
    # If the current state and position is already computed, return stored result
    if (state, pos) in memo:
        return memo[state, pos]

    res = None  # Initialize result as None, to find minimum
    for i in range(n):
        # Check if node i is not visited in current state
        if (state >> i) & 1 == 0:
            d0 = D[pos][1]  # order value at current position pos
            s, d1, v = D[i]  # cost, order, and value for the candidate node i
            # Recursively call dfs for new state including node i, new position i,
            # and updated weight incremented by 20 * v
            r = dfs(state | (1 << i), i, w + 20 * v)
            # Calculate new cost as previous cost plus absolute difference in orders times (70 + w)
            val = (r[0] + abs(d0 - d1) * (70 + w), r[1] + (s,))
            # Update result if this path has lower cost or if no result yet
            if res is None or val < res:
                res = val

    # If at least one extension was found, store in memo and return
    if res:
        memo[state, pos] = res
    return res

def solve():
    """
    Generates solutions starting from each node.

    Yields:
        tuple: (minimum_cost, tuple_of_order) for each starting node path.
    """
    for i in range(n):
        s0, d0, v0 = D[i]
        # Start DFS with only node i visited, position i, weight initialized at 20*v0
        result = dfs(1 << i, i, 20 * v0)
        # Yield the total cost and order sequence including starting node s0
        yield result[0], result[1] + (s0,)

# Find the minimal cost solution among all starting nodes
ans = min(solve())

# Print the order sequence in reverse
print(*reversed(ans[1]))