# AOJ 1208 - Rational Approximation Code with Detailed Comments and Docstrings

import math

def rational(p, n):
    """
    Given a value p and a maximum denominator n, this function finds two rational approximations
    of sqrt(p) with the smallest differences from sqrt(p), for denominators up to n.
    It then prints two fractions: 
      - one just greater than sqrt(p) (the 'upper' approximation),
      - one just less than sqrt(p) (the 'lower' approximation).
    
    Args:
        p (int): The value whose square root is to be approximated.
        n (int): The maximum allowed denominator for the approximation.
    """
    rt = math.sqrt(p)            # Calculate the square root of p
    k = math.floor(rt)           # Take the integer part of the square root as a baseline
    # Initialize the minimum and maximum difference variables to 'n' (a large value)
    mi = n                       # Smallest fractional part below the square root
    mx = n                       # Smallest fractional part above the square root
    mikk = 0                     # Denominator for the lower approximation
    mibb = 0                     # Numerator offset for the lower approximation
    mxkk = 0                     # Denominator for the upper approximation
    mxbb = 0                     # Numerator offset for the upper approximation

    # Iterate through all possible denominators from 1 to n
    for i in range(1, n + 1):
        a = (rt - k) * i         # Compute the fractional part times the denominator
        b = math.floor(a)        # Get the integer part of a

        # Check for the best lower approximation (just less than sqrt(p))
        # with numerator = k * i + b and denominator = i
        if mi > a - b and k * i + b <= n:
            mi = a - b
            mikk = i             # Store the denominator
            mibb = b             # Store the numerator offset

        # Check for the best upper approximation (just greater than sqrt(p))
        # with numerator = k * i + (b + 1) and denominator = i
        if mx > b + 1 - a and k * i + (b + 1) <= n:
            mx = b + 1 - a
            mxkk = i             # Store the denominator
            mxbb = b             # Store the numerator offset

    # Print the result in the required format:
    #   Upper rational approximation, then lower rational approximation
    print("{}/{} {}/{}".format(
        k * mxkk + (mxbb + 1), mxkk,   # Upper approximation numerator/denominator
        k * mikk + mibb, mikk          # Lower approximation numerator/denominator
    ))

def main():
    """
    Main function to repeatedly read lines from standard input,
    parse them into integers p and n, call the rational() approximation,
    and terminate when a pair of zeros is input.
    """
    while True:
        # Read a line from input and split into components
        line = input().split()
        # Parse input as integers
        p, n = map(int, list(line))
        # Termination condition: both inputs are zero
        if p == 0 and n == 0:
            break
        # Call the rational approximation function
        rational(p, n)

# Invoke the main function when the script is run
if __name__ == '__main__':
    main()