def minimize_sum_over_x(N, x, A):
    """
    Minimize the total excess of adjacent sums over a given threshold x in a sequence.

    Args:
        N (int): The number of elements in the array A (without the prepended zero).
        x (int): The maximum allowed sum for any pair of adjacent elements.
        A (list of int): List of integers (size N), representing the sequence.

    Returns:
        int: The minimal total amount subtracted from the sequence so that
             for every index i (from 1 to N), A[i-1] + A[i] <= x.
    """
    # Insert a zero at the beginning of the sequence to simplify accessing A[i-1] at i=0
    A = [0] + A
    ans = 0  # This variable will accumulate the total amount subtracted

    # Iterate through the sequence to check sums of adjacent elements
    for i in range(N):
        # Compute the sum of adjacent elements
        temp = A[i + 1] + A[i]
        # Calculate the amount to subtract so that the sum doesn't exceed x
        excess = max(temp - x, 0)
        # Accumulate the total amount subtracted
        ans += excess
        # Subtract the excess from the current element to satisfy the constraint for future pairs
        A[i + 1] -= excess

    return ans

if __name__ == "__main__":
    # Read input values for N and x
    N, x = map(int, input().split())
    # Read the sequence A of length N
    A = list(map(int, input().split()))
    # Compute and print the minimal total subtracted amount
    print(minimize_sum_over_x(N, x, A))