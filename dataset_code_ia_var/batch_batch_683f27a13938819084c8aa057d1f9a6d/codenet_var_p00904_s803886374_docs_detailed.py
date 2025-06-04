def main():
    """
    Main function to process multiple test cases.

    For each test case, reads two integers p and q, counts the number of integer pairs (i, j) in range(143)
    (excluding the (0, 0) pair) where both (j*p + i*q) and (j*q - i*p) are divisible by (j*j + i*i).
    If the count 'c' is less than 5, prints 'P', otherwise prints 'C'.
    """
    for _ in range(int(input())):
        p, q = map(int, input().split())
        c = count_divisible_pairs(p, q)
        if c < 5:
            print('P')
        else:
            print('C')

def count_divisible_pairs(p, q):
    """
    Counts the number of integer pairs (i, j) with 0 <= i < 143 and 0 <= j < 143,
    (i, j) ≠ (0, 0), such that both (j*p + i*q) and (j*q - i*p) are divisible by (j*j + i*i).

    Args:
        p (int): The first integer parameter.
        q (int): The second integer parameter.

    Returns:
        int: The number of valid pairs (i, j) satisfying the divisibility conditions.
    """
    c = 0  # Initialize counter
    for i in range(143):
        for j in range(143):
            # Exclude the (0, 0) pair
            if i > 0 or j > 0:
                denominator = j * j + i * i
                numerator1 = j * p + i * q
                numerator2 = j * q - i * p
                # Check divisibility for both numerators with denominator
                if numerator1 % denominator == 0 and numerator2 % denominator == 0:
                    c += 1
    return c

if __name__ == "__main__":
    main()