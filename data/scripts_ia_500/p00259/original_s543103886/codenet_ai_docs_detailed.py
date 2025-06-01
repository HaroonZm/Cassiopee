import re

# Initialize the modulus variable p to zero
p = 0

class N(int):
    """
    A subclass of int that implements arithmetic modulo p.
    All operations (+, -, *, //) are performed modulo p.
    """
    def __add__(self, n):
        """
        Perform addition modulo p.
        
        Args:
            n (int or N): The number to add.
        
        Returns:
            N: The result of (self + n) mod p as an N instance.
        """
        return N((int(self) + int(n)) % p)

    def __sub__(self, n):
        """
        Perform subtraction modulo p.
        
        Args:
            n (int or N): The number to subtract.
        
        Returns:
            N: The result of (self - n) mod p as an N instance.
        """
        return N((int(self) - int(n)) % p)

    def __mul__(self, n):
        """
        Perform multiplication modulo p.
        
        Args:
            n (int or N): The number to multiply.
        
        Returns:
            N: The result of (self * n) mod p as an N instance.
        """
        return N((int(self) * int(n)) % p)

    def __floordiv__(self, n):
        """
        Perform modular division (integer division) modulo p.
        Division is computed using modular inverse based on Fermat's little theorem:
        a / b ≡ a * b^(p-2) (mod p), assuming p is prime.
        
        Args:
            n (int or N): The divisor.
        
        Returns:
            N: The result of (self / n) mod p as an N instance.
        
        Raises:
            ZeroDivisionError: If n is zero.
        """
        if not n:
            raise ZeroDivisionError("Division by zero is undefined.")
        # Compute modular inverse of n using pow with modulus p
        inverse = pow(int(n), p - 2, p)
        return self * inverse

# Main input-processing loop
while True:
    s = input()  # Read a line from standard input
    p, s = s.split(':')  # Split input at the ':' character into modulus and expression
    p = int(p)  # Convert modulus string to integer
    
    # If modulus is zero, terminate the loop/program
    if not p:
        break
    
    s = s.replace(' ', '')  # Remove all spaces from the expression string to simplify parsing
    
    try:
        # Replace all integers in the expression with N(integer) to enable modular arithmetic
        # Also replace '/' with '//' to enforce integer division in Python syntax
        expr = re.sub(r'(\d+)', r'N(\1)', s).replace('/', '//')
        
        # Evaluate the expression using Python's eval in the current context, where N and p are defined
        n = eval(expr)
        
        # Print the original expression, its computed value modulo p, and the modulus
        print(f'{s} = {n} (mod {p})')
    except ZeroDivisionError:
        # Handle division by zero errors and print "NG" indicating an invalid operation
        print('NG')