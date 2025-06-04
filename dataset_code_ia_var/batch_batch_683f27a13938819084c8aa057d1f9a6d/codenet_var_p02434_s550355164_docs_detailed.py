from collections import deque

def process_queue_operations():
    """
    Reads inputs to perform a series of operations on an array of deques.
    The number of deques and the number of queries are read from input.
    For each query, one of three operations is performed:
      - Append an element to a target deque.
      - Print all elements of a target deque as a space-separated string.
      - Clear all elements from a target deque.
    The input and all print outputs are managed via standard I/O.
    """
    # Read the initial input line and extract the number of deques (n) and number of queries (q)
    n, q = map(int, input().split())

    # Initialize a list to hold n deques
    Q = []
    for i in range(n):
        Q.append(deque())

    # Process q queries/operations
    for i in range(q):
        # Read the operation parameters as a list of strings
        a = input().split()
        # The second value in the operation specifies the target deque index
        t = int(a[1])

        if a[0] == "0":
            # Operation type "0": Append a new element to deque Q[t]
            # a[2] contains the value to append
            Q[t].append(a[2])
        elif a[0] == "1":
            # Operation type "1": Print all elements in deque Q[t], space-separated
            print(*Q[t])
        else:
            # Operation type "2": Clear all elements from deque Q[t]
            Q[t].clear()

# Execute the queue operations processing function
process_queue_operations()