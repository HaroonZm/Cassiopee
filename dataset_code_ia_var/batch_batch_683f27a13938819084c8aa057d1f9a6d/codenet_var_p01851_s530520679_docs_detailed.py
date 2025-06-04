import sys

# Alias for faster input and output
readline = sys.stdin.readline
write = sys.stdout.write

# Modulo constant for calculations
MOD = 10**9 + 7

# Precompute factorials and inverse factorials up to L to enable combinatorial calculations efficiently.
L = 4 * 10**6
fact = [1] * (L + 1)    # fact[i] = i! % MOD
rfact = [1] * (L + 1)   # rfact[i] = (i!)^{-1} % MOD (Modular inverse of i!)
r = 1

# Precompute all factorials modulo MOD
for i in range(1, L + 1):
    fact[i] = r = r * i % MOD

# Compute the inverse factorial for L using Fermat's little theorem, then propagate backwards
rfact[L] = r = pow(fact[L], MOD - 2, MOD)
for i in range(L, 0, -1):
    rfact[i - 1] = r = r * i % MOD

def solve():
    """
    Reads a line of input, parses integers A, B, C, Sx, Sy and
    performs a combinatorial calculation based on their values.

    The function handles several edge cases, performs a main combinatorial sum,
    and outputs the result to stdout.

    Returns
    -------
    bool
        Returns True if the function should be called again for more input,
        or False if input is exhausted or a terminating condition is met.
    """

    # Read input
    A, B, C, Sx, Sy = map(int, readline().split())

    # Terminate if the input indicates the end (all zero)
    if A + B + C == 0:
        return False

    # Ensure that Sx is greater than Sy; if not, swap (A,B) and (Sx, Sy)
    if not Sx > Sy:
        A, B = B, A
        Sx, Sy = Sy, Sx

    # Compute the difference between Sx and Sy and set up K
    Sd = Sx - Sy
    K = Sy
    zero = False    # Flag to determine if the answer should be zero

    # Handle special cases where some parameters are zero
    if A == 0:
        if B > 0 or Sd != 0:
            zero = True
        else:
            K = 0
    elif B == 0:
        K = 0

    # If flagged, output zero and terminate this call
    if zero:
        write("0\n")
        return True

    res = 0    # Initialize result accumulator

    # Main combinatorial sum loop
    for k in range(K + 1):
        # Validate parameters to avoid out-of-bounds or nonsensical values
        if Sd + k < A or k < B:
            continue

        # Compute the combinatorial result for this value of k, using precomputed factorials
        r = fact[Sd + k - 1] * rfact[Sd + k - A] % MOD
        r = r * (fact[k - 1] * rfact[k - B] % MOD) % MOD
        r = r * (fact[Sy - k + A + B + C - 1] * rfact[Sy - k] % MOD) % MOD
        res += r    # Accumulate into result

    # Reduce accumulated sum modulo MOD
    res %= MOD

    # Apply additional combinatorial multipliers and divisors according to the problem's requirements
    res = res * (fact[A + B + C] * rfact[A] % MOD) % MOD
    res = res * (rfact[B] * rfact[C] % MOD) % MOD
    res = res * (rfact[A - 1] * rfact[B - 1] % MOD) % MOD
    res = res * rfact[A + B + C - 1] % MOD

    # Output the result
    write("%d\n" % res)
    return True

# Continuously execute 'solve' while it returns True (i.e., while there is more input to process)
while solve():
    ...