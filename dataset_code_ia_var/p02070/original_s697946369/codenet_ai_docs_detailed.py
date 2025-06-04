from functools import reduce

def main():
    """
    Main execution function for solving a system of modular equations generated
    from permutation cycles. It takes input, processes permutations, constructs
    modular equations and solves them using the Chinese Remainder Theorem.
    """
    # Read the number of elements in the permutations
    N = int(input("Enter value for N: "))

    # Read permutation P as a list of integers, adjust to 0-based indexing
    P = list(map(int, input("Enter permutation P: ").split()))
    Q = list(map(int, input("Enter permutation Q: ").split()))

    # Convert both permutations to zero-based indexing for easier manipulation
    for i in range(N):
        P[i] -= 1
        Q[i] -= 1

    # Prepare equations for all indices in P/Q
    eqs = []
    for i in range(N):
        # For element at index i, trace its path under the permutation Q starting from P[i]
        a = []
        for j in range(3 * N):
            if len(a) == 2:
                break
            if P[i] == i:
                a.append(j)
            P[i] = Q[P[i]]  # Advance P[i] through permutation Q
        if len(a) != 2:
            # If no valid cycle found, problem has no solution
            print(-1)
            exit(0)
        # The equation is: x ≡ a[0] (mod a[1]-a[0])
        eqs.append([a[0], a[1] - a[0]])

    # Reduce all equations into one using the Chinese Remainder Theorem (CRT)
    x, mod = reduce(crt, eqs, (0, 1))
    # Output the solution in the canonical range
    print(x % mod)

def gcd(a, b):
    """
    Compute the greatest common divisor (GCD) of two integers using recursion.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: GCD of a and b.
    """
    if b == 0:
        return a
    return gcd(b, a % b)

def extgcd(a, b):
    """
    Extended Euclidean Algorithm.
    Given integers a and b, computes their GCD as well as coefficients x and y
    satisfying the equation: a*x + b*y = gcd(a, b).

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        list: [g, x, y] where g = gcd(a, b), and a*x + b*y = g.
    """
    if b == 0:
        return [a, 1, 0]
    g, x, y = extgcd(b, a % b)
    return [g, y, x - (a // b) * y]

def crt(eq0, eq1):
    """
    Chinese Remainder Theorem for combining two modular equations.

    Each equation is of the form:
        x ≡ a0 mod m0
        x ≡ a1 mod m1

    Args:
        eq0 (tuple/list): The first equation's [a0, m0].
        eq1 (tuple/list): The second equation's [a1, m1].

    Returns:
        list: [x, mod] representing x ≡ x (mod mod), the solution of both equations.
              If no solution exists, prints -1 and exits.
    """
    a0, m0 = eq0
    a1, m1 = eq1

    g = gcd(m0, m1)

    # Check compatibility: equations only have a solution if residues are equal modulo gcd
    if a0 % g != a1 % g:
        print(-1)
        exit(0)

    # Reduce the moduli if they are not coprime
    if g > 1:
        m0 //= g
        m1 //= g

        while True:
            gt = gcd(m0, g)
            if gt == 1:
                break
            m0 *= gt
            g //= gt

        m1 *= g

        a0 %= m0
        a1 %= m1

    # Solve for coefficients using extended GCD
    g, p, q = extgcd(m0, m1)

    # Compute combined solution
    x = a0 * q * m1 + a1 * p * m0
    mod = m0 * m1
    x = x % mod

    return [x, mod]

if __name__ == "__main__":
    main()