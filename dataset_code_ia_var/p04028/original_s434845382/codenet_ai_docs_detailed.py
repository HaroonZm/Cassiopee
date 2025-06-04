N = int(input())  # Read the input integer N, representing the problem size.
s = input()       # Read the input string s.
mod = 10 ** 9 + 7 # Define the modulus value for computations (commonly used to avoid overflow).

def main():
    """
    Main function to calculate and print the required value based on dynamic programming.
    Uses a DP table to efficiently calculate combinatorial values modulo mod.
    """
    # Initialize a two-row dynamic programming table.
    # dp[t][j] represents a computed result at step t mod 2 and for value j.
    dp = [[0 for _ in range(N+1)] for _ in range(2)]
    dp[0][0] = 1  # Base case: one way to start with 0 items processed and size 0.
    
    # Loop through each position from 0 to N-1
    for i in range(N):
        # Reset the next row of dp to 0 for fresh computation
        for j in range(N):
            dp[(i+1)%2][j] = 0

        # For each valid state in the current row, update the next row
        for j in range(N):
            # Transition: Increase the value of j by 1, multiplying the number of ways by 2
            dp[(i+1)%2][j+1] = (dp[(i+1)%2][j+1] + dp[i%2][j] * 2) % mod
            
            # Transition: Decrease the value of j by 1 if possible
            if j-1 >= 0:
                dp[(i+1)%2][j-1] = (dp[(i+1)%2][j-1] + dp[i%2][j]) % mod
            # If j-1 is not possible, stay at the same j
            else:
                dp[(i+1)%2][j] = (dp[(i+1)%2][j] + dp[i%2][j]) % mod

    # Compute modular inverse of pow(2, len(s)), to normalize the result
    pow2 = pow(2, len(s), mod)
    inv_pow2 = pow(pow2, mod-2, mod)  # Modular multiplicative inverse

    # Output the final result: normalized DP value for state (N, len(s))
    print((dp[N%2][len(s)] * inv_pow2) % mod)

if __name__=='__main__':
    main()