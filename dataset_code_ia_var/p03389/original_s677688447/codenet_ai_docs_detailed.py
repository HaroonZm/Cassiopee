def main():
    """
    Main function to read three integers from input, sort them in ascending order,
    assign to variables a, b, c, and then apply the logic to print the calculated output
    based on the relationship between the numbers.
    """
    # Read a line of input, split it by spaces, convert each item to an integer, and store in a list
    abc = [int(i) for i in input().split(" ")]

    # Sort the list in ascending order so that a <= b <= c
    abc = sorted(abc)

    # Assign the sorted values to variables a, b, c
    a, b, c = abc[0], abc[1], abc[2]

    # Check if a and b are equal
    if a == b:
        # If a and b are equal, the answer is c - a
        print(str(c - a))
    else:
        # If a and b are not equal
        if (a - b) % 2 == 0:
            # Check if the difference (a - b) is even
            # The answer is (b - a) / 2 + (c - b)
            # (b - a) is always >= 0 because a <= b
            print(str(int((b - a) / 2 + c - b)))
        else:
            # If the difference is odd,
            # The answer involves rounding up ((b - a - 1) / 2 + 1) + (c + 1 - b)
            print(str(int((b - a - 1) / 2 + 1 + c + 1 - b)))


if __name__ == "__main__":
    main()