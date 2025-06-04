import string

# Define a large value to represent infinity.
INF = 1 << 30

def conv(base, num):
    """
    Convert a number given as a string in a specified base to its decimal (base 10) integer value.
    
    Args:
        base (int): The base in which the number is represented.
        num (str): The string representation of the number in the specified base.
    
    Returns:
        int: The decimal value of the input number.
    
    The function supports bases larger than 10, allowing alphabetic characters ('A', 'B', ..., 'Z') 
    to represent digits 10 and above.
    """
    ret = 0  # Initialize the result
    for n in str(num):
        # Convert each character to the appropriate numeric value
        if n in string.ascii_letters:
            # For letters, map 'A' to 10, 'B' to 11, etc.
            n = ord(n.upper()) - ord("A") + 10
        else:
            # For digits, directly convert to integer
            n = int(n)
        # Accumulate the value according to positional notation
        ret = ret * base + n
    return ret

def get_fact(n):
    """
    Compute the prime factorization of a number.
    
    Args:
        n (int): The integer to be factorized.
    
    Returns:
        list of tuple: A list of tuples where each tuple contains a prime factor and its exponent.
        
    Each tuple is of the form (prime_factor, exponent), indicating that 'prime_factor' appears 
    'exponent' times in the prime factorization of 'n'.
    """
    ret = []  # Store the result as a list of (prime, exponent) tuples
    i = 2     # Start checking for factors from 2
    while i <= n:
        cnt = 0  # Counter for the current exponent
        # While 'i' divides 'n', increase the exponent and divide 'n'
        while n % i == 0:
            cnt += 1
            n //= i  # Use integer division to keep 'n' as an integer
        if cnt != 0:
            # We've found a prime factor 'i' with exponent 'cnt'
            ret.append((i, cnt))
        i += 1  # Increment the factor to check for the next integer
    return ret

def main():
    """
    Main loop to process successive inputs of base and number strings, compute the largest integer k
    such that k! is divisible by the number represented in the given base.

    The function continues to process input until both base and number are zero.
    Each line of input should contain the base and the number (as a string), separated by a space.
    """
    while True:
        # Read input from the user. Expects two values separated by space.
        user_input = raw_input()
        base, num = user_input.split()

        # If both inputs are "0", terminate the loop
        if (base, num) == ("0", "0"):
            break

        base = int(base)

        # Convert number from the specified base to decimal
        num_dec = conv(base, num)

        # Find prime factors of the base
        fact = get_fact(base)

        ans = []  # List to hold the minimal count for each prime factor

        # Loop over each prime factor and its exponent in the factorization of the base
        for prime, exponent in fact:
            power = prime  # Current power of the prime
            cnt = 0        # Count of times 'prime' divides any number <= num_dec!

            # Use Legendre's formula to compute exponent of 'prime' in num_dec!
            while power <= num_dec:
                cnt += num_dec // power
                power *= prime

            # Divide the total count by the exponent in base factorization
            ans.append(cnt // exponent)

        # The answer is the minimal among all such quotients
        print(min(ans))

# Execute the main function when the script is run.
if __name__ == "__main__":
    main()