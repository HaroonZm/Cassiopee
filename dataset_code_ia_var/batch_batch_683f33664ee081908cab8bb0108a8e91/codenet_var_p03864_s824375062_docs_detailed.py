def minimize_excess_sum(n, x, a):
    """
    Adjusts the given sequence 'a' so that for every consecutive pair (a[i], a[i+1]),
    their sum does not exceed x. The function computes the minimal total amount that 
    needs to be subtracted from the sequence to achieve this condition.
    
    Args:
        n (int): The number of elements in the sequence.
        x (int): The maximum allowed sum for any pair of consecutive elements.
        a (list of int): The input sequence of integers.
    
    Returns:
        int: The total amount subtracted from the sequence to satisfy the condition.
    """
    ans = 0  # Initialize the total amount to subtract to zero
    for i in range(n - 1):
        # Calculate how much the sum of a[i] and a[i+1] exceeds x
        excess = a[i] + a[i + 1] - x
        if excess > 0:
            # Add the excess to the total answer
            ans += excess
            # Reduce a[i+1] by the minimum of excess or a[i+1], ensuring non-negativity
            a[i + 1] -= min(excess, a[i + 1])
    return ans

def main():
    """
    Main function to read input, process the sequence, and print the result.
    
    Reads two integers (n and x) separated by space, followed by n integers.
    Then calls the minimize_excess_sum function and prints the answer.
    """
    # Read n and x from input
    n, x = map(int, raw_input().split())
    # Read the sequence a
    a = map(int, raw_input().split())
    # Compute and print the minimal amount to subtract
    print minimize_excess_sum(n, x, a)

# Entry point for the script
if __name__ == "__main__":
    main()