def read_input():
    """
    Read the input values from the standard input.
    
    Returns:
        N (int): The size of the permutations.
        P (list of int): The first permutation (0-based).
        Q (list of int): The second permutation (0-based).
    """
    N = int(input())
    # Read permutation P, converting to 0-based indexing
    P = [int(x) - 1 for x in input().split()]
    # Read permutation Q, converting to 0-based indexing
    Q = [int(x) - 1 for x in input().split()]
    return N, P, Q

def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm.
    Solves for integers x, y such that a*x + b*y = gcd(a, b).
    
    Args:
        a (int): First number.
        b (int): Second number.
    Returns:
        tuple: (gcd, x, y)
    """
    if b == 0:
        return (a, 1, 0)
    q = a // b
    g, x, y = extended_gcd(b, a - q * b)
    z = x - q * y
    return (g, y, z)

def chinese_remainder(A, B, a, b):
    """
    Combine two congruences using the generalized Chinese Remainder Theorem.
    Given:
        x ≡ A mod B
        x ≡ a mod b
    Finds their unique solution modulo lcm(B, b), if one exists.
    
    Args:
        A (int): The first remainder.
        B (int): The first modulus.
        a (int): The second remainder.
        b (int): The second modulus.
    Returns:
        tuple: (A_new, B_new) - the merged congruence (x ≡ A_new mod B_new),
               or (0, 0) if no solution exists.
    """
    g, x, y = extended_gcd(B, b)
    # Check if the difference is divisible by gcd
    if (a - A) % g != 0:
        return (0, 0)
    # Adjust the solution for offset
    x *= (a - A) // g
    A += B * x
    # Update modulus to LCM of B and b
    B = B // g * b
    # Ensure result is in the canonical range [0, B)
    A %= B
    if A < 0:
        A += B
    return (A, B)

def main():
    """
    Main function to process the permutations and solve for the minimal time X such that 
    after X applications of permutation Q to permutation P, the identity is reached for each index,
    or outputs -1 if impossible.
    """
    N, P, Q = read_input()
    # ap[i][j] is the earliest time step when position i maps to j, initialized to -1
    ap = [[-1 for _ in range(N)] for _ in range(N)]
    # b_j: the cycle length for each position j
    b = [0] * N

    # For N + 1 steps, update mapping history
    P_current = list(P)
    for i in range(N + 1):
        for j in range(N):
            # If already visited this state, set cycle length for b[j]
            if ap[j][P_current[j]] >= 0:
                if b[j] == 0:
                    b[j] = i - ap[j][P_current[j]]
            else:
                ap[j][P_current[j]] = i
            # Update current position by applying Q
            P_current[j] = Q[P_current[j]]

    # a[i]: first time step when the i-th position returns to i
    a = [ap[i][i] for i in range(N)]
    flag = True

    # Check if any position never returns (i.e., a[i] < 0)
    if sum(A < 0 for A in a) > 0:
        flag = False

    # A: solution to the congruence; B: current modulus
    A = 0
    B = 1

    # For each index i, merge the current solution with the new congruence
    for i in range(N):
        if flag:
            A, B = chinese_remainder(A, B, a[i], b[i])
            if B == 0:
                flag = False

    # Output result: the smallest non-negative X or -1 if no solution exists
    print(A if flag else -1)

if __name__ == "__main__":
    main()