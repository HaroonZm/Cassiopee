# AOJ 1141: Dirichlet's Theorem on Arithmetic Progression
# Solution in Python3
# This program finds the n-th prime in the arithmetic progression a, a+d, a+2d, ...

# Define the maximum value up to which we want to check for primes.
# This is used to create the sieve array. All numbers less than MAX can be checked for primality.
MAX = 1000000  # We set the limit for checking prime numbers to one million.

# SQRT represents the integer square root of MAX.
# This is required because in the Sieve of Eratosthenes algorithm, we only need to go up to the square root of the highest number to mark composite numbers.
SQRT = 1000    # Since sqrt(1_000_000) is 1000; so, we only go up to 1000 in the sieve.

# We create an array (list) called 'prime' that will indicate if a number is prime or not.
# The length of this array is MAX, and all elements are initialized to True.
# The idea is: prime[i] == True means that the number 'i' is assumed to be prime initially.
prime = [True]*MAX  # Create a list of length MAX (i.e., 1_000_000), with all values set to True.

# Define the sieve function that will fill/enrich the 'prime' array using the Sieve of Eratosthenes algorithm.
def sieve():
    # The number 1 is known NOT to be prime, so we set its corresponding index to False.
    # In arrays, index 1 corresponds to the integer 1.
    prime[1] = 0

    # All even numbers greater than 2 are not prime, so we begin by marking them as not prime starting from 4.
    # We use the range function to iterate from 4 to MAX (not inclusive) in steps of 2, thus getting all even numbers.
    for i in range(4, MAX, 2):
        prime[i] = False  # Mark even numbers as not prime (except for 2 itself).

    # Now we need to mark other composite numbers. We only need to consider odd numbers for this purpose.
    # We iterate i from 3 to SQRT, taking step 2 to only check odd numbers.
    for i in range(3, SQRT, 2):
        # If 'i' is still marked as prime, then mark all its multiples as not prime.
        if prime[i]:
            # Begin marking multiples of 'i' as not prime.
            # We start from i*i because all smaller multiples of 'i' would already have been marked by smaller primes.
            # Go from i*i up to MAX (not inclusive), in steps of i.
            for j in range(i*i, MAX, i):
                prime[j] = False  # Mark multiple j as not a prime.

# Call the sieve function to populate the 'prime' list with correct information about each number's primality.
sieve()

# The main loop of the program. This loop continues until the user provides a line starting with 0.
while True:
    # The input is a line containing three integers separated by spaces: a, d, and n.
    # Example: "367 186 151"
    # input().split() splits the input into parts by whitespace, and map(int, ...) converts each part to an integer.
    a, d, n = map(int, input().split())

    # If a == 0, that means end of input, so we break out of the loop and the program terminates.
    if a == 0:
        break

    # Before starting the search, decrement 'a' by 'd' so that on the first iteration of the loop below, adding d brings us to the real starting value 'a'.
    a -= d

    # Now, repeatedly search for the n-th prime in the sequence.
    # 'n' is the count of primes still left to find. We continue looping while n > 0.
    while n > 0:
        # Add 'd' to 'a' to get the next term in the arithmetic progression.
        a += d

        # Check if 'a' is a prime number by examining prime[a].
        # If it is a prime, reduce the count 'n' by 1, because that means we've found one more prime in the progression.
        if prime[a]:
            n -= 1

    # Once n reaches 0, 'a' contains the n-th prime in the arithmetic progression.
    # Output the number found.
    print(a)