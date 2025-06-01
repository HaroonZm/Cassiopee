def process_inputs():
    """
    Continuously reads input lines representing three integers until the sentinel '0 0 0' is encountered.
    For each set of inputs:
        - Initializes a list 'd' with default value 2 for each node, indexed from 1 to sum of the three integers.
        - Reads further input lines defining edges with additional attributes.
        - Updates 'd' based on the presence or absence indicated by 'v' value.
        - Processes collected edges to make further updates to 'd'.
        - Prints the final state of 'd' (excluding the zero index).
    
    This function does not take any arguments and performs I/O operations directly.
    """
    # Loop until input line is '0 0 0'
    for e in iter(input, '0 0 0'):
        # Convert the input string of three integers into a list and sum them to get total nodes
        total_nodes = -~sum(map(int, e.split()))  # -~x is equivalent to x+1

        # Initialize list 'd' of length total_nodes with default value 2
        # This list tracks the state of each node, index 0 is unused to align with node numbering
        d = [2] * total_nodes

        # Initialize list to hold edges where v == 0
        f = []

        # Read the number of edges to process from the next input line
        num_edges = int(input())

        # Process each edge input line
        for _ in range(num_edges):
            # Parse edge attributes: s, t, u are node indices, v is a flag
            s, t, u, v = map(int, input().split())

            # If flag v is non-zero, mark corresponding nodes in 'd' as 1
            if v:
                d[s] = 1
                d[t] = 1
                d[u] = 1
            else:
                # If flag v is zero, store edge tuple for later processing
                f.append((s, t, u))

        # Process the stored edges where v == 0 to update 'd'
        for s, t, u in f:
            # If both nodes t and u are marked as 1, set node s to 0
            if d[t] * d[u] == 1:
                d[s] = 0

            # If both nodes u and s are marked as 1, set node t to 0
            if d[u] * d[s] == 1:
                d[t] = 0

            # If both nodes s and t are marked as 1, set node u to 0
            if d[s] * d[t] == 1:
                d[u] = 0

        # Print the state of d for nodes 1 through end, each on a new line
        print(*d[1:], sep='\n')


# Call the function to execute the processing
process_inputs()