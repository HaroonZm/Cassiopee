"""
Module to evaluate boolean expressions involving bitwise operations on 4-digit binary numbers.
Supports custom operators: + (OR), * (AND), ^ (XOR), and square brackets for grouping.
Reads expressions and numbers from standard input, prints the result and uniqueness count.
"""

import sys
import functools

# Determine the correct maketrans() function based on Python version
if sys.version_info[0] >= 3:
    maketrans = str.maketrans
else:
    from string import maketrans

def bitwise_or(a):
    """
    Returns a function that computes the bitwise OR of 'a' and another number 'b'.
    Args:
        a (int): First operand.
    Returns:
        function: Function taking one argument (b) and returning a | b.
    """
    return lambda b: a | b

def bitwise_and(a):
    """
    Returns a function that computes the bitwise AND of 'a' and another number 'b'.
    Args:
        a (int): First operand.
    Returns:
        function: Function taking one argument (b) and returning a & b.
    """
    return lambda b: a & b

def bitwise_xor(a):
    """
    Returns a function that computes the bitwise XOR of 'a' and another number 'b'.
    Args:
        a (int): First operand.
    Returns:
        function: Function taking one argument (b) and returning a ^ b.
    """
    return lambda b: a ^ b

def replace_operators(expr):
    """
    Replaces custom operator symbols in the expression with their corresponding function names and Python syntax.
    Args:
        expr (str): The string expression to translate.
    Returns:
        str: The translated expression.
    """
    # Replace: + -> O, * -> A, ^ -> X, [ -> (, ] -> )
    return expr.translate(maketrans('+*^[]', 'OAX()'))

def expand_variables(expr):
    """
    Encloses each variable (a, b, c, d) in parentheses for safe evaluation.
    Args:
        expr (str): Expression string.
    Returns:
        str: Expression with variables enclosed in parentheses.
    """
    for var in 'abcd':
        expr = expr.replace(var, '(%s)' % var)
    return expr

def substitute_variables(expr, n):
    """
    Replaces the variable names (a, b, c, d) in the expression with corresponding digits from the integer n.
    Args:
        expr (str): The expression with variables.
        n (int): A 4-digit integer whose digits represent the values of a, b, c, d.
    Returns:
        str: Expression with variables replaced by digits.
    """
    # Convert n to a zero-padded 4-digit string
    values = '%04d' % n
    return expr.translate(maketrans('abcd', values))

def process_expression(expr, n):
    """
    Evaluates the translated expression for a particular 4-digit number n.
    Args:
        expr (str): The Python-translatable expression.
        n (int): A 4-digit integer.
    Returns:
        int: Result of evaluating the boolean expression with n substituted for a, b, c, d.
    """
    evaluated_expr = substitute_variables(expr, n)
    return eval(evaluated_expr)

def count_uniqueness(expr, target_result):
    """
    Counts in how many 4-digit combinations the expression evaluates to the same result as target_result.
    Args:
        expr (str): The Python-translatable expression.
        target_result (int): The result to compare against.
    Returns:
        int: Number of 4-digit integers for which the expression evaluates to target_result.
    """
    count = 0
    for i in range(10000):  # All values from 0000 to 9999
        if eval(substitute_variables(expr, i)) == target_result:
            count += 1
    return count

def main():
    """
    Main loop to read expressions and numbers from standard input, process, and print results.
    """
    # Define function aliases matching the transformed operator names
    O = bitwise_or
    A = bitwise_and
    X = bitwise_xor

    while True:
        # Read an expression line, process and translate it
        s = sys.stdin.readline().rstrip()
        s_translated = replace_operators(s)
        
        # Break if we reach end marker '.'
        if s_translated == '.':
            break

        # Expand variables to ensure evaluation order
        s_vars = expand_variables(s_translated)
        
        # Remove the outermost parentheses (for the full expr)
        s_expr = s_vars[1:-1]

        # Read the number N to be used for this expression
        n_line = sys.stdin.readline()
        n = int(n_line)

        # Evaluate the result for n
        r = process_expression(s_expr, n)

        # Count how many other 4-digit numbers yield the exact same result
        uniqueness_count = sum(
            r == process_expression(s_expr, i)
            for i in range(10000)
        )
        print('%d %d' % (r, uniqueness_count))

# Invoke main function when the script is executed
if __name__ == '__main__':
    main()