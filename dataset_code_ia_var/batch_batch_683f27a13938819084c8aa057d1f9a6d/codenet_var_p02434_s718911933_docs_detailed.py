def main():
    """
    Main function to process dynamic arrays based on user input. Supports three operations:
      - Append an element to a specific list
      - Print all elements of a specific list
      - Clear all elements from a specific list

    The function reads the number of lists and operations, then processes each operation accordingly.
    """

    # Read the number of lists (n) and the number of queries (q)
    n, q = map(int, input().split())

    # Initialize a list containing n empty sublists
    A = [[] for _ in range(n)]

    # Process each query
    for _ in range(q):
        # Read the operation input, padding with ' 1' in case of missing x argument
        # Then, split and take the first three items to safely unpack
        op, t, x = (input() + ' 1').split()[:3]

        if op == '0':
            # Operation 0: Append the element x to the sublist at index t
            # Arguments:
            #   t (str): index of the list to append to, convert to int
            #   x (str): element to append
            # Returns: None
            A[int(t)].append(x)
        elif op == '1':
            # Operation 1: Print all elements in the sublist at index t
            # Arguments:
            #   t (str): index of the list to print, convert to int
            # Returns: None (prints to standard output)
            print(*A[int(t)])
        else:
            # Operation 2 (or other): Clear all elements in the sublist at index t
            # Arguments:
            #   t (str): index of the list to clear, convert to int
            # Returns: None
            A[int(t)] = []

if __name__ == "__main__":
    main()