import sys
input = sys.stdin.readline

def main():
    """
    Main function that reads graph and dice values from input, processes assignments and outputs results.

    The logic is:
    1. Read the number of nodes (N), edges (M), and list of dice values (D).
    2. Read the edges, and map each (undirected, sorted) edge to its input index.
    3. For each node, store its neighbors in adjacency list E.
    4. Sort nodes by their die value, processing in increasing order.
    5. Assign each node and its neighbor to "B" (Black) or "W" (White) following problem constraints, populating answer arrays.
    6. Output the color assignments and processed values for each edge.
    """
    # Read number of nodes and edges
    N, M = map(int, input().split())

    # Read the dice values for nodes (0-indexed)
    D = list(map(int, input().split()))

    # Read the M edges, store as sorted tuples for undirected representation (node indices start from 1)
    EDGE = [tuple(sorted(map(int, input().split()))) for _ in range(M)]

    # Map each edge (as tuple of sorted node indices) to its index in input
    DICE = dict()
    for idx, edge in enumerate(EDGE):
        DICE[edge] = idx

    # Initialize adjacency list for nodes (1-based indexing, node 1 to N)
    E = [[] for _ in range(N + 1)]
    for x, y in EDGE:
        E[x].append(y)
        E[y].append(x)

    # Prepare a list that pairs each dice value with the corresponding node index (for sorting)
    # Nodes are 1-indexed, enumerate returns (index 0...N-1, value)
    P = [(val, ind + 1) for ind, val in enumerate(D)]
    P.sort()  # Sort by dice value, increasing order

    # Prepend a dummy zero for 1-based indexing of D
    D = [0] + D

    # Results:
    # DECIDED: list of color assignments for nodes ("" if undecided, else "B" or "W"). 1-based index.
    # DIS: stores values to be output for each edge, default -1.
    DECIDED = [""] * (N + 1)
    DIS = [-1] * M

    # Main loop: process nodes in increasing order of dice values
    for x, po in P:
        flag = 0
        # Check if any neighbor of node 'po' is already assigned ("B" or "W")
        for to in E[po]:
            if DECIDED[to] != "":
                flag = 1
                break

        if flag == 0:
            # If all neighbors are unassigned, try to find a neighbor 'to' with dice value equal to 'x'
            for to in E[po]:
                if D[to] == x:
                    # Assign colors to 'po' and 'to'
                    DIS[DICE[tuple(sorted([po, to]))]] = x
                    DECIDED[po] = "B"
                    DECIDED[to] = "W"
                    break
            else:
                # No suitable neighbor found: impossible configuration
                print(-1)
                sys.exit()
        else:
            # Some neighbor(s) of po are already assigned
            for to in E[po]:
                if DECIDED[to] != "" and DECIDED[po] == "":
                    # Assign opposite color to current node
                    if DECIDED[to] == "B":
                        DECIDED[po] = "W"
                    else:
                        DECIDED[po] = "B"
                    # Set edge value to the current dice value
                    DIS[DICE[tuple(sorted([po, to]))]] = x
                    break
                elif DECIDED[to] != "" and DECIDED[po] == DECIDED[to]:
                    # If neighbor has same color as current, update edge value accordingly
                    if x <= D[to]:
                        continue
                    DIS[DICE[tuple(sorted([po, to]))]] = x - D[to]
                    break
                elif DECIDED[to] != "" and DECIDED[po] != DECIDED[to]:
                    # If neighbor has different color, update edge value accordingly if possible
                    if x <= D[to]:
                        continue
                    DIS[DICE[tuple(sorted([po, to]))]] = x
                    break

    # Output the assignment string (skip 0th index)
    print("".join(DECIDED[1:]))

    # Output processed edge values
    for d in DIS:
        if d == -1:
            print(10 ** 9)
        else:
            print(d)

if __name__ == "__main__":
    main()