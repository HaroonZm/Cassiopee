from collections import deque  # Import the deque class from the collections module for queue efficiency

while 1:  # Infinite loop, will continue until we break (exit condition inside)
    # Read four integers from input: n (number of nodes), a (number of edges/arcs), s (start node), g (goal node)
    n, a, s, g = map(int, raw_input().split())  # Use map to cast all elements of the input to int
    if n == a == s == g == 0:  # Input of four zeros is the termination signal
        break  # Exit the infinite loop if all input are zero

    # G is a list of n empty lists, one for each node: G[v] will store outgoing edges from v as (to, label)
    G = [[] for i in xrange(n)]
    # H is a list of n empty lists: H[v] will store incoming nodes u (with an edge u->v)
    H = [[] for i in xrange(n)]

    # Loop to read 'a' edges/arcs
    for i in xrange(a):
        # Read one edge from input: two integers (nodes x and y), and a string label
        x, y, lab = raw_input().split()
        x = int(x)  # Convert x (start node of this edge) to int
        y = int(y)  # Convert y (end node of this edge) to int
        G[y].append((x, lab))  # For node y, add (x, lab) as an incoming (reverse) edge with its label
        H[x].append(y)  # For node x, add y as an outgoing destination

    # Create 'can' list to track which nodes are reachable from s, initialized to 0 (not reachable)
    can = [0]*n  # Set all n elements to zero (False)
    deq = deque()  # Use deque for efficient popping from left (as a queue)
    can[s] = 1  # Mark the start node 's' as reachable from itself
    deq.append(s)  # Initialize queue with the start node

    # Breadth-First Search (BFS) to find all nodes reachable from s
    while deq:  # While the queue is not empty
        v = deq.popleft()  # Remove and get the node at the left/front of the queue
        # For every node t that is an outgoing destination from v
        for t in H[v]:
            if not can[t]:  # If 't' has not been visited yet
                can[t] = 1  # Mark 't' as reachable
                deq.append(t)  # Add 't' to the queue for further exploration

    # 'state' keeps the shortest lexicographical string found for each node (None means not yet visited)
    state = [None]*n  # Initially, all are None
    state[g] = ""  # For the goal node, the initiation string is the empty string, as it is our target

    step = 0          # Number of consecutive steps state[s] hasn't changed
    prev_s = None     # Previous best-known value at state[s]
    LIM = 5*n+1       # Arbitrary iteration limit (based on problem constraints)
    ok = 0            # Will be set to 1 if we see no improvement for LIM consecutive steps

    # Attempt for up to 2*LIM iterations (arbitrary upper bound to avoid infinite loops)
    for c in xrange(LIM*2):
        update = 0  # Becomes 1 if we make an improvement to any state
        # Iterate through all nodes
        for v in xrange(n):
            # Skip nodes that are not solved yet (state[v] is None) or not reachable from s
            if state[v] is None or not can[v]:
                continue
            # For all incoming edges to v (from t, with label l)
            for t, l in G[v]:
                # If t is not solved, or we can form a better/shorter string for t by prepending l to state[v]
                if state[t] is None or l + state[v] < state[t]:
                    state[t] = l + state[v]  # Update state's value for t
                    update = 1  # Mark that we made at least one update
        # Check if state[s] didn't change this round compared to last time
        if prev_s == state[s]:
            step += 1  # Increment counter if no change in state[s]
        else:
            prev_s = state[s]  # Update the last-seen value of state[s]
            step = 0  # Reset counter because state[s] has changed
        # If we saw no improvement to state[s] for LIM consecutive steps, convergence
        if step == LIM:
            ok = 1  # Mark as converged
            break  # Exit the for-loop early

    # If state[s] is still None (not solved), or we didn't reach convergence (ok==0)
    if state[s] is None or not ok:
        print "NO"  # Print NO as the answer
    else:
        print state[s]  # Print the lex shortest string collected from s to g