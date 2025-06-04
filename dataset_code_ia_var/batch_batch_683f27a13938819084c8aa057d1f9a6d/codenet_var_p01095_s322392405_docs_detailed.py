from bisect import bisect_left

def rwh_primes2(n):
    """
    Generate a list of all prime numbers less than n using an optimized Sieve of Eratosthenes algorithm.

    Args:
        n (int): An integer greater than or equal to 6. Function returns all prime numbers p such that 2 <= p < n.

    Returns:
        list[int]: Sorted list of all primes less than n.

    Note:
        Based on an optimization from StackOverflow (reference in original code).
        Uses 6k +/- 1 wheel factorization for efficiency.
    """
    # Adjust n so that it fits the wheel, correcting by n mod 6
    correction = (n % 6 > 1)
    n = {0: n, 1: n-1, 2: n+4, 3: n+3, 4: n+2, 5: n+1}[n % 6]
    
    # Start with a sieve list covering possible primes using the 6k+/-1 pattern
    sieve = [True] * (n // 3)
    sieve[0] = False  # 1 is not a prime

    # Iterate through the sieve up to the square root of n
    for i in range(int(n**0.5)//3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1  # This maps i to wheel index
            # Mark all multiples of k*k as non-prime
            sieve[((k*k)//3) :: 2*k] = [False] * ((n//6 - (k*k)//6 - 1)//k + 1)
            # Mark additional composites for even/odd indices
            sieve[(k*k+4*k-2*k*(i&1))//3 :: 2*k] = [False] * ((n//6 - (k*k+4*k-2*k*(i&1))//6 - 1)//k + 1)
    # Combine found primes with 2 and 3, and return results
    return [2, 3] + [3*i+1|1 for i in range(1, n//3-correction) if sieve[i]]

def find_nth_prime_or_composite(m, n, prime_list):
    """
    Find the nth number (zero-based) in the sequence formed by merging 
    primes >= m and particular composite numbers constructed from products i*j 
    in the given range, following problem-defined constraints.

    Args:
        m (int): Lower bound of the range for composite and primes.
        n (int): Required zero-based index in the merged sequence.
        prime_list (list[int]): Precomputed list of all primes up to a bound.

    Returns:
        int: The nth element as specified by the algorithm.
    """
    # Find all small primes less than m^2 for factorization
    small_prime = prime_list[:bisect_left(prime_list, m**2)]
    composite = []

    # Generate "special" composite numbers x = i*j, m <= x <= m^2, 
    # x is not in small_prime, and obeys extra constraints (see below)
    for i in range(1, m+1):
        for j in range(i, m+1):
            x = i * j
            if m <= x <= m**2 and x not in small_prime:
                for p in small_prime:
                    if x % p == 0:
                        # Only add if composite x is less than m times its least prime divisor
                        if x < m * p:
                            composite.append(x)
                        break
    # Ensure unique and sorted composite numbers
    composite = sorted(list(set(composite)))
    
    # Set pointers to merge 'composite' and 'prime' lists
    pp = bisect_left(prime_list, m)  # Index in primes starting at first >= m
    cp = 0  # Index in composite
    sz = len(composite)

    # Merge the two sequences to find the nth element
    for i in range(n+1):
        if cp < sz:
            if composite[cp] < prime_list[pp]:
                ans = composite[cp]
                cp += 1
            else:
                ans = prime_list[pp]
                pp += 1
        else:
            # All composites consumed; fetch from the primes list directly
            ans = prime_list[pp + n - i]
            break
    return ans

if __name__ == "__main__":
    """
    Main execution block for running the prime and composite number search interactively.
    - Primes are precomputed up to a large bound.
    - For each input pair m, n, the merged sequence is searched and the nth item is printed.
    """
    # Precompute all primes up to a very high bound, suitable for input constraints
    prime = rwh_primes2(7368791 + 10)   # 7368787 is 500000th prime

    while True:
        # Read two space-separated integers m and n from user input
        m, n = map(int, input().split())
        # Stop input loop when both inputs are zero
        if m == 0 and n == 0:
            break
        # Compute and print the answer for the current input pair
        ans = find_nth_prime_or_composite(m, n, prime)
        print(ans)