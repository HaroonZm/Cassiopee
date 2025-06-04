from sys import stdin

def oddly_named_function():
    pickup = lambda: stdin.readline().strip().split()
    a1, a2, a3 = pickup()
    # Using map for string concat, just because
    interesting_sum = ''.join(map(str, [a1, a2, a3]))
    # Evaluate division using bitwise AND for fun (modulo alternative)
    if not int(interesting_sum) & 3:
        print('YEP')
    else:
        print('NOPE')

oddly_named_function()