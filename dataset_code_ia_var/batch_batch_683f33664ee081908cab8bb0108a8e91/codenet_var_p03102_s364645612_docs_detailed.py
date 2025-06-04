def count_positive_sums():
    """
    This function reads from the standard input the following parameters:
        - N: The number of test cases (integer)
        - M: The number of integers in each test case (integer)
        - C: An additional integer to add to each sum (integer)
        - B: A list of M integers to be used as multipliers
        - For each test case, reads a list A of M integers
    
    For each test case, it computes the dot product of A and B, adds C,
    and counts the number of times this sum is greater than zero.

    The final count is printed to the standard output.
    """
    # Read the integers N, M, C from the first input line.
    N, M, C = map(int, input().split())

    # Read the list of multipliers B from the second input line.
    B = list(map(int, input().split()))

    # Initialize a counter to keep track of how many test cases satisfy the condition.
    counter = 0

    # Iterate through each of the N test cases.
    for i in range(N):
        # Read the array A of size M for the current test case.
        A = list(map(int, input().split()))

        # Compute the element-wise product of corresponding elements in A and B.
        mul = [a * b for a, b in zip(A, B)]

        # Append the additional integer C to the list of products.
        mul.append(C)

        # Compute the sum of all elements in mul (dot product + C).
        total = sum(mul)

        # If the sum is strictly greater than zero, increment the counter.
        if total > 0:
            counter += 1

    # After processing all test cases, print the final count.
    print(counter)

# Call the function to execute the described process.
count_positive_sums()