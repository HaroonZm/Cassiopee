def solve(x, a, ind):
    """
    Evaluates a mathematical expression stored in a 2D grid, starting at a given column index.
    The grid encodes a tree-like expression using '+', '*', digits, and '.' as structure.

    Args:
        x (int): Number of rows in the subgrid to process.
        a (List[str]): The 2D list (list of strings) representing the grid.
        ind (int): Starting column index in the current tree/subtree.

    Returns:
        int: Result of evaluating the subtree/expression rooted at a[0][ind].
    """
    # If the character at the current root is a digit, return its integer value.
    if "0" <= a[0][ind] <= "9":
        return int(a[0][ind])

    # If the current root is the '+' operator, compute the sum of its children sub-expressions
    if a[0][ind] == "+":
        i = j = 1  # Pointers to scan rows for child nodes.
        su = 0     # Initialize sum accumulator.
        while i < x:
            # If we find the start of a new subexpression (indicated by '+' or '*')
            if a[i][ind + 1] == "+" or a[i][ind + 1] == "*":
                j += 1
                # Advance j to the end of this subexpression (denoted by consecutive '.'s)
                while j < x and a[j][ind + 1] == ".":
                    j += 1
                # Recursively evaluate the child subexpression
                su += solve(j - i, a[i:j], ind + 1)
                i = j  # Move to the next potential child node
            else:
                # If it's a digit, accumulate its value directly
                su += int(a[j][ind + 1])
                i += 1
                j += 1
        return su

    # If the current root is the '*' operator, compute the product of its children sub-expressions
    if a[0][ind] == "*":
        i = j = 1  # Pointers as before
        su = 1     # Initialize product accumulator
        while i < x:
            # If we find the start of a new subexpression (next to the current column)
            if a[i][ind + 1] == "+" or a[i][ind + 1] == "*":
                j += 1
                # Advance to end of subexpression
                while j < x and a[j][ind + 1] == ".":
                    j += 1
                # Evaluate recursively and multiply
                su *= solve(j - i, a[i:j], ind + 1)
                i = j
            else:
                # If digit, multiply directly
                su *= int(a[j][ind + 1])
                i += 1
                j += 1
        return su

while True:
    n = int(input())
    if n > 0:
        a = [input() for _ in range(n)]
        print(solve(n, a, 0))
    else:
        break