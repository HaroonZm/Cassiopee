from collections import deque  # Import the deque class from the collections module, which allows fast appends and pops from both ends of a queue
import sys  # Import the sys module to interact with the system (for standard input/output)

# Assign the readline function from sys.stdin to a variable named readline, for fast line-by-line input
readline = sys.stdin.readline
# Assign the write function from sys.stdout to a variable named write, for fast output writing
write = sys.stdout.write

def solve():
    # Read a line of input, split it into separate strings, and map them to integers (for H, W, R, C)
    H, W, R, C = map(int, readline().split())
    # Subtract 1 from R and C to convert from 1-based to 0-based indexing for positions in a 2D array
    R -= 1
    C -= 1

    # If both H and W are zero, this indicates the end of input; return False to stop processing
    if H == 0 and W == 0:
        return False

    # G0 and G1 will represent two adjacency lists for a graph; each is a list of lists with H*W+1 elements (one per cell and one extra node)
    G0 = [[] for i in range(H * W + 1)]  # Adjacency list for edges of type 0 (unlit)
    G1 = [[] for i in range(H * W + 1)]  # Adjacency list for edges of type 1 (lit)
    g = H * W  # The 'g' node represents an auxiliary, extra node used for border connections

    # Loop through each row of the grid (i goes from 0 to H-1)
    for i in range(H):
        # Read a line, split and convert it to integers; store it as a list called s (walls between NORTH and the row)
        *s, = map(int, readline().split())
        k = W * i  # 'k' is the offset for this row in the 1D representation of a 2D grid

        # If this is not the top row
        if i:
            for j in range(W):
                # For each cell (j), check if there is a wall (1 means the edge is 'lit', 0 is 'unlit') between this row and the row above
                if s[j]:
                    # If the edge is lit, add corresponding bidirectional edges to G1
                    G1[k + j].append(k + j - W)
                    G1[k + j - W].append(k + j)
                else:
                    # Otherwise, add to G0 (unlit edges)
                    G0[k + j].append(k + j - W)
                    G0[k + j - W].append(k + j)
        else:
            # Special handling for the top row, connect to the extra node 'g' instead of another row
            for j in range(W):
                if s[j]:
                    G1[j].append(g)
                    G1[g].append(j)
                else:
                    G0[j].append(g)
                    G0[g].append(j)

        # Read the next line, which describes the internal walls between columns in row i
        *s, = map(int, readline().split())
        for j in range(W - 1):
            # For each horizontal wall between columns (except the last column)
            if s[j + 1]:
                # If lit (edge of type 1), connect nodes in G1
                G1[k + j].append(k + j + 1)
                G1[k + j + 1].append(k + j)
            else:
                # If unlit (edge of type 0), connect nodes in G0
                G0[k + j].append(k + j + 1)
                G0[k + j + 1].append(k + j)
        # Now connect the leftmost and rightmost columns to the outside node 'g', using the info in s[0] and s[W]
        if s[0]:
            G1[k].append(g)
            G1[g].append(k)
        else:
            G0[k].append(g)
            G0[g].append(k)
        if s[W]:
            G1[k + W - 1].append(g)
            G1[g].append(k + W - 1)
        else:
            G0[k + W - 1].append(g)
            G0[g].append(k + W - 1)

    # After processing all rows, handle the walls at the southern border (bottom of the grid)
    *s, = map(int, readline().split())
    k = (H - 1) * W  # The starting index of the last row in the 1D grid
    for j in range(W):
        # For each cell in the bottom row, connect to outside node 'g' as above
        if s[j]:
            G1[k + j].append(g)
            G1[g].append(k + j)
        else:
            G0[k + j].append(g)
            G0[g].append(k + j)

    # u0 and u1 are visitation arrays: u0 tracks visited nodes in G0, u1 for G1; initialized to zero (not visited)
    u0 = [0] * (H * W + 1)
    u1 = [0] * (H * W + 1)
    # Start BFS (Breadth-First Search) from the extra node 'g'; mark it visited in both types
    u0[g] = 1
    u1[g] = 1

    que = deque([g])  # Initialize a double-ended queue (deque) and enqueue the starting node

    while que:
        # Pop a node from the left side of the deque to process as the current node 'v'
        v = que.popleft()
        # Explore all neighbors reachable via unlit edges (type 0)
        for w in G0[v]:
            if u0[w]:
                continue  # Skip if already visited in u0
            if u1[w]:
                que.append(w)  # If visited in u1, add to queue to propagate
            u0[w] = 1  # Mark as visited in u0
        # Explore all neighbors reachable via lit edges (type 1)
        for w in G1[v]:
            if u1[w]:
                continue  # Skip if already visited in u1
            if u0[w]:
                que.append(w)  # If visited in u0, add to queue to propagate
            u1[w] = 1  # Mark as visited in u1

    # After BFS, check if the target cell (after linearizing to 1D as R*W + C) was visited in u0
    if u0[R * W + C]:
        write("Yes\n")  # If yes, write 'Yes' to output (reachable)
    else:
        write("No\n")   # Otherwise, write 'No'
    return True  # Return True to continue processing further test cases

# Repeat the solve() function until it returns False (no more input regions to process)
while solve():
    ...  # The ellipsis is a no-op (does nothing) and is used here for syntax completeness