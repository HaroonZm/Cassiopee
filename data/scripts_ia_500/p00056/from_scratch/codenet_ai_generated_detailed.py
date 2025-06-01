# Import sys for efficient input reading
import sys

# Upper limit for n as given in problem
MAX_N = 50000

# Step 1: Use Sieve of Eratosthenes to find all primes up to MAX_N
# We create a list is_prime where is_prime[i] = True if i is prime, else False
is_prime = [True] * (MAX_N + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(MAX_N ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False

# Step 2: For each input number n, count the number of ways n can be expressed as sum of two primes
# The count considers two primes p and q such that p + q = n and p <= q to avoid double counting

# Read multiple inputs until 0 is encountered (which terminates input)
for line in sys.stdin:
    n = line.strip()
    if n == '0':
        break
    n = int(n)
    count = 0
    # If n is less than 4, definitely no representation, print 0
    if n < 4:
        print(0)
        continue
    # If n is odd, per problem, output 0 since it can't be expressed as sum of two primes (according to the example)
    # The problem states "4以上の偶数" so likely no sum for odd inputs
    if n % 2 != 0:
        print(0)
        continue
    # For even n >= 4, check all primes p <= n//2
    half = n // 2
    for p in range(2, half + 1):
        if is_prime[p]:
            q = n - p
            if is_prime[q]:
                # p + q = n and both primes, count this combination
                count += 1
    print(count)