def solve():
    # Import the stdin object from the sys module to read input efficiently from standard input.
    from sys import stdin
    f_i = stdin  # Alias 'f_i' is created to simplify references to stdin.

    # Importing two functions from the heapq module to enable efficient min-heap operations:
    # - heappush: to insert a tuple into the heap while maintaining heap order.
    # - heappop: to remove and return the smallest tuple from the heap.
    from heapq import heappush, heappop

    # Start an infinite loop that only breaks when stopped explicitly.
    while True:
        # Read a line from standard input, split it into individual strings, convert those to integers,
        # and unpack them into 'n' (number of nodes) and 'm' (number of edges).
        n, m = map(int, f_i.readline().split())
        # If the number of nodes 'n' is 0, this signals termination of input; exit loop.
        if n == 0:
            break
        
        # Build an adjacency list representing the graph.
        # Create a list with 'n' empty sublists: one sublist for each node.
        adj = [[] for i in range(n)]
        # For each edge to be read:
        for i in range(m):
            # Read a line, split and convert input to integers representing:
            # 'a': start node of the edge
            # 'b': end node of the edge
            # 'c': associated cost/fare for traversing the edge
            a, b, c = map(int, f_i.readline().split())
            # Decrement 'a' and 'b' by 1 to convert 1-based input to 0-based indices (Python convention).
            a -= 1
            b -= 1
            # For undirected graphs, add the edge both ways: (b,c) to adj[a], and (a,c) to adj[b].
            adj[a].append((b, c))
            adj[b].append((a, c))
        
        # Implementing Dijkstra's shortest path algorithm with modifications for ticket usage.
        # Prepare a 2D list 'fare' of size n x 3:
        # - fare[u][t] will store the minimum total fare to reach node 'u'
        #   with 't' as the remaining ticket state (2 = unused, 1 = just used, 0 = already used)
        # Initialize all fares to a large constant value (100000 acts as 'infinity').
        fare = [[100000] * 3 for i in range(n)]
        # Set the fare to reach start node (node 0) with 2 tickets left (i.e., not used yet) as 0.
        fare[0][2] = 0

        # Create a min-heap priority queue to process states efficiently.
        # Each heap entry is a tuple:
        #   (current total fare, current node index, remaining ticket state)
        # Start from node 0, with fare 0, and 2 tickets available.
        hq = [(0, 0, 2)]

        # The target node is the last node, which is (n-1) due to 0-based indexing.
        # Temporarily store n-1 in 'n' for use in this block (careful: shadows node count).
        n -= 1

        # Repeat as long as the heap is not empty.
        while hq:
            # Pop the tuple with the minimal current fare from the heap.
            # f1: total fare so far; u: current node; rt: remaining ticket state
            f1, u, rt = heappop(hq)
            
            # Goal check:
            # - Only print the answer if not immediately after using a ticket (rt != 1)
            # - And if the current node is the destination node (n).
            if rt != 1 and u == n:
                # Print the minimum fare found to reach the target with proper ticket usage.
                print(f1)
                # Solution is reached for this test case; proceed to next by breaking out of the loop.
                break
            
            # Explore all neighboring nodes 'v' accessible from current node 'u',
            # with 'f2' as the extra fare for traveling to 'v' via this edge.
            for v, f2 in adj[u]:
                # If no tickets remain (rt == 0), must pay full fare along this edge.
                if rt == 0:
                    f3 = f1 + f2  # Add edge fare to total fare.
                    # If this is a cheaper way to reach 'v' with 0 tickets left, update records.
                    if f3 < fare[v][0]:
                        fare[v][0] = f3
                        # Add new state to heap for further exploration.
                        heappush(hq, (f3, v, 0))
                # If we've just used a ticket in the previous step (rt == 1),
                # the move to 'v' is 'free', but after that, we have 0 tickets left.
                elif rt == 1:
                    # Total fare remains the same as prior to this move (since ticket was used to pay).
                    if f1 < fare[v][0]:
                        fare[v][0] = f1
                        heappush(hq, (f1, v, 0))
                else:
                    # Have not yet used ticket (rt == 2): two options to proceed.

                    # Option 1: Do not use ticket.
                    # - Pay full fare as normal, remain in the unused tickets state (2).
                    f3 = f1 + f2
                    if f3 < fare[v][2]:
                        fare[v][2] = f3
                        heappush(hq, (f3, v, 2))
                    
                    # Option 2: Use the ticket on this edge.
                    # - Do not pay for this fare (edge is free),
                    # - State updates to '1' (just used ticket, next step will be mandatory rt==1).
                    if f1 < fare[v][1]:
                        fare[v][1] = f1
                        heappush(hq, (f1, v, 1))

# Without adding any extra output or guard, immediately call solve to run this code if file is run.
solve()