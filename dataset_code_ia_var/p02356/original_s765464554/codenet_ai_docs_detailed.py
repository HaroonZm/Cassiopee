import sys
import os

def il():
    """
    Reads a line from standard input, splits it into tokens, converts each token to an integer,
    and returns the resulting list of integers.
    
    Returns:
        list of int: The integers read from stdin.
    """
    return list(map(int, sys.stdin.buffer.readline().split()))

def main():
    """
    Entry point of the program.
    Reads integer sequences and queries from input, then processes each query by
    finding the number of contiguous subarrays whose sum is less than or equal to the query value.
    The input can be redirected from a file if the 'LOCAL' environment variable is set.
    """
    # If running locally, redirect standard input to read from 'input.txt'
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    # Read the first line, expecting two integers: N (array size) and Q (number of queries)
    N, Q = il()
    # Read the next line, containing N integers for array A
    A = il()
    # Read the next line, containing Q integers representing the queries
    queries = il()

    # Process each query
    for q in queries:
        # Initialize the sum of the current window, result count, and the left pointer of the window
        current_sum = 0      # To store the sum of the current window
        result = 0           # To store the number of valid subarrays for this query
        left = 0             # Left pointer of the sliding window

        # Iterate over the array with the right pointer
        for right in range(N):
            # Add the current right element to the current sum
            current_sum += A[right]
            # If current sum exceeds the query value, move the left pointer to reduce the sum
            while current_sum > q and left <= right:
                current_sum -= A[left]
                left += 1
            # After adjusting left and right pointers, all subarrays ending at 'right'
            # and beginning from 'left' to 'right' satisfy the sum ≤ q
            result += right - left + 1

        # Output the number of valid subarrays for this query
        print(result)

if __name__ == '__main__':
    main()