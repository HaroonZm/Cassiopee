def handle_queries():
    """
    Reads an integer q (number of queries) from standard input, then processes q queries to manipulate a 64-bit number bitwise.
    Each query consists of a list of integers where the first number denotes the operation to be performed, with the subsequent(s)
    indicating parameters for the operation. Results from queries that require output are printed to standard output.

    Supported operations:
      0 i:  Check if the i-th bit is set in n.
      1 i:  Set the i-th bit of n.
      2 i:  Unset (clear) the i-th bit of n.
      3 i:  Toggle the i-th bit of n.
      4:    Check if all 64 bits are set in n.
      5:    Check if any bit is set in n.
      6:    Check if all bits are unset in n.
      7:    Count the number of set bits in n.
      8:    Output the current value of n.
    """
    q = int(input())  # Read number of queries

    MASK = (1 << 64) - 1  # 64-bit mask, all bits set to 1 for 64 bits
    n = 0  # Our "bitset": the 64-bit number initialized to 0

    for _ in range(q):
        # Read the query: first integer is the operation, rest are parameters
        query = [i for i in map(int, input().split())]
        op = query[0]  # Operation type

        if op == 0:
            # Check if i-th bit is set in n
            i = query[1]
            temp = 1 << i  # Bitmask for i-th bit
            if (n & temp) == 0:
                print(0)
            else:
                print(1)

        elif op == 1:
            # Set the i-th bit of n
            i = query[1]
            temp = 1 << i
            n = n | temp  # Set the bit using OR

        elif op == 2:
            # Unset (clear) the i-th bit of n
            i = query[1]
            temp = 1 << i
            n = n & (~temp & MASK)  # Clear the bit and mask to stay within 64 bits

        elif op == 3:
            # Toggle the i-th bit of n
            i = query[1]
            temp = 1 << i
            n = n ^ temp  # Flip the i-th bit

        elif op == 4:
            # Check if all bits are set (n is 2^64-1)
            if n == MASK:
                print(1)
            else:
                print(0)

        elif op == 5:
            # Check if at least one bit is set
            if n & MASK > 0:
                print(1)
            else:
                print(0)

        elif op == 6:
            # Check if all bits are unset (n == 0)
            if n == 0:
                print(1)
            else:
                print(0)

        elif op == 7:
            # Count the number of set bits in n
            temp = n
            one = 1
            counter = 0
            for _ in range(64):
                if (one & temp) == 1:
                    counter += 1
                temp = temp >> 1
            print(counter)

        elif op == 8:
            # Output the current value of n
            print(n)

# Call the function to execute the program
handle_queries()