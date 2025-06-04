import sys
from functools import lru_cache

# Define the modulus to be used for all modular arithmetic operations
mod = 10 ** 9 + 7

def iim():
    """
    Reads a line from standard input, strips whitespace, and returns a map object
    of the line split into integer values.
    """
    return map(int, sys.stdin.readline().rstrip().split())

@lru_cache(maxsize=100)
def calc(n):
    """
    Computes a complicated combinatorial polynomial expression modulo mod.
    The value of m is computed as (n-5)//2, and multiple high-degree polynomial expressions
    of m and n are combined according to a specific formula.
    
    The result is returned as an integer modulo mod.

    Args:
        n (int): Input integer value for which the function is evaluated.

    Returns:
        int: The computed result modulo mod.
    """
    # Calculate m as per the provided formula
    m = (n - 5) // 2

    # The result is the product of several polynomial expressions of m and n
    # All calculations are performed modulo mod to prevent integer overflow
    result = (
        (1 + m) * (2 + m) * (3 + m) % mod
        * (4 + m) * (5 + m) % mod
        * (
            1025024 * pow(m, 10, mod)
            + 3003 * (-4 + n) % mod * (-3 + n) * (-2 + n) % mod * (-1 + n) * n * (1 + n) % mod
            * (2 + n) * (3 + n) % mod * (4 + n) * (5 + n) % mod
            - 549120 * pow(m, 9, mod) * (-1 + 10 * n) % mod
            + 42240 * pow(m, 8, mod) * (-398 + 45 * n * (-1 + 7 * n)) % mod
            - 369600 * pow(m, 7, mod) * (3 + 2 * (-2 + n) * n * (49 + 26 * n) % mod) % mod
            + 2688 * pow(m, 6, mod) * (33529 + 75 * n * (-33 - 679 * n + 91 * n ** 3) % mod) % mod
            - 336 * pow(m, 5, mod) * (
                88065 + 2 * n * (426107 + 7 * n * (-6675 + 13 * n * (-2420 + 9 * n * (5 + 22 * n) % mod)) % mod)
            ) % mod
            + 560 * pow(m, 4, mod) * (
                -291598 + n * (216249 + 7 * n * (95465 + 26 * n * (-495 + n * (-980 + 11 * n * (3 + 5 * n)) % mod) % mod) % mod)
            ) % mod
            - 30 * pow(m, 3, mod) * (
                -3080960 + n * (
                    -10447602 + 7 * n * (
                        854525 + 13 * n * (93170 + n * (-15295 + 22 * n * (-714 + 5 * n * (7 + 6 * n) % mod) % mod) % mod) % mod
                    ) % mod
                )
            ) % mod
            + 2 * pow(m, 2, mod) * (
                28412712 + 25 * n * (
                    -3433650 + n * (
                        -4123841 + 13 * n * (
                            189882 + n * (
                                142177 + 22 * n * (-1344 + n * (-791 + 27 * n * (2 + n) % mod) % mod)
                            ) % mod
                        ) % mod
                    ) % mod
                )
            ) % mod
            - m * (
                30149280 + n * (
                    31294296 + n * (
                        -93275400 + 13 * n * (
                            -3808420 + n * (
                                2988195 + 11 * n * (
                                    111678 + 25 * n * (-1302 + n * (-456 + n * (45 + 14 * n) % mod) % mod
                                ) % mod
                                ) % mod
                            ) % mod
                        ) % mod
                    ) % mod
                )
            ) % mod
        ) % mod
        * pow(1307674368000 % mod, mod - 2, mod) % mod  # Modular inverse, for division
    )
    return result

def resolve():
    """
    Main function that reads input from stdin, computes results for N input values using calc,
    and outputs the results--one per line.
    """
    # Read all integers from standard input
    it = map(int, sys.stdin.read().split())
    # The first integer indicates the number of test cases
    N = next(it)

    # Prepare the answer list of the appropriate size
    ans = [0] * N

    # For each test case, read the integer n and compute calc(n)
    for i in range(N):
        n = next(it)
        ans[i] = calc(n)

    # Print each answer on a new line
    print(*ans, sep="\n")

if __name__ == "__main__":
    # Entry point of the script
    resolve()