import sys

# Set up fast input and output methods
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    """
    Solves the problem as described in the input.
    
    Reads integers specifying the number of rounds (H), number of positions (N),
    initial position (P), number of rounds with predetermined swaps (M), and a limit value (K).
    Then, M predetermined swap actions are read.
    Calculates and writes the maximal probability for a specific event after K steps,
    using dynamic programming.
    """
    # Read input parameters: H (total rounds), N (number of positions), P (starting position),
    # M (number of predetermined swaps), K (maximum steps allowed)
    H, N, P, M, K = map(int, readline().split())
    
    # Initialize swap actions: A[i] stores which positions to swap at round i (0 if random)
    A = [0] * H
    for i in range(M):
        a, b = map(int, readline().split())
        A[a-1] = b  # The swap at round (a-1) involves position b
    
    # S[k][x] represents the probability of being at position x after k randomizations
    S = [[0] * N for _ in range(K+1)]
    S[0][P-1] = 1  # Initial probability: 1 at starting position, 0 elsewhere

    # Temporary storage for previous step's probabilities
    T = [[0] * N for _ in range(K+1)]
    
    # Process the rounds in reverse order (from last to first)
    for i in range(H-1, -1, -1):
        b = A[i]  # Get swap position for this round (0 if random)
        # Copy current probabilities for this round's processing
        for j in range(K+1):
            T[j][:] = S[j][:]
        
        if b > 0:
            # If there is a predetermined swap: swap probabilities between positions b-1 and b
            for Si in S:
                Si[b-1], Si[b] = Si[b], Si[b-1]
        else:
            # If randomization: update the probability distribution for each possible additional randomization
            for k in range(K):
                # v is a normalization factor: what fraction of "extra" randomness can still be spent
                v = (K - k) / (H - M - k)
                # Update probabilities for internal positions (not the endpoints)
                for j in range(1, N-1):
                    S[k+1][j] += (T[k][j-1] + T[k][j] * (N-3) + T[k][j+1]) / (N-1) * v
                # Update probabilities for the leftmost endpoint
                S[k+1][0] += (T[k][0] * (N-2) + T[k][1]) / (N-1) * v
                # Update probabilities for the rightmost endpoint
                S[k+1][N-1] += (T[k][N-1] * (N-2) + T[k][N-2]) / (N-1) * v
    
    # Output the maximum probability over all positions after K randomizations
    write("%.016f\n" % max(S[K]))

solve()