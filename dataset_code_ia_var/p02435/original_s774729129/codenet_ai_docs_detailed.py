def process_stack_operations():
    """
    Reads input parameters and performs a series of stack operations on multiple stacks.

    The function expects the following input from the user:
    - The first line contains two integers separated by a space:
        n: the number of stacks to be managed.
        r: the number of operations to perform.
    - The next r lines each describe an operation as a list of integers.
        Operations are defined as follows:
        - If the first integer (c) is 0: push the third integer onto stack i.
        - If c is 1: print the top element of stack i (if not empty).
        - If c is 2: pop the top element of stack i (if not empty).

    The function manages the stacks and performs each operation accordingly.
    """
    # Read the number of stacks (n) and the number of operations (r) from input
    n, r = input().split(' ')
    n = int(n)
    r = int(r)

    # Initialize a list of n empty lists to represent stacks
    stack = [[] for _ in range(n)]

    # Process each operation
    for _ in range(r):
        # Read and parse the operation parameters for the current operation
        row = list(map(int, input().split(' ')))
        c = row[0]  # Operation code: 0 (push), 1 (top), 2 (pop)
        i = row[1]  # Stack index to operate on

        # If the operation is push (c == 0), push the element row[2] onto stack[i]
        if c == 0:
            stack[i].append(row[2])

        # If the stack[i] is non-empty, proceed with other operations
        if stack[i]:
            # If the operation is top (c == 1), print the top element of stack[i]
            if c == 1:
                print(stack[i][-1])
            # If the operation is pop (c == 2), remove the top element from stack[i]
            if c == 2:
                stack[i].pop()

# Call the function to run the stack operations processor
process_stack_operations()