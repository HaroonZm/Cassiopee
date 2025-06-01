MAX = 1000000
SQRT = 1000     # Approximate square root of MAX for sieve limit
comp = [0] * (MAX + 2)  # List to mark composite numbers; 0 means prime candidate

def sieve():
    """
    Populate the 'comp' list with composite number markers using the Sieve of Eratosthenes algorithm.
    Odd composite numbers between 3 and MAX are marked with 1.
    Even numbers are excluded since 2 is the only even prime.
    """
    for i in range(3, SQRT, 2):  # Iterate over odd numbers up to SQRT
        if comp[i] == 0:  # If i is a prime candidate
            for j in range(i * i, MAX, i):  # Mark multiples of i as composite
                comp[j] = 1

# Run sieve to mark composite numbers up to MAX
sieve()

# tbl[i] will store the count of primes up to i (inclusive)
tbl = [0] * (MAX + 2)
tbl[2] = 1  # 2 is prime, so start count at 1
k = 1       # Count of primes encountered so far

# Fill the tbl array with cumulative counts of primes
for i in range(3, MAX, 2):  # Consider only odd numbers (2 handled separately)
    if comp[i] == 0:
        k += 1  # Found a prime, increment count
    tbl[i] = k
    tbl[i + 1] = k  # For even indices, copy the prime count from the previous odd number

while True:
    n = int(input())
    if n == 0:
        break  # Exit condition for input loop
    ans = 0  # Initialize answer accumulator for this test case
    for _ in range(n):
        p, m = map(int, input().split())
        a, b = p - m, p + m  # Define inclusive range [a, b] around p
        if a < 2:
            a = 2  # Primes start at 2, so adjust lower bound
        if b > MAX:
            b = MAX  # Upper bound limited by MAX
        # Calculate number of primes in [a, b]
        # Subtract 1 to exclude p itself if it's prime and within the range
        ans += tbl[b] - tbl[a - 1] - 1
    if ans < 0:
        ans = 0  # Ensure ans is non-negative
    print(ans)