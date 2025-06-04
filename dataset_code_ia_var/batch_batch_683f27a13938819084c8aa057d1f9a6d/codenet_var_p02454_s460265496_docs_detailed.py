import bisect

def main():
    """
    Main function to interactively process queries for the lower and upper bounds of values in a sorted list.

    This function does the following:
    1. Reads an integer n representing the size of the list.
    2. Reads n integers and forms a list A. The list must be sorted for correct bisect behavior.
    3. Reads an integer q representing the number of queries.
    4. For each query:
        - Reads an integer value 'b'.
        - Finds the leftmost insertion point (lower bound) for 'b' in A.
        - Finds the rightmost insertion point (upper bound) for 'b' in A.
        - Prints the lower and upper bounds.
    """
    # Read the number of elements in the list
    n = int(input())
    # Read the list of integers and store in A. Assumes input is sorted.
    A = list(map(int, input().split()))
    # Read the number of queries to process
    q = int(input())
    # Process each query
    for _ in range(q):
        # Read the query value
        b = int(input())
        # Find the insertion position for b from the left (lower bound)
        lb = bisect.bisect_left(A, b)
        # Find the insertion position for b from the right (upper bound)
        ub = bisect.bisect_right(A, b)
        # Output the lower and upper bounds
        print(lb, ub)

if __name__ == '__main__':
    main()