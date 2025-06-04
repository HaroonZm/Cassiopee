def read_matrix(n):
    """
    Reads a matrix of size n x 2 from user input.

    Parameters:
    n (int): The number of rows in the matrix.

    Returns:
    list: A list of lists (matrix) where each sublist contains two integers.
    """
    matrix = []
    for _ in range(n):
        # Read a line of input, split it into integers, and append as a row
        row = [int(i) for i in input().split()]
        matrix.append(row)
    return matrix

def count_valid_pairs(A, C):
    """
    Counts the maximum number of valid (A, C) pairs based on matching conditions.

    Each pair (a, b) from list A can be paired with (c, d) from list C if:
      - a < c
      - b < d
      - Element from A has not been paired yet

    Once a pair from A is used, it cannot be reused.

    The list A is sorted in descending order by its second element.
    The list C is sorted in ascending order (first element, then second).

    Parameters:
    A (list): List of [a, b] pairs, representing the first set.
    C (list): List of [c, d] pairs, representing the second set.

    Returns:
    int: The maximum number of valid pairs.
    """
    n = len(A)
    ans = 0  # Stores the count of valid pairs found
    used = [False] * n  # Tracks which elements in A have been matched

    # Sort A by second element in descending order for greedy matching
    A.sort(key=lambda x: x[1], reverse=True)
    # Sort C in natural ascending order (first by first, then by second element)
    C.sort()

    for c, d in C:
        i = 0
        # For each (c, d) in C, find the first unused element in A
        # where both elements are strictly less than c and d respectively
        while i < n and (used[i] or A[i][0] >= c or A[i][1] >= d):
            i += 1
        if i >= n:
            # No available element from A for this (c, d)
            continue
        # Valid match found
        ans += 1
        used[i] = True  # Mark as used
    return ans

def main():
    """
    Main function that orchestrates reading inputs, processing data,
    and printing the result.
    """
    n = int(input())  # Number of pairs in each list

    # Read in the two lists of pairs as matrices
    A = read_matrix(n)
    C = read_matrix(n)

    # Find the maximal number of valid pairs according to the matching rules
    result = count_valid_pairs(A, C)

    # Output the result
    print(result)

if __name__ == '__main__':
    main()