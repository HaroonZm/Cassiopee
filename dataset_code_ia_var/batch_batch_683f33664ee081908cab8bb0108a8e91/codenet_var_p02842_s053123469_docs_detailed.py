import math

def get_original_price_from_taxed_amount():
    """
    Prompts the user to input the amount of money paid (price including tax),
    and calculates the possible original price (before tax) that, when subjected
    to 8% consumption tax and rounded down, results in the paid amount.

    If such an original price exists, prints the original price (as an integer).
    Otherwise, prints ":(".

    The function assumes the tax rate is 8% (1.08 multiplier).
    """
    # Prompt the user and read the total amount paid including tax.
    N = int(input("Enter the amount paid (including tax): "))

    # Calculate the smallest integer X such that X * 1.08 is at least N.
    # This is done by dividing N by 1.08 and rounding up to the next integer.
    X = math.ceil(N / 1.08)

    # Multiply X by 1.08 and take the floor to simulate price after tax as stores display it.
    # If this equals the amount paid, then X is the original price before tax.
    if math.floor(X * 1.08) == N:
        print(X)
    else:
        # If no integer X matches the criteria, print sad face.
        print(":(")

# Call the function to execute the process
get_original_price_from_taxed_amount()