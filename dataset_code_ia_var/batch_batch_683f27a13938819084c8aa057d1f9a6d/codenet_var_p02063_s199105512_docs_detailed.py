def main():
    """
    Main function to process two integers from input and determine a specific value or output -1.

    The function reads two integers, `a` and `b`, from standard input, then computes two possible
    values based on formulas involving integer division and maximum selection:
      - val1 = (b - 1 + a - 2) // (a - 1)
      - val2 = (b + a - 1) // a

    It compares the larger of these to (a + b) / a. If the maximum value is less than this, it prints
    the product of that maximum value and `a`, otherwise it prints -1.
    """
    # Read two integers from input, separated by spaces
    a, b = map(int, input().split())

    # Calculate integer divisions according to the problem's formulae
    # val1: represents the minimum k such that (k-1)*(a-1)+1 >= b
    val1 = (b - 1 + a - 2) // (a - 1)
    # val2: represents the minimum k such that a*k >= a+b-1
    val2 = (b + a - 1) // a

    # Select the maximum of the two computed integer division results
    k = max(val1, val2)

    # Compute the threshold for comparison: (a + b) / a (floating point)
    threshold = (a + b) / a

    # If k is less than the threshold, output the product k*a; otherwise, output -1
    if k < threshold:
        print(k * a)
    else:
        print(-1)

if __name__ == '__main__':
    main()