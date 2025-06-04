def main():
    """
    Main loop for processing multiple test cases. For each test case, the user is prompted
    for the values of n (nodes) and m (edges), followed by m edges. For each case, it checks 
    if the described graph is a collection of cycles or simple paths where no vertex has degree >2.
    Prints 'yes' if so, 'no' otherwise.
    """
    while True:
        # Read input values for number of nodes n and edges m
        try:
            n, m = map(int, raw_input().split())
        except Exception:
            # In case of malformed input, break
            break
        # If n is 0, exit the loop (termination condition)
        if n == 0:
            break

        # Initialize adjacency lists for all nodes, 0 is a special entry to track unused nodes
        D = [[] for _ in range(n + 1)]
        # D[0] will hold all unvisited node indices (from 1 to n)
        D[0] = range(1, n + 1)
        # Flag to indicate if a degree constraint has been violated
        nflg = 0

        # Read and process all m edges
        for i in range(m):
            u, v = map(int, raw_input().split())
            # Add edge to adjacency lists
            D[u].append(v)
            D[v].append(u)
            # If any node's degree exceeds 2, set violation flag
            if len(D[u]) > 2 or len(D[v]) > 2:
                nflg = 1

        if nflg:
            # If any node has degree >2, it is not a collection of paths/cycles
            print 'no'
        else:
            # bkf is a flag for early break when an inconsistency is found
            bkf = 0
            # While there are unvisited nodes
            while len(D[0]) > 0:
                # Pop an unvisited starting node
                st = D[0].pop()
                # If this node is not isolated, but in a cycle, put it back for later
                if len(D[st]) == 2:
                    D[0].append(st)
                # st0 will be used to track the starting node for cycle detection
                st0 = st
                # Start traversing the connected component from st
                while len(D[st]) != 0:
                    # Pick a neighbor
                    nxt = D[st].pop()
                    # If neighbor is not the starting node, continue traversal
                    if nxt != st0:
                        # Remove this neighbor from the unvisited list and its back edge
                        D[0].remove(nxt)
                        D[nxt].remove(st)
                        # Advance to the neighbor
                        st = nxt
                    else:
                        # Found a backward edge to the starting node => invalid configuration
                        print 'no'
                        bkf = 1
                        break
                # If an invalid configuration was found, break out of main loop
                if bkf:
                    break
            else:
                # If all connected components checked out, graph is a collection of cycles/paths
                print 'yes'

if __name__ == "__main__":
    main()