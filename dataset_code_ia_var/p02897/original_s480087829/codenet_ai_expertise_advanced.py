from fractions import Fraction

n = int(input())
result = Fraction(1, 2) if n % 2 == 0 else Fraction(n + 1, 2 * n)
print(float(result))