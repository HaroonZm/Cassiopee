from collections import Counter

def get_par(x, par_lst):
    """
    Find the representative (parent) of the set containing element x in a disjoint-set (union-find) structure.
    Implements path compression for optimization.

    Args:
        x (int): The index of the current node.
        par_lst (list of int): The parent list where par_lst[i] is the parent of node i.

    Returns:
        int: The representative (root parent) of the set containing x.
    """
    # If x is its own parent, return x (x is the root of its set)
    if x == par_lst[x]:
        return x
    # Recursively find the root parent of x
    ret = get_par(par_lst[x], par_lst)
    # Path compression: directly connect x to its root parent for efficiency
    par_lst[x] = ret
    return ret

def main():
    """
    Main loop to process multiple test cases. For each case:
    - Reads the number of nodes (n) and edges (m).
    - Processes each edge, updating union-find structure and degree counters.
    - After processing, checks graph constraints:
        * No node can have a degree > 2.
        * The graph must remain a forest (i.e., no cycles).
    Prints "yes" if all constraints are satisfied, otherwise "no".
    Terminates when the number of nodes (n) is zero.
    """
    while True:
        # Read number of nodes n and number of edges m
        n, m = map(int, input().split())
        # Exit condition: n==0 signifies end of input
        if n == 0:
            break

        # Initialize union-find parent list: each node is its own parent initially
        par_lst = [i for i in range(n)]
        # Degree counter for each node
        counter = [0] * n
        # Flag to indicate if graph violates constraints (cycle or degree>2)
        flag = False

        # Process all edges
        for _ in range(m):
            u, v = map(int, input().split())
            # Convert to 0-based index
            u -= 1
            v -= 1
            # Increment the degree of nodes u and v
            counter[u] += 1
            counter[v] += 1

            # Find root parents of both nodes
            pu, pv = get_par(u, par_lst), get_par(v, par_lst)
            if pu == pv:
                # Cycle detected
                flag = True
            else:
                # Union operation: Merge the two sets
                par_lst[pu] = pv

        # Check if any node has degree greater than 2 (invalid for a simple path or cycle)
        if max(counter) > 2:
            flag = True
        # Output result based on detected conditions
        if flag:
            print("no")
        else:
            print("yes")

main()