def two_int():
    """
    Reads two integers from a single input line separated by space.

    Returns:
        tuple: A tuple containing two integers (N, K).
    """
    N, K = map(int, input().split())
    return N, K

def one_int():
    """
    Reads a single integer from input.

    Returns:
        int: The integer read from input.
    """
    return int(input())

def one_str():
    """
    Reads a single line of string from input.

    Returns:
        str: The string read from input.
    """
    return input()

def many_int():
    """
    Reads a line of input, splits it by spaces, and converts each part to an integer.

    Returns:
        list: A list of integers parsed from the input.
    """
    return list(map(int, input().split()))

# Read two integers (A and B) from input. This will define the phone number's two segments' lengths.
A, B = many_int()

# Read the string S, which should represent the phone number.
S = one_str()

# Initialize flag to determine if S matches the specified phone number format.
flg = False

# Check if the character at position A is a dash '-'
if S[A] == "-":
    # Remove the dash at position A and check the rest are all digits, and length matches A+B+1
    temp = S[:A] + S[A+1:]
    if temp.isdecimal() and len(S) == A + B + 1:
        flg = True

# Output the result based on the flag.
if flg:
    print("Yes")
else:
    print("No")