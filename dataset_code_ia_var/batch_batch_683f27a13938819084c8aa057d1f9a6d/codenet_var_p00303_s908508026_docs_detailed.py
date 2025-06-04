def read_input():
    """
    Reads the input for the graph construction.
    Returns:
        int: Number of constraints (N).
        list: A list of tuples, each representing a constraint in the form (u, relation, v).
    """
    N = int(input())
    constraints = []
    for _ in range(N):
        u, r, v = input().split()
        constraints.append((int(u), r, int(v)))
    return N, constraints

def build_graph(N, constraints):
    """
    Builds the directed graph based on the given constraints.
    The graph uses a two-part index trick (0-99 for variables, 100-199 for their lock versions).

    Args:
        N (int): Number of constraints.
        constraints (list): List of tuples containing the constraints.

    Returns:
        tuple: 
            - G (list): Graph represented as adjacency lists.
            - U (list): Marker list signifying used nodes.
    """
    G = [[] for _ in range(200)]  # Create adjacency lists for up to 200 nodes
    U = [0] * 200                 # Track which nodes are involved in constraints
    for i in range(N):
        u, relation, v = constraints[i]
        u -= 1  # Convert to 0-based index
        v -= 1
        U[u] = 1            # Mark variable node as used
        U[v + 100] = 1      # Mark lock node as used
        if relation == 'lock':
            G[u].append(v + 100)  # u -> lock(v)
        else:
            G[v + 100].append(u)  # lock(v) -> u
    return G, U

def dfs(v, G, used, hold):
    """
    Performs DFS traversal to detect cycles in the directed graph.

    Args:
        v (int): Current node.
        G (list): Graph's adjacency lists.
        used (list): Visited status of nodes (0: unvisited, 1: visited).
        hold (list): Recursion stack tracking active path of DFS.

    Returns:
        int: 1 if a cycle is found, else 0.
    """
    if used[v]:
        return 0  # Node already processed, no need to continue
    r = 0         # Result variable to track if a cycle is detected
    hold[v] = 1   # Mark the current node as being in the current path (active)
    for w in G[v]:
        if hold[w]:    # Found a back edge indicating a cycle
            r = 1
            continue
        r |= dfs(w, G, used, hold)  # Explore neighbors
    hold[v] = 0      # Unmark node from recursion stack after visiting all neighbors
    used[v] = 1      # Mark node as fully processed
    return r

def main():
    """
    Main function. Reads input, builds the graph, and checks for cycles
    among the relevant nodes. Outputs 1 if a cycle is found (contradiction), else 0.
    """
    # Step 1: Read constraints from input
    N, constraints = read_input()
    # Step 2: Build the graph and get usage marker array
    G, U = build_graph(N, constraints)

    used = [0] * 200  # Used/visited marker for each node
    hold = [0] * 200  # Recursion stack tracker

    # Step 3: Check each relevant node for cycles using DFS
    for i in range(200):
        if not U[i]:    # Only process nodes involved in constraints
            continue
        if dfs(i, G, used, hold):  # If a cycle is found, print 1 and exit
            print(1)
            break
    else:
        print(0)    # No cycles found: output 0

if __name__ == "__main__":
    main()