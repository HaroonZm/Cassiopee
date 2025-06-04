from collections import deque  # Import the deque class from the collections module; this allows us to efficiently add and remove elements from both ends of the queue

def Topologicalsort(v):
    # This function performs the topological sort on the graph
    # 'v' is the total number of vertices in the graph
    start = deque()  # Create an empty deque, which will be used as a queue to store vertices with 0 incoming edges (indegree)
    for i in xrange(v):  # Loop over all vertices numbered from 0 to v-1 (xrange is an efficient iterator)
        if indeg[i] == 0:  # If vertex 'i' does not have any incoming edges
            start.append(i)  # Add such a vertex to the queue for processing; these will be potential starting points for topological order

    if len(start) > 1:
        flag = True  # If there is more than one node that can be chosen at the beginning, flag indicates non-uniqueness in topological ordering
    else:
        flag = False  # Otherwise, the order may be unique

    while len(start) > 0:  # Continue the process until all nodes with indegree 0 are processed
        i = start.popleft()  # Remove and return the vertex at the left end of the deque (the next node to add to the ordering)
        ans.append(i)  # Add this node to the solution list which stores the topological order

        tmp = []  # Temporary list to store any new vertices with indegree 0 found in this iteration

        for j in g[i]:  # For every neighbor 'j' of the currently processed node 'i'
            indeg[j] -= 1  # Decrease its indegree by 1, since the edge from 'i' to 'j' is removed in our virtual traversal
            if indeg[j] == 0:  # If, after removal, the neighbor now has no incoming edges
                tmp.append(j)  # Record in temporary list
                start.append(j)  # Add the neighbor to the queue, as it is ready to be processed in the ordering
                if len(tmp) > 1:  # If more than one node becomes zero-indegree at the same time, again the order is not unique
                    flag = True  # Set the uniqueness flag to True to indicate ambiguity

    return ans, flag  # Return two results: the computed topological order and the flag about uniqueness

def solve(n, m):
    # This function reads m dependencies and builds the graph and indegree list
    # 'n' is the total number of vertices, 'm' is the number of edges
    for i in xrange(m):  # Loop exactly m times, once for each dependency to be read
        wt, lt = map(int, raw_input().split())  # Read two integers (wt and lt) from input; this represents an edge from wt to lt
        wt -= 1  # Decrement by 1 to convert user input (possibly 1-based indexing) to Python's 0-based index
        lt -= 1
        g[wt].append(lt)  # Append lt to the adjacency list of wt, indicating a directed edge from wt to lt
        indeg[lt] += 1  # Increment the indegree count for lt, as it has one more incoming edge now

    ans, flag = Topologicalsort(n)  # Run topological sort algorithm using the constructed graph
    return ans, flag  # Return the results from the sorting function

n = int(raw_input())  # Read the number of vertices (nodes) from input and convert to integer
m = int(raw_input())  # Read the number of edges (relations) from input

indeg = [0] * n  # Initialize a list of size n with all zeros to keep track of each vertex's indegree
g = [[] for _ in xrange(n)]  # Create a list of n empty lists; each inner list will store the outgoing edges of that node

ans = []  # Initialize an empty list to store the result of the topological sort

ans, flag = solve(n, m)  # Call 'solve' to process the input and compute (ans: ordering, flag: uniqueness)

if flag:
    # If there was ever ambiguity in choosing the next node (more than one zero-indegree at any moment)
    for i in xrange(n):  # Output the sorted nodes
        print(ans[i] + 1)  # Convert back from 0-based to 1-based indexing for output, as per usual competitive programming standards
    print(1)  # Output 1 to indicate the ordering is not unique (ambiguous)
else:
    # If the computation found a unique ordering
    for i in xrange(n):  # Output the sorted nodes
        print(ans[i] + 1)  # Again, switch to 1-based indexing for output
    print(0)  # Output 0 to indicate the ordering is unique (no ambiguity found)