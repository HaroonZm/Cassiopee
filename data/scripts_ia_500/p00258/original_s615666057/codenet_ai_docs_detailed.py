bc = [bin(i).count('1') for i in range(65536)]
# Precompute the bit counts for all 16-bit integers (0 to 65535).
# This list allows O(1) retrieval of the number of set bits in any 16-bit number,
# used repeatedly in the dynamic programming for efficiency.

def solve():
    """
    Reads multiple test cases from standard input until a terminating condition is met.
    Each test case consists of:
      - n: number of initial states
      - c: number of available operations
      - n lines representing binary strings (states)
      - c lines representing binary strings (operations)
    
    The function uses dynamic programming to find the maximum score achievable by applying operations
    on the states according to the specified rules.

    Scoring rules:
      - For each state and operation, the score increases by the count of bits set in the intersection of the state and operation.
      - The new state is formed by removing these intersecting bits from the current state and then adding bits from the next state's bitmask.
    
    Time complexity is O(n * (2^16) * c), which is feasible given constraints.
    """
    from sys import stdin
    f_i = stdin

    while True:
        # Read n (number of states) and c (number of operations)
        n, c = map(int, f_i.readline().split())
        if n == 0:
            # Termination condition for the input
            break
        
        # Read n lines, each a binary string representing a state,
        # convert them to integers by removing spaces and treating as base-2 numbers
        A = [int(f_i.readline().replace(' ', ''), 2) for i in range(n)]
        
        # Read c lines, each a binary string representing an operation,
        # similarly converted to integers
        B = [int(f_i.readline().replace(' ', ''), 2) for i in range(c)]
        
        # Initialize dynamic programming dictionary:
        # key = current state bitmask, value = maximum score achieved so far
        dp1 = {A[0]: 0}
        dp2 = {}
        
        # Iterate through the remaining n-1 states plus one additional iteration with a=0
        # to simulate the final transition step
        for a in A[1:] + [0]:
            # For each state (st1) and its current score (sc1) in dp1
            for st1, sc1 in dp1.items():
                # Try applying each operation b
                for b in B:
                    # Calculate bits common to state and operation
                    cb = st1 & b
                    # Update score by adding number of bits set in cb
                    sc2 = sc1 + bc[cb]
                    # Compute the new state after removing cb bits from st1 and adding bits from next state a
                    st2 = (st1 - cb) | a
                    # Store the best score for this resulting state in dp2
                    if st2 not in dp2 or dp2[st2] < sc2:
                        dp2[st2] = sc2
            # Move dp2 into dp1 for the next iteration and reset dp2
            dp1, dp2 = dp2, {}
        
        # After processing all states, output the maximum achievable score
        print(max(dp1.values()))

solve()