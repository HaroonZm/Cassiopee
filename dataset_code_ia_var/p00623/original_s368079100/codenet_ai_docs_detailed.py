def calc():
    """
    Evaluate the expression tree stored in the global variable 'tree' and compute
    all possible bitwise results of assigning input values to the tree leaves and
    combining them according to the operators.

    This function uses recursion to process the binary expression tree consisting
    of bitwise operators: AND, OR, and XOR. At each internal node ('('), it recursively
    evaluates the left and right subtrees, then combines results for all possible
    4-bit values (0-15) using bitwise operations. At a leaf node (number), it
    initializes the result corresponding to the specific input value.

    Returns:
        list: A list of size 16, where each element counts how many assignments
              of values to the tree give that 4-bit result. The index 15 (0b1111)
              is the count of assignments resulting in all bits on.
    """
    global sz
    n = sz  # Unique buffer index for this node
    sz += 1
    # If current token is '(', it's an internal node (an operator)
    if tree[0] == '(':
        del tree[0]  # Remove the '(' token
        left = calc()  # Recursively evaluate the left subtree
        del tree[0]    # Remove the operator, always ')'
        right = calc() # Recursively evaluate the right subtree
        del tree[0]    # Remove the ')' token
        # Combine left and right subtree results using all bitwise operators
        for i in range(16):  # All possible 4-bit values from left
            for j in range(16):  # All possible 4-bit values from right
                k = left[i] * right[j]  # Number of ways to attain i and j
                if k:
                    # Bitwise AND
                    buf[n][i & j] += k
                    # Bitwise OR
                    buf[n][i | j] += k
                    # Bitwise XOR
                    buf[n][i ^ j] += k
    else:
        # Leaf node: assign this node's variable value from info
        buf[n][info[int(tree.pop(0)) - 1]] = 1
    return buf[n]

while True:
    # Read an expression tree as a list of characters
    tree = list(input())
    if tree[0] == 'E':
        break  # Sentinel: End of input
    # Initialize buffer for intermediate results and node count
    buf = [[0 for _ in range(16)] for _ in range(20)]  # 20 nodes, 16 possible values
    sz = 0  # Node index for buffer
    # Read in assignment information for each of the tree variables
    info = [0]*10  # Stores the 4-bit value for each variable
    for i in range(int(input())):
        # Read 4 bits (as 0 or 1) for current variable
        p = list(map(int, input().split()))
        for j in range(4):
            if p[j]:
                info[i] |= (1<<j)
    # Calculate the number of assignments that result in 0b1111 (all bits set)
    print(calc()[15])  # Output the count for bit value 15 (i.e. all four attributes set)