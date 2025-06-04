import sys

def set_recursion():
    """
    Sets a very high recursion limit to avoid RecursionError in recursive algorithms.
    """
    sys.setrecursionlimit(2000000000)

def custom_input():
    """
    Custom input function that reads a line from stdin and strips the newline character.
    
    Returns:
        str: The user input as a string with trailing newlines removed.
    """
    return sys.stdin.readline().rstrip('\n')


def main():
    """
    Main function to process input data, compute prefix sums,
    and determine the maximum value according to the problem's logic.

    The code works as follows:
    1. Reads the total number of entries `n`.
    2. Reads `n` pairs of integers and sorts them based on the first value.
    3. Computes prefix sums of the second values.
    4. Iterates to determine the maximum value of s[i] - data[i][0] - minimal prefix difference.
    5. Outputs the result.
    """
    set_recursion()

    # Read the number of data points
    n = int(custom_input())

    # Initialize the list to store input tuples
    data = []
    
    # List to store prefix sums, initial value 0
    s = [0]

    # Read each data point and add to 'data' list
    for i in range(n):
        # Read a line and convert it into a tuple of integers
        data.append(tuple(map(int, custom_input().split())))

    # Add a dummy tuple at the beginning and sort the data
    # This ensures 1-based indexing after sorting
    data = [(0, 0)] + sorted(data)

    # Compute prefix sums for the second elements
    for i in range(n):
        # Add the next value to the running total
        s.append(s[-1] + data[i+1][1])

    # Initialize variables for tracking the result
    ans = 0          # Stores the maximum answer found
    mn = 10 ** 18    # Holds the minimum value of (prefix sum - first value) seen so far

    # Iterate through each sorted data entry (1-based)
    for i in range(1, n+1):
        # Update 'mn' with the minimal value up to index i-1
        if mn > s[i-1] - data[i][0]:
            mn = s[i-1] - data[i][0]
        # Update 'ans' with the maximum possible value at position i
        if ans < s[i] - data[i][0] - mn:
            ans = s[i] - data[i][0] - mn

    # Output the final computed answer
    print(ans)

if __name__ == '__main__':
    main()