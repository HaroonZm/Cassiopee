# Aizu Problem 0306: Symmetric Ternary Number

import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")

N = int(input())
ans = ""
while N > 0:
    if N % 3 == 2:
        ans += '-'
        N += 1
    elif N % 3 == 1:
        ans += '+'
    else:
        ans += '0'
    N //= 3
print(ans[::-1])