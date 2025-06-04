def ilog2(n):
    """
    Compute the floor of the base-2 logarithm of a positive integer n.
    If n is less than or equal to 0, returns 0.

    Args:
        n (int): The integer to compute the log2 of.

    Returns:
        int: The floor of log2(n), or 0 if n <= 0.
    """
    return 0 if n <= 0 else n.bit_length() - 1

def pack(pack, shamt):
    """
    Packs an array of integers into a single integer by bitwise interleaving.

    Args:
        pack (list of int): The list to pack.
        shamt (int): The initial shift amount.

    Returns:
        int: The packed integer.
    """
    size = len(pack)
    # Continue reducing until only one integer remains
    while size > 1:
        npack = []
        # Pairwise combine with left-shift and bitwise OR
        for i in range(0, size - 1, 2):
            npack.append(pack[i] | (pack[i+1] << shamt))
        # If odd, carry the last element unchanged
        if size & 1:
            npack.append(pack[-1])
        # Prepare for next round with half the size and double the shift
        pack, size, shamt = npack, (size + 1) >> 1, shamt << 1
    return pack[0]

def unpack(M, size, shamt):
    """
    Unpacks a single packed integer into an array of integers using provided shift size.

    Args:
        M (int): The packed integer.
        size (int): The number of elements to unpack.
        shamt (int): The initial shift amount (width per element).

    Returns:
        list of int: The unpacked list of integers.
    """
    s = size
    sizes = []
    # Record sizes at each depth of packing
    while s > 1:
        sizes.append(s)
        s = (s + 1) >> 1
    ret = [M]
    # Unpack from least to most packed level
    for size in reversed(sizes):
        mask = (1 << shamt) - 1
        nret = []
        for c in ret:
            nret.append(c & mask)
            nret.append(c >> shamt)
        ret, shamt = nret[:size], shamt >> 1
    return ret

def poly_mul_mod(f, g, mod):
    """
    Multiplies two polynomials under a modulus using integer packing tricks.

    Args:
        f (list of int): Coefficient list for the first polynomial.
        g (list of int): Coefficient list for the second polynomial.
        mod (int): Modulus for coefficients.

    Returns:
        list of int: Resulting coefficients modulo mod.
    """
    size = min(len(f), len(g))
    # Calculate bit shift to avoid overlaps
    shift = ((mod - 1) ** 2 * size).bit_length()
    rsize = len(f) + len(g) - 1
    # Pack and multiply, then unpack
    h = unpack(
        pack(f, shift) * pack(g, shift),
        rsize,
        shift * (1 << ilog2(rsize - 1))
    )
    # Reduce each coefficient modulo mod
    return [int(x % mod) for x in h]

# Define modulus and size for factorial/precompute arrays
mod = 998244353
N = 10 ** 4 + 10

def inv(n):
    """
    Compute modular inverse of n modulo mod, using Fermat's little theorem.

    Args:
        n (int): The number to invert.

    Returns:
        int: The modular inverse of n modulo mod.
    """
    return pow(n, mod - 2, mod)

def poly_power_mod(f, n, mx):
    """
    Raises a polynomial to the given power modulo mod, truncated to degree < mx.

    Args:
        f (list of int): Polynomial coefficients.
        n (int): The exponent.
        mx (int): The size limit for the output's degree.

    Returns:
        list of int: The resulting coefficients modulo mod, length mx.
    """
    ret = [1]
    f_copy = f[:]
    while n:
        # If the lowest bit is set, multiply into result
        if n & 1:
            ret = poly_mul_mod(ret, f_copy, mod)[:mx]
        # Square polynomial for next bit
        f_copy = poly_mul_mod(f_copy, f_copy, mod)[:mx]
        n >>= 1
    return ret

# Precompute factorials, inverse factorials, and the polynomial for powers
fact = [1] * N
ifact = [1] * N
poly = [1] * N

for i in range(1, N):
    fact[i] = (fact[i - 1] * i) % mod
    ifact[i] = (ifact[i - 1] * inv(i)) % mod
    poly[i - 1] = ifact[i]

# Read inputs as binary strings
A = raw_input()
B = raw_input()
n = 0  # Number of '1' bits in A
m = 0  # Number of '1's in A, but not in B

# Count positions where A is '1', and where A is '1' but B is not
for i in range(len(A)):
    if A[i] == '1':
        n += 1
        if B[i] != '1':
            m += 1

ans = 0
# Compute the m-th power of polynomial and truncate to degree n+1
poly_power = poly_power_mod(poly, m, n + 1)

# Main combinatorial summation
for k in range(n - m + 1):
    # Compute coefficient for current term, using factorials
    term = fact[n - m - k] * fact[n - m - k] % mod
    if k < len(poly_power):
        term = term * poly_power[k] * fact[m] % mod
    else:
        term = 0
    term = term * fact[n - m] * fact[n] * ifact[n - m - k] * ifact[n - m - k] % mod
    ans = (ans + term) % mod

# Output the final answer modulo mod
print ans % mod