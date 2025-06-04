import queue

def read_input():
    """
    Reads the input values for a single test case.
    
    Returns:
        m (int): The maximum number of steps allowed.
        n (int): The number of positions.
        d (list of int): The list of extra moves from each position. Index 0 and n+1 are placeholders.
    """
    m = int(input())
    if m == 0:
        return None, None, None  # Indicates the termination signal
    n = int(input())
    d = [0] * (n + 2)  # Initialize extra movement values for positions 0 .. n+1
    for i in range(1, n + 1):
        d[i] = int(input())
    return m, n, d

def forward_bfs(m, n, d):
    """
    Performs a forward search from position 0 and builds the graph of reachable states.
    Also builds reverse edges for use in the backward search.
    
    Args:
        m (int): Maximum allowed jump from current position.
        n (int): Number of positions.
        d (list of int): Extra moves applied at each position.
        
    Returns:
        visited (list of bool): True if a position has been reached in the forward move.
        rev (list of list): rev[k] contains positions that can reach position k in one step.
    """
    visited = [False] * (n + 2)      # Mark if node i has been visited in forward BFS
    visited[0] = True                # Start from position 0
    rev = [[] for _ in range(n + 2)] # Record reverse edges (for backward check)
    que = queue.LifoQueue()          # Use LIFO queue (DFS-like)

    que.put(0)
    while not que.empty():
        i = que.get()
        for j in range(1, m + 1):               # Try all possible jumps from 1 to m
            if i + j > n + 1:                   # If jump goes past the end, stop
                break
            # Compute target position after jump and extra move
            k = min(max(i + j + d[i + j], 0), n + 1)
            rev[k].append(i)                    # Record that k can be reached from i
            if not visited[k]:
                que.put(k)
                visited[k] = True
    return visited, rev

def backward_bfs(n, rev):
    """
    Performs backward search from the final position n+1 to determine reverse reachability.
    
    Args:
        n (int): Number of positions.
        rev (list of list): rev[k] contains all nodes that can reach k in one step.

    Returns:
        ok (list of bool): True if the position can reach the end (n+1) in reverse search.
    """
    ok = [False] * (n + 2)    # ok[i] indicates if position i is "OK" (can reach n+1)
    ok[n + 1] = True          # Start backwards from the goal n+1
    que = queue.LifoQueue()

    que.put(n + 1)
    while not que.empty():
        i = que.get()
        for j in rev[i]:      # For each node that can reach i
            if not ok[j]:
                ok[j] = True
                que.put(j)
    return ok

def evaluate_result(visited, ok, n):
    """
    Evaluates the final result for the current test case.
    
    Args:
        visited (list of bool): Visited state from forward BFS.
        ok (list of bool): "OK" status from backward BFS.
        n (int): Number of positions.

    Returns:
        ans (str): "OK" if the puzzle is solvable, "NG" otherwise.
    """
    if not visited[n + 1]:
        return 'NG'
    for i in range(n + 1):
        if visited[i] and (not ok[i]):
            # If reached position i in forward search, but it can't reach the end
            return 'NG'
    return 'OK'

def main():
    """
    Main loop to repeatedly process test cases until a termination signal is encountered.
    """
    while True:
        m, n, d = read_input()
        if m is None:
            break  # End of input detected

        visited, rev = forward_bfs(m, n, d)   # Get reachable states and reverse edges
        ok = backward_bfs(n, rev)             # Backward analysis from the end
        ans = evaluate_result(visited, ok, n) # Final output: "OK" or "NG"
        print(ans)

if __name__ == "__main__":
    main()