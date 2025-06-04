def extended_euclidean():
    """
    Calculate the coefficients (x, y) such that ax + by = gcd(a, b), 
    using the extended Euclidean algorithm.

    Input:
        The function expects a single line of input with two integers a and b separated by a space.

    Output:
        Prints the coefficients x and y, separated by a space.
    """

    # Read a line of input and split it into two parts
    L = input().split()

    # Initialize 'a' as a list with:
    #   - a[0]: the current remainder in the Euclidean algorithm (initialized to the first input)
    #   - a[1]: the current coefficient for 'a' in the linear combination (starts at 1)
    #   - a[2]: the current coefficient for 'b' in the linear combination (starts at 0)
    a = [int(L[0]), 1, 0]

    # Initialize 'b' as a list with:
    #   - b[0]: the second input (the divisor in the Euclidean algorithm)
    #   - b[1]: coefficient for 'a' for this row in the algorithm (starts at 0)
    #   - b[2]: coefficient for 'b' for this row in the algorithm (starts at 1)
    b = [int(L[1]), 0, 1]

    # Perform the main loop of the extended Euclidean algorithm
    # Continue while the remainder of a divided by b is not zero
    while a[0] % b[0] != 0:
        # Find the integer quotient of the current division
        k = a[0] // b[0]

        # Save current 'b' values to use in swapping after updates
        c = b[0]
        c1 = b[1]
        c2 = b[2]

        # Update the coefficients for 'a' and 'b'
        # These correspond to the representation of the current remainder as a linear combination
        a[1] -= (k * b[1])
        a[2] -= (k * b[2])

        # Update 'b' for the next iteration: new remainder and new coefficients
        b[0] = a[0] % b[0]
        b[1] = a[1]
        b[2] = a[2]

        # Prepare 'a' for the next iteration by swapping in the previous 'b' values
        a[0] = c
        a[1] = c1
        a[2] = c2

        # (Debug print could go here, but is omitted in functional code)

    # One more iteration after the main loop to finalize the calculation
    k = a[0] // b[0]
    c = b[0]
    c1 = b[1]
    c2 = b[2]
    a[1] -= (k * b[1])
    a[2] -= (k * b[2])
    b[0] = a[0] % b[0]
    b[1] = a[1]
    b[2] = a[2]
    a[0] = c
    a[1] = c1
    a[2] = c2

    # Output the coefficients: these are the solutions (x, y) where ax + by = gcd(a, b)
    print(a[1], a[2])

# Call the function to execute the algorithm
extended_euclidean()