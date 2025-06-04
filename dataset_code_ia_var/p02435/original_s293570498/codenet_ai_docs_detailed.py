from collections import deque
import sys

# Use sys.stdin.readline for faster input reading
input = sys.stdin.readline

def loop_proc():
    """
    Handle multiple stacks and process queries.
    
    This function reads:
    - The number of stacks and queries.
    - A sequence of queries to manipulate and access the stacks.
    
    Supported queries:
    0 s x: Push value x onto stack s.
    1 s  : Print the top element of stack s if it's not empty.
    2 s  : Pop the top element from stack s if it's not empty.
    """
    # Read the first line: n1 -> number of stacks, n2 -> number of queries
    n1, n2 = map(int, input().split())
    
    # Initialize a list of deques, one for each stack
    wl = []
    for i in range(n1):
        wl.append(deque())
    
    # Process each query
    for i in range(n2):
        # Read the command as a list of integers
        l = list(map(int, input().split()))
        
        # If the command is to push: 0 stack_num value
        if l[0] == 0:
            # Append value x (l[2]) to stack s (l[1])
            wl[l[1]].append(l[2])
        
        # If the command is to print the top of stack: 1 stack_num
        elif l[0] == 1:
            # Check if the stack is not empty
            if len(wl[l[1]]) != 0:
                # Get the stack's reference
                tl = wl[l[1]]
                # Print the top element (i.e., the last in deque)
                print(tl[-1])
        
        # If the command is to pop from stack: 2 stack_num
        elif l[0] == 2:
            # Check if the stack is not empty
            if len(wl[l[1]]) != 0:
                # Remove the top element from the stack
                wl[l[1]].pop()

# Start the processing of queries
loop_proc()