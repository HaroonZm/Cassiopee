def checkback(B, i, j):
    """
    Check and possibly flip the bit at position (i, j) in matrix B, based on its neighbors.

    The function counts how many of the three neighbors (left, right, and above) have the same value
    as B[i][j]. If exactly two neighbors are equal (i.e., samesum == 2), the bit is flipped (0 becomes 1, and vice versa).
    Otherwise, the bit remains unchanged.

    Args:
        B (list of lists): The 2D matrix containing bits or values.
        i (int): Row index in matrix B.
        j (int): Column index in matrix B.

    Returns:
        int: The potentially modified value of B[i][j] (either 0 or 1).
    """
    # Count the number of neighbors (left, right, upper) equal to B[i][j]
    samesum = (
        (B[i][j] == B[i][j - 1]) +
        (B[i][j] == B[i][j + 1]) +
        (B[i][j] == B[i - 1][j])
    )
    # If exactly 2 neighbors are the same, flip the bit
    if samesum == 2:
        return not B[i][j]
    # Otherwise, return the original value
    else:
        return B[i][j]

while True:
    # Read two integers N and K from input
    N, K = map(int, raw_input().split())
    # When N is zero, terminate the loop
    if N == 0:
        break

    # If N is odd or K is too large to generate a valid configuration, print "No"
    if N % 2 or K > 2 ** (N // 2):
        print "No\n"
    else:
        # Split the matrix into pairs
        n = N // 2

        # Initialize the main array A representing the first row, filled with zeros
        A = [0 for _ in range(N)]

        # Adjust K to be zero-indexed, as we are generating the K-th configuration
        K -= 1

        # Fill the array A according to the binary representation of K
        for i in range(1, n + 1):
            # For each pair, set both elements to the corresponding bit of K
            A[2 * (i - 1)]     = K // 2 ** (n - i)
            A[2 * (i - 1) + 1] = K // 2 ** (n - i)
            # Update K to the remainder for the next iteration
            K %= 2 ** (n - i)

        # Initialize matrix B with borders of dummy values (-1)
        # The matrix is (N+2)x(N+2) to handle edge conditions easily
        B = [[-1 for _ in range(N + 2)] for _ in range(N + 2)]

        # Set the first row (excluding borders) to the generated configuration from A
        B[1][1:N + 1] = A[:]

        # Fill each subsequent row of the matrix using the checkback function
        for i in range(2, N + 1):
            for j in range(1, N + 1):
                # The value is determined by analyzing the row above
                B[i][j] = checkback(B, i - 1, j)

        # Output the matrix, translating 0 to '.' and 1 to 'E' for each cell
        for i in range(1, N + 1):
            row_str = ""
            for j in range(1, N + 1):
                row_str += ".E"[B[i][j]]
            print row_str
        print "\n"  # Separate outputs with a blank line