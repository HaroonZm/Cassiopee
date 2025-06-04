from math import factorial
from collections import Counter

S = input().strip()
freq = Counter(S)
n = len(S)

# Vérification des conditions nécessaires à l'existence d'un palindrome
odd_count = sum(1 for v in freq.values() if v % 2 != 0)
if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count != 1):
    print(0)
    exit()

# Calcul du nombre de palindromes anagrammes
half_len = n // 2
half_freq = {c: v // 2 for c, v in freq.items()}

numerator = factorial(half_len)
denominator = 1
for v in half_freq.values():
    denominator *= factorial(v)

print(numerator // denominator)