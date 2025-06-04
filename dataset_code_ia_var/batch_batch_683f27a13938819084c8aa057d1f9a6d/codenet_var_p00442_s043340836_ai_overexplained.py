# AOJ 0519: Worst Reporter
# Python3, excessively commented for educational clarity

# This function performs a topological sort on a directed graph.
# V: the total number of nodes (vertices) in the graph.
# to: the adjacency list, where to[i] is a list of all nodes that node i points to.
def topological_sort(V, to):
    # Create a list to count the in-degree (number of incoming edges) of each node.
    # Initialize in-degree of all nodes to zero.
    cnt = [0] * V
    
    # Compute the in-degree for each node.
    # For each node 'i', iterate through all nodes 'j' it points to.
    # Increment the in-degree count for node 'j'.
    for i in range(V):
        for j in to[i]:
            cnt[j] += 1

    # Create a list Q, which will be used as a queue for nodes ready to be processed.
    # Initially, Q is an empty list.
    Q = []

    # Find all nodes with in-degree zero.
    # These nodes have no dependencies and can be processed first.
    for i in range(V):
        if cnt[i] == 0:
            Q.append(i)

    # Initialize a variable f to zero.
    # This variable will be used as a flag to detect if at any time there are multiple nodes available to process (i.e., len(Q) > 1).
    # This relates to uniqueness of the topological order.
    f = 0

    # Process nodes in queue Q until it is empty.
    while len(Q) > 0:
        # Check if there are multiple candidates for processing.
        # If so, set f to True (by bitwise OR with f and the result of the condition).
        f |= len(Q) > 1

        # Select the node at the front of the queue.
        # In Python, Q[0] refers to the first element of the list.
        i = Q[0]

        # Remove the first node from the queue.
        # del Q[0] deletes the element at index 0.
        del Q[0]

        # Output the (1-based) index of the node being processed.
        # print() outputs the specified value to the console.
        # i is zero-based in Python, so add 1 for 1-based output.
        print(i + 1)

        # For each node 'k' that the current node 'i' points to (i.e., for neighbors of 'i'):
        for k in to[i]:
            # Decrease the in-degree count for node 'k' by 1.
            cnt[k] -= 1

            # If node 'k' now has in-degree zero, it can be processed next, so add it to the queue.
            if cnt[k] == 0:
                Q.append(k)

    # Return the flag 'f'.
    # If f is True (non-zero), there were multiple candidates to process at some step, meaning the topological order is not unique.
    # If f is False (zero), the order is unique.
    return f

# Read the number of nodes in the graph from user input.
# input() reads a line from standard input as a string.
# int() converts the string to an integer.
n = int(input())

# Initialize the adjacency list for the graph.
# to will be a list of empty lists, one for each node.
# [[] for i in range(n)] creates a list of 'n' empty lists.
to = [[] for i in range(n)]

# Read the number of edges in the graph from user input.
m = int(input())

# Process each edge in the input.
for i in range(m):
    # Read a line of input, split it into two values, and convert both to integers.
    # The input represents an edge from node 'a' to node 'b'.
    a, b = list(map(int, input().split()))

    # Add an edge from node a to node b to the adjacency list.
    # Subtract 1 from both 'a' and 'b' to convert from 1-based input to 0-based indices in Python.
    to[a - 1].append(b - 1)

# Call the topological_sort function with the number of nodes and the adjacency list.
# If the function returns True (non-zero), print 1, otherwise print 0.
# 1 indicates that the topological order is not unique; 0 indicates it is unique.
print(1 if topological_sort(n, to) else 0)