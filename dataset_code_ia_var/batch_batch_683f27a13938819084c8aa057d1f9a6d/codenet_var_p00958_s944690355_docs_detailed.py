def read_input():
    """
    Reads input from the standard input.
    Returns:
        m (int): The number of points.
        P (List[List[int]]): List of (x, y) coordinates for each point.
    """
    m = int(input())
    P = [list(map(int, input().split())) for _ in range(m)]
    return m, P

def compute_unique_directions(m, P):
    """
    Computes all unique directions (as vector differences) between all pairs of points up to proportionality.
    Only keeps one representative per direction.

    Args:
        m (int): Number of points.
        P (List[List[int]]): List of (x, y) point coordinates.

    Returns:
        s (set): Set of unique (u, v) pairs representing direction vectors.
    """
    s = set()  # Set to store unique direction vectors
    for i in range(m):
        xi, yi = P[i]
        for j in range(i + 1, m):
            xj, yj = P[j]
            u = xj - xi
            v = yj - yi
            # Check if this direction (u, v) is already represented in 's'
            for x, y in s:
                if x * v == y * u:
                    # Found a proportional direction
                    break
            else:
                # New unique direction
                s.add((u, v))
    return s

def dfs(state, dx, dy, m, P, s, memo):
    """
    Performs a depth-first search with dynamic programming to find the maximal value
    obtainable by iteratively pairing points and marking them as used, following the rules
    defined on the direction and state.

    Args:
        state (int): Bitmask representing used points (1 = used).
        dx (int): x-component of the current direction vector.
        dy (int): y-component of the current direction vector.
        m (int): Total number of points.
        P (List[List[int]]): Points and their coordinates.
        s (set): Set of unique direction vectors.
        memo (dict): Memoization dictionary.

    Returns:
        res (int): Maximum result computed from the current state and direction.
    """
    if (state, dx, dy) in memo:
        return memo[(state, dx, dy)]
    pstate = state  # Keep the original state for memoization
    update = 1      # Flag to track if any new pairing happened in this round
    cnt = -1        # Counter for the number of successful pairings
    while update:
        update = 0
        cnt += 1
        for i in range(m):
            if (state >> i) & 1:
                continue  # Point i already used
            xi, yi = P[i]
            for j in range(i + 1, m):
                if (state >> j) & 1:
                    continue  # Point j already used
                xj, yj = P[j]
                u = xj - xi
                v = yj - yi
                # Check if the direction of (i, j) matches the current direction
                if dx * v == dy * u:
                    update = 1
                    # Mark both points as used
                    state |= (1 << i) | (1 << j)
                    break
            if update:
                break  # Restart search after updating state
    # If less than or equal to one pairing made, the base case value is 0
    if cnt <= 1:
        res = 0
    else:
        # Otherwise, compute value for current configuration and recurse on all possible directions
        res = cnt * (cnt - 1) // 2 + max(dfs(state, *e, m, P, s, memo) for e in s)
    memo[(pstate, dx, dy)] = res  # Memoize the result
    return res

def main():
    """
    Main function to read input, process unique directions, and find the maximal achievable value
    using a combinatorial search with memoization.
    """
    m, P = read_input()
    s = compute_unique_directions(m, P)
    memo = {}  # Dictionary for memoization to store computed subproblem results
    # Run the DFS for all unique directions as starting directions
    res = max(dfs(0, *e, m, P, s, memo) for e in s)
    print(res)

# Entry point for program execution
if __name__ == "__main__":
    main()