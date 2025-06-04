def process_queries():
    """
    Reads input, processes queries on an n x n grid as per specified rules, and prints the computed result.

    The function expects:
    - The first input line with two integers n (size of grid) and q (number of queries).
    - Each of the next q lines contains a query as two integers (type t and position x).
    
    Applies each query, updating internal state arrays describing 'blocked' rows and columns,
    and maintains a running total ('ans') of grid positions after queries are processed.

    Returns:
        None (Prints the final answer)
    """

    # Read the grid size 'n' and the number of queries 'q' from input.
    n, q = (int(x) for x in input().split())
    
    # Read all 'q' queries. Each query is a tuple (t, x) read from input.
    queries = [tuple(int(x) for x in input().split()) for _ in range(q)]

    # Initial answer: the number of valid inner cells in the (n-2) x (n-2) subgrid
    ans = (n - 2)**2
    
    # t1 and t2 arrays track, for each index, the minimal reached border for column/row blocks:
    # t1[i]: For column i, the minimal blocked row index.
    # t2[i]: For row i, the minimal blocked column index.
    t1 = [n] * (n + 1)
    t2 = [n] * (n + 1)

    # 'h' (height border) and 'w' (width border): 
    # track the current minimal unblocked row and column index, respectively.
    h, w = n, n

    # Process each query
    for t, x in queries:
        if t == 1:
            # Type 1 query: Block all cells in column x for rows >= 2 up to minimal h
            if x < w:
                # If the queried column index is less than current width border,
                # Update t1 for all affected columns and reduce w.
                tmp = h
                for i in range(x, w + 1):
                    t1[i] = h
                w = x
            else:
                # If already processed, just retrieve last block value for x.
                tmp = t1[x]
            # Subtract the number of affected rows (excluding edges).
            ans -= tmp - 2
        else:
            # Type 2 query: Block all cells in row x for columns >= 2 up to minimal w
            if x < h:
                # If the queried row index is less than current height border,
                # Update t2 for all affected rows and reduce h.
                tmp = w
                for i in range(x, h + 1):
                    t2[i] = w
                h = x
            else:
                # If already processed, just retrieve last block value for x.
                tmp = t2[x]
            # Subtract the number of affected columns (excluding edges).
            ans -= tmp - 2

    # Output the final answer after all queries.
    print(ans)

# Run the function to process queries as per the algorithm
process_queries()