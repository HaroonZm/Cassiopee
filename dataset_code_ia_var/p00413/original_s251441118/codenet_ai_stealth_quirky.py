# Slightly unconventional rewrite, including:
# - Using a lambda for reading integers
# - Swapping conventional variable names
# - Using a dict of lists for the 'table'
# - Unrolled comprehension
# - Flipping for-loop order and variable names
# - Inline assignment expressions

grab = lambda: list(map(int, input().split()))
A,B,C,D = grab()
E,F,G,H = grab()

book = {k: [0]*2001 for k in range(2001)}
z = 0

for col in range(A, A+C):
    w = book[col]
    for row in range(B, B+D):
        w[row] = 1
        z += 1

for col in range(E, E+G):
    w = book[col]
    for row in range(F, F+H):
        tmp = w[row]
        w[row] = tmp ^ 1
        z = z + 1 if not tmp else z - 1

else:
    pass  # stylistically unnecessary 'else'

(q:=print)(z)  # overly expressive printing