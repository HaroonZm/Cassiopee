def calculate_max_sum_with_sign_adjustment():
    """
    Reads the size and elements of an integer list from standard input, then calculates the maximum possible
    sum of absolute values of the elements. If any number is zero or the count of negative numbers is even,
    the absolute sum is the answer. If the count of negative numbers is odd and there is no zero in the 
    list, the sum is reduced by twice the smallest absolute value.

    This adjustment handles the case where signs can be flipped to maximize the sum, optimally flipping the
    sign of the smallest absolute value in case of an odd count of negatives and absence of zeros.

    No parameters or return. Result is printed directly.
    """
    # Read the number of elements in the list
    n = int(input())
    # Read the list of integers
    a = list(map(int, input().split()))
    
    # Initialize the accumulator for the absolute sum
    ans = 0
    # Counter for the number of negative numbers
    c = 0
    # Track the smallest absolute value in the list
    tmp_m = 10**9
    # Flag to mark if zero exists in the list
    zero = False

    # Iterate through each element to gather necessary information
    for i in range(n):
        # If the number is negative, increment the counter
        if a[i] < 0:
            c += 1
        # If the number is zero, turn on the zero flag
        elif a[i] == 0:
            zero = True
        # Take the absolute value of the current element
        tmp = abs(a[i])
        # Add the absolute value to the running total
        ans += tmp
        # Update the minimum absolute value found so far
        tmp_m = min(tmp_m, tmp)
    
    # If there's any zero in the list, the total sum is already maximal
    if zero:
        print(ans)
    else:
        # If the count of negative numbers is even, the total sum is already maximal
        if c % 2 == 0:
            print(ans)
        else:
            # If the count of negative numbers is odd, subtract twice the smallest absolute value
            # to flip its sign and maximize the sum
            print(ans - tmp_m * 2)

# Call the function to execute the logic
calculate_max_sum_with_sign_adjustment()