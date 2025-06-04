def count_strings_with_conditions():
    """
    Reads an integer and a string from input, and computes a final result
    using a dynamic programming approach. Each step of the calculation modifies
    an array according to specific rules, and the process is repeated 'n' times.
    The result is printed to output.

    The specific logic is as follows:
    - 'n' is the number of iterations and the maximum index used.
    - A list 'p' of size 5001 is initialized with zeros to be used as a DP array.
    - The length of the input string determines the initial position set to 1.
    - The DP update involves, for each index j in range(n):
      If j == 0: (take p[j])
      Otherwise: (take 2 * p[j-1])
      And add p[j+1]
    - All operations are performed modulo 1_000_000_007.
    - The final result is p[0].
    """
    MOD = 10**9 + 7  # Large prime for modulo operations

    # Read number of steps/maximum index to use
    n = int(input())

    # Initialize DP array where indices represent string lengths or states
    p = [0] * 5001

    # Read string and set starting position in DP array to 1 based on its length
    s = input()
    p[len(s)] = 1

    # Main DP loop: update DP array for 'n' iterations
    while n:
        # For each position j, compute new value based on neighbors and itself
        new_p = []
        for j in range(n):
            # If j > 0, include twice the value of p[j-1], else use p[j] only
            left = 2 * p[j-1] if j > 0 else p[j]
            # Always add the value to the right (p[j+1])
            right = p[j+1]
            # Combine, apply modulo, and append to new DP array
            new_val = (left + right) % MOD
            new_p.append(new_val)
        # Update DP array and decrease n
        p = new_p
        n -= 1

    # Final result, print computed value for base position
    print(p[0])

# Call the main function to execute the process
count_strings_with_conditions()