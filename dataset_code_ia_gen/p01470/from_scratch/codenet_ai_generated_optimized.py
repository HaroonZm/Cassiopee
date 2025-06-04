import sys
from fractions import Fraction

input = sys.stdin.readline
N = int(input())
X = Fraction(0, 1)
for _ in range(N):
    o, y = map(int, input().split())
    if o == 1:
        X += y
    elif o == 2:
        X -= y
    elif o == 3:
        X *= y
    else:  # o == 4
        X /= y
print(X.numerator // X.denominator if X.denominator == 1 else X)