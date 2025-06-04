def calculate_remaining_types():
    """
    Reads an integer N and a list of N integers from input.
    Sorts the list and computes how many 'types' (kind) remain based on the following rule:
    For each element a in the sorted list, if double the accumulated sum (c) is less than a,
    updates the value of kind to N - i (where i is the index in the sorted list).
    At the end, prints the value of kind.

    Returns:
        None
    """

    # Read the number of elements from standard input
    N = int(input())
    # Read the list of N integers and convert them into a list
    A = list(map(int, input().split()))
    # Sort the list to process elements in increasing order
    A.sort()

    # Initialize the cumulative sum and the kind counter
    c = 0         # Accumulate the sum of elements processed so far
    kind = N      # Initially, all elements are considered

    # Iterate through the sorted list with both index and value
    for i, a in enumerate(A):
        # If double the current sum is less than the current value,
        # update kind to represent the remaining elements from this point
        if c * 2 < a:
            kind = N - i
        # Add the current value to the cumulative sum
        c += a

    # Print the final value of kind, which is the answer
    print(kind)

# Call the function to execute the logic
calculate_remaining_types()