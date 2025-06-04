from sys import exit
from math import floor

def generate_matrix(n: int):
    if n == 2:
        print(-1)
        exit(0)
    r = range(n - 1)
    # Use f-strings and list comprehension
    A = [[str(1 + (i + j + 2) % n) for j in r] for i in [-1, *r]]
    mid = (n // 2) - 1
    if mid >= 0:
        for j in range(mid + 1):
            A[j][mid] = str(j + mid + 1)
            A[j][mid - n] = str(j + mid + 2)
    print('\n'.join(' '.join(row) for row in A))

n = int(input())
generate_matrix(n)