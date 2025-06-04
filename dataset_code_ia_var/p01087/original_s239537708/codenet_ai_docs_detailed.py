def process_expressions():
    """
    Main function to process multiple expressions entered by the user.
    Reads integer 'n' for the number of expressions, or terminates if 'n' is 0.
    For each expression, collects lines, processes them in reverse using a custom evaluation logic,
    and prints the result for each test case.
    """
    while True:
        # Read number of input lines for current case
        n = int(input())
        if n == 0:
            # Exit the loop if the input is 0
            break

        # Read 'n' lines and store them in a list
        w = [input() for _ in range(n)]
        # Reverse the list to process from the last expression upwards
        w = reversed(w)

        # Initialize a list to store elements at each depth/level
        eles = [[] for _ in range(9)]

        # Iterate through each expression line
        for item in w:
            # Determine the depth based on the position of the character
            d = len(item) - 1
            # Last character indicates the operation or value
            c = item[-1]

            if c == "+":
                # Sum all elements in the next depth and append result to current depth
                eles[d].append(sum(eles[d+1]))
                # Clear next deeper list after operation
                eles[d+1] = []
            elif c == "*":
                # Multiply all elements in the next depth, append result to current
                tmp = 1
                for i in eles[d+1]:
                    tmp *= i
                eles[d].append(tmp)
                # Clear next deeper list after operation
                eles[d+1] = []
            else:
                # If the character is a digit, convert and append to current depth list
                eles[d].append(int(c))

        # Output the final computed result from the deepest level
        print(eles[0][0])

# Call the processing function to begin the program
process_expressions()