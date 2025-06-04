def main():
    """
    Main function to read input, process calculations, and output the final result.
    The program performs a special summation over a list of integers, applying a
    modular arithmetic operation at each step.
    """
    # Read an integer N from input, representing the number of elements.
    N = int(input())

    # Read a list of N integers from input, representing the sequence X.
    X = list(map(int, input().split()))

    # Initialize the answer accumulator to zero.
    ans = 0

    # Define the modulus value for all modular arithmetic operations.
    mod = 998244353

    # Iterate over each value x in X along with its index i.
    for i, x in enumerate(X):
        # For each element, update 'ans' with the formula:
        # ans = (ans * 2 + x * (x + 1) ** i mod mod) mod mod
        # - ans is doubled at each step.
        # - pow(x + 1, i, mod) efficiently computes (x + 1) to the power i modulo mod.
        # - The new value is added, and the sum is reduced modulo 'mod'.
        ans = (ans * 2 + x * pow(x + 1, i, mod)) % mod

    # Output the final result.
    print(ans)

if __name__ == "__main__":
    main()