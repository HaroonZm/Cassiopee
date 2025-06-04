N = 0
def check_palindrome(x):return x==x[::-1]
from sys import stdin
_lines = iter(stdin.readline, '')
for S in _lines:
  S = S.rstrip('\n')
  N = N + 1*check_palindrome(S)
print ([N][0])