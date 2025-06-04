def process_sequences():
    """
    Reads input data to process a list of integer sequences (lists) according to specified commands.
    The first input line should contain two integers: n (number of sequences) and seq (number of operations).
    Then, seq lines follow, each with a command:
        - c t x: where c is the command type, t is the target sequence index, and x (if needed) is a value.
            - If c == 0: append x to the sequence at index t.
            - If c == 1: print the sequence at index t as space-separated values.
            - If c == 2: clear the sequence at index t.
    """
    # Parse the first input line to get number of sequences n and commands seq
    n, seq = [int(x) for x in input().split()]
    
    # Initialize a list containing n empty lists, each representing a sequence
    L = []
    for i in range(n):
        L.append([])

    # Process each command
    for i in range(seq):
        # Read the next command line and ensure it has at least three elements by appending "0"
        c, t, x = [int(x) for x in (input() + " 0").split()][:3]
        
        if c == 0:
            # Command 0: Append x to the sequence at index t
            L[t].append(x)
        elif c == 1:
            # Command 1: Print the sequence at index t as space-separated values
            print(" ".join(map(str, L[t])))
        elif c == 2:
            # Command 2: Clear the sequence at index t
            L[t].clear()
        else:
            # Unknown command; do nothing
            pass

# Run the sequence processing function
process_sequences()