def main():
    """
    Main function to process a sequence of integers, analyze its trends (increases/decreases),
    and compute the length of the longest segment exhibiting a monotonic 'zigzag'
    (sequence of alternations between increases and decreases).
    The result is printed to standard output.
    """

    # Read the number of elements (unused in logic, provided per input format)
    _ = int(input())

    # Read the sequence of integers from input and convert them to a list
    A = list(map(int, input().split()))

    # Step 1: Remove consecutive duplicates to standardize the sequence for trend analysis.
    # Append an extra element (-1) to simplify pair iteration without index errors.
    A.append(-1)
    # Filter out consecutive duplicate elements by comparing each with its successor
    A = [a for a, b in zip(A, A[1:]) if a != b]

    # Step 2: Identify every element that is the "turning point" of a zigzag (peak or valley).
    # Insert -1 at the start and end for boundary handling during triple iteration.
    A.insert(0, -1)
    A.append(-1)
    # Keep only the middle element `b` of every triplet (a, b, c) where the trend changes:
    # - (a < b) != (b < c) is True only if the trend changes direction at b
    A = [b for a, b, c in zip(A, A[1:], A[2:]) if (a < b) != (b < c)]

    # Step 3: Prepare a structure for trend tracking and segment counting.
    # Append sentinel -1 to simplify next comparison.
    A.append(-1)
    # For each adjacent pair (a, b), generate (a, s), where:
    #   s = 1 if the trend here is increasing (a < b), else -1.
    # Sort the list by `a` for proper iteration in the next step.
    A = sorted((a, (1 if a < b else -1)) for a, b in zip(A, A[1:]))

    # Step 4: Iterate over the processed list to compute the maximal segment length.
    n = 1       # Current segment length counter.
    n_max = 0   # Store the maximum found segment length.
    prev = 0    # Track the previous value to check for strict increases.

    for a, s in A:
        if prev < a:
            # Start of a new segment, so update max if needed.
            if n_max < n:
                n_max = n
            prev = a
        n += s   # Update current segment length with the trend (+1 or -1).

    # Output the length of the longest zigzag segment.
    print(n_max)

# Run the main function when the script is executed
main()