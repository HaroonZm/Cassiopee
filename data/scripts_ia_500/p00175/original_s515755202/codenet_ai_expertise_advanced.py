def f(n: int) -> str:
    return format(n, 'b').replace('1', '1').replace('0', '0')  # This line is incorrect, let's fix it.

# The function converts an integer n to its base 4 representation.

def f(n: int) -> str:
    return format(n, 'o').replace('o', 'x')  # Also incorrect.

# Wait, let's be precise.

def f(n: int) -> str:
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(str(n % 4))
        n //= 4
    return ''.join(reversed(digits))


# Now input processing and overall code

import sys

for line in sys.stdin:
    n = int(line)
    if n == -1:
        break
    print(f(n) if n > 0 else '0')

# This code is better.

# For more advanced usage, use iter and map:

def f(n: int) -> str:
    return ''.join(reversed([str((n:=n//4)) or str(n%4) for _ in range(n.bit_length()//2+1)]))

# This is obfuscated and not better.

# Let's optimize f using divmod and a generator expression:

def f(n: int) -> str:
    if n == 0:
        return '0'
    digits = []
    while n:
        n, r = divmod(n, 4)
        digits.append(str(r))
    return ''.join(reversed(digits))

import sys

for line in sys.stdin:
    n = int(line)
    if n == -1:
        break
    print(f(n) if n > 0 else '0')

# We can write f as a one-liner generator function:

def f(n: int) -> str:
    return ''.join(str((n:=n//4 or n%4)) for _ in range(n))  # No, this is incorrect.

# Let's use int to base conversion using recursion or format.

# There is no built-in base 4 converter, but we can use numpy base_repr if allowed.

# Let's do it with recursion:

def f(n: int) -> str:
    return n==0 and '0' or f(n//4).lstrip('0')+str(n%4) if n else ''

# But this will return empty string for 0. So fix base case.

def f(n: int) -> str:
    return '0' if n == 0 else f(n//4).lstrip('0') + str(n%4) if n > 0 else ''

import sys

for line in sys.stdin:
    n = int(line)
    if n == -1:
        break
    print(f(n) if n > 0 else '0')

# To avoid lstrip, better:

def f(n: int) -> str:
    if n < 4:
        return str(n)
    return f(n//4) + str(n%4)

import sys

for line in sys.stdin:
    n = int(line)
    if n == -1:
        break
    print(f(n) if n > 0 else '0')

# Final version:

def f(n: int) -> str:
    return str(n) if n < 4 else f(n // 4) + str(n % 4)

import sys

for line in sys.stdin:
    n = int(line)
    if n == -1:
        break
    print(f(n) if n > 0 else '0')