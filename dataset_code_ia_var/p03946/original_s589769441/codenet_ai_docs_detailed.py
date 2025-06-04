def count_max_difference_occurrences():
    """
    Reads input values, computes the maximum difference between an element and 
    the minimum of previous elements in the list, and counts how many times 
    this maximum difference occurs.

    The function expects input in the following format via stdin:
    - The first line contains two integers: n (length of list) and t (unused).
    - The second line contains n integers, representing the list.

    Prints:
        The number of occurrences of the maximum found difference.
    """
    # Read the input and parse n and t (t is unused, possibly a placeholder)
    n, t = map(int, input().split())

    # Read the list of n integers
    a = list(map(int, input().split()))

    # Initialize min_a to the first element (minimum value up to the previous element)
    min_a = a[0]

    # Initialize min_b to 0 (the maximum difference found so far)
    min_b = 0

    # Initialize count for occurrences of min_b
    cnt = 0

    # Iterate through the array starting from the second element
    for i in range(1, n):
        # Update min_a to be the minimum value encountered up to a[i-1]
        min_a = min(min_a, a[i-1])

        # Calculate the difference between current value and min_a
        diff = a[i] - min_a

        # If a new maximum difference is found, update min_b and reset count
        if min_b < diff:
            min_b = diff
            cnt = 1
        # If the same maximum difference is found, increment the count
        elif min_b == diff:
            cnt += 1

    # Print the number of occurrences of the maximum difference
    print(cnt)

# Function call to execute the algorithm
count_max_difference_occurrences()