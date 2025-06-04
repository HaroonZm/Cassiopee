import sys
from collections import deque

def solve():
    """
    Reads a tree structure from stdin, assigns values (colors) to each node in a greedy manner,
    and outputs the sum of all assigned colors except for the largest one, as well as the colors
    assigned to each node.
    
    The input must be formatted as:
    - An integer N (number of nodes)
    - N-1 lines with pairs of integers (edges of the tree, 1-based indices)
    - A line with N space-separated integers (the available colors/values)
    
    Prints:
    - The sum of assigned colors except the largest one
    - The list of colors assigned to each node, in order
    """

    # Local function 'input' reads a line from stdin (faster input in contests)
    input = sys.stdin.readline

    # Read number of nodes in the tree
    N = int(input())

    # Initialize adjacency list for all nodes (0-based indexing)
    Edge = [[] for _ in range(N)]

    # Read tree edges, build adjacency list (convert to 0-based indexing)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        Edge[a - 1].append(b - 1)
        Edge[b - 1].append(a - 1)

    # Read colors/values, convert to list of integers and sort descendingly (largest first)
    C = [int(c) for c in input().split()]
    C.sort(reverse=True)

    # Initialize a list to store the assigned color for each node (None means not assigned yet)
    Color = [None] * N

    # Assign the largest color to node 0 (usually the root in such problems)
    Color[0] = C[0]

    # Prepare a queue for BFS traversal; store tuples of (current node, parent node)
    q = deque()
    for e in Edge[0]:
        q.append((e, 0))

    # Initialize the answer to 0 (will sum the assigned colors except the largest one)
    ans = 0

    # Assign the next largest colors one by one to the rest of the nodes using BFS order
    for i in range(1, N):
        # Get the next node to process and its parent
        nowN, preN = q.popleft()
        # Add this color to the answer (since the largest, C[0], is not included in ans)
        ans += C[i]
        # Assign the color to the node
        Color[nowN] = C[i]
        # Add unvisited neighbors to the BFS queue (avoid going back to parent)
        for e in Edge[nowN]:
            if e != preN:
                q.append((e, nowN))

    # Output the result: the sum and the assigned color list
    print(ans)
    print(" ".join(map(str, Color)))

    return 0

if __name__ == "__main__":
    solve()