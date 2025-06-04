def process_stack_operations():
    """
    Reads the number of stacks and operations, then processes each stack operation.

    The function performs the following supported operations:
    - Push (append) a value to a specific stack.
    - Print the top value of a specified stack (if non-empty).
    - Pop the top value from a specific stack (if non-empty).

    The input is read from standard input in this format:
    - First line: two integers n (number of stacks), q (number of operations)
    - Next q lines: each line describes an operation:
        - "0 stack_index value": Push 'value' onto stack 'stack_index'.
        - "1 stack_index": Print the value at the top of stack 'stack_index' if not empty.
        - "2 stack_index": Pop the top value from stack 'stack_index' if not empty.
    """
    # Read the number of stacks (n) and the number of queries (q)
    n, q = list(map(int, input().split(' ')))
    
    # Initialize a list of empty lists, representing the stacks
    stacks = [[] for _ in range(n)]
    
    # Iterate over each operation
    for _ in range(q):
        # Read the current operation as a list of integers
        op = list(map(int, input().split(' ')))
        
        # If operation code is 0, push the given value onto the specified stack
        if op[0] == 0:
            # op[1]: stack index, op[2]: value to append
            stacks[op[1]].append(op[2])
            
        # If operation code is 1, print the top value of the specified stack (if not empty)
        elif op[0] == 1:
            # Check if the stack is not empty before printing
            if len(stacks[op[1]]) != 0:
                print(stacks[op[1]][-1])
        
        # If operation code is 2, pop the top value of the specified stack (if not empty)
        elif op[0] == 2:
            # Check if the stack is not empty before popping
            if len(stacks[op[1]]) != 0:
                stacks[op[1]].pop()

# Start processing stack operations when the script is executed
process_stack_operations()