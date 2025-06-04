from string import digits, ascii_uppercase

def parse(S):
    """
    Parse a string representation of an encoded sequence, supporting repetition and grouping, 
    and build an abstract syntax tree (AST) and the length of the fully-decoded sequence.

    The supported encoding consists of:
    - Repetitions: "2A" means 'A' repeated twice
    - Grouping: "3(AB)" means 'AB' is repeated 3 times

    Args:
        S (str): The encoding string to parse

    Returns:
        tuple: (AST representation of the sequence, total decoded length)
    """
    S += "$"  # Sentinel character to avoid index errors during parsing
    cur = 0   # Current cursor position in string

    def expr():
        """
        Parses a sequence expression, recursively handling repetitions and groups.

        Returns:
            tuple: (AST of parsed sequence, length of decoded sequence)
        """
        nonlocal cur
        R = []  # Holds parsed sequence AST elements
        l = 0   # Holds total decoded length for current expression

        while True:
            c = S[cur]  # Current character
            if c in digits:
                v = number()  # Repetition count
                if S[cur] == '(':  # Indicates repetition of a group
                    cur += 1  # Skip '('
                    R0, l0 = expr()  # Parse group recursively
                    cur += 1  # Skip ')'
                    l += v * l0
                    R.append((v, l0, R0))  # Store as tuple: (repeat count, length, AST of group)
                else:
                    # It's repetition of a single character (e.g., "2A")
                    c = S[cur]
                    cur += 1  # Advance over the character
                    l += v
                    R.append((v, 1, [c]))  # Store as a group for consistency
            elif c in ascii_uppercase:
                # A bare character with implicit repeat of 1
                cur += 1  # Advance over the character
                l += 1
                R.append(c)  # Store as a bare character
            else:
                # Non-recognized character, end of this expr
                break
        return R, l

    def number():
        """
        Parses a multi-digit number from the input string.

        Returns:
            int: The parsed integer value
        """
        nonlocal cur
        v = 0
        while True:
            c = S[cur]
            if c not in digits:
                break
            v = 10 * v + int(c)
            cur += 1  # Move to next character
        return v

    R, l = expr()
    return R, l

def solve(res, x):
    """
    Recursively finds the character at position x in the fully-decoded sequence represented by the AST.

    Args:
        res (tuple): (AST of sequence, total decoded length)
        x (int): The position (0-based) to retrieve

    Returns:
        str: The character at position x, or "0" if x is out of bounds
    """
    R, l = res
    if l <= x:
        return "0"  # Out of bounds
    cur = R
    while True:
        for data in cur:
            if isinstance(data, str):
                # It's a bare character
                if x == 0:
                    return data
                x -= 1
            else:
                v, l_inner, R_inner = data  # Unpack group
                if x < v * l_inner:
                    # Position falls into this group; descend recursively
                    cur = R_inner
                    x %= l_inner
                    break
                x -= v * l_inner

# Main interaction loop
while True:
    S, x = input().split()
    if S == "0":
        break  # End of processing
    x = int(x)
    R, l = res = parse(S)  # Parse input string and get AST and total length
    if l <= x:
        print("0")  # Out of bounds
        continue
    print(solve(res, x))