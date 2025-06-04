#!/usr/bin/env python3

# Import the sys module, which provides access to system-specific parameters and functions.
# We'll use sys.stdin to read input from the standard input stream.
import sys

# Define two string constants, YES and NO, which will be used to output the result.
# "Possible" indicates a successful/valid scenario, and "Impossible" indicates failure/invalidity.
YES = "Possible"      # type: str
NO = "Impossible"     # type: str

def solve(N: int, a: "List[int]"):
    # The 'solve' function determines whether a given list 'a' of integers (of length N)
    # satisfies certain conditions and outputs "Possible" or "Impossible" as a result.

    # Calculate the maximum value in the list 'a' using the built-in max() function.
    amax = max(a)

    # Compute the minimum value threshold vmin.
    # Here, (amax + 1) // 2 performs integer division; it computes the half of the maximum value,
    # rounded up to the nearest whole number, due to the '+1' before division.
    vmin = (amax + 1) // 2

    # Determine the minimum count 'nmin' for the value vmin.
    # 'amax % 2' computes the remainder when amax is divided by 2 (i.e., checks if amax is odd or even).
    # If amax is even, 'amax % 2' is 0, thus nmin = 0 + 1 = 1.
    # If amax is odd, 'amax % 2' is 1, thus nmin = 1 + 1 = 2.
    nmin = amax % 2 + 1

    # Start a for loop. We check every integer 'i' starting from 1 up to and including 'amax'.
    for i in range(1, amax+1):
        # If 'i' is less than vmin, then there should be no occurrence of 'i' in 'a'.
        # a.count(i) counts how many times 'i' appears in the list 'a'.
        if i < vmin and a.count(i) > 0:
            # If the forbidden value appears, print NO (Impossible), and exit the function immediately.
            print(NO)
            return
        # If 'i' is exactly equal to vmin, the number of appearances of 'i' in 'a' must be exactly nmin (either 1 or 2).
        if i == vmin and a.count(i) != nmin:
            # If vmin appears too many or too few times, print NO and exit early.
            print(NO)
            return
        # If 'i' is greater than vmin, it must appear at least 2 times in 'a'.
        if i > vmin and a.count(i) < 2:
            # If any number above vmin appears less than 2 times, print NO (Impossible) and exit function.
            print(NO)
            return

    # If all checks passed (the function did not return early), then it's valid.
    # Print YES (Possible) as per the problem's requirements.
    print(YES)
    return

def main():
    # This is the main function where the input is read, parsed and sent to the 'solve' function.

    def iterate_tokens():
        # A generator function to break each input line into space-separated tokens (words or numbers).
        # It reads lines from sys.stdin (the standard input), splits each line, and yields each token one at a time.
        for line in sys.stdin:
            # For each line in the input, split into individual words/tokens (by whitespace).
            for word in line.split():
                # Yield each token to the caller. 'yield' is like return but for generators.
                yield word

    # Create a generator instance called 'tokens'.
    tokens = iterate_tokens()

    # Read the first token from the input generator and convert it to an int to get N,
    # which represents the number of elements in the list 'a'.
    N = int(next(tokens))              # type: int

    # Using a list comprehension, read the next N tokens from the input generator,
    # convert each one to int, and collect them into the list 'a'.
    a = [ int(next(tokens)) for _ in range(N) ]   # type: "List[int]"

    # Call the 'solve' function, providing the number of elements and the list as arguments.
    solve(N, a)

# This statement makes sure the main() function is executed only if this script is run as a standalone program.
# If the script is imported as a module, the main() function will not be executed.
if __name__ == '__main__':
    main()