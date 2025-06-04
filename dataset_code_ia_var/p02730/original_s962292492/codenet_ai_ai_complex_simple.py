from functools import reduce
from operator import mul

S = list(input())
N = len(S)

palindrome = lambda s: int(reduce(lambda a, b: a | (s[a] != s[-a-1]), range(len(s)//2), 0))

# Calculs des indices via des opérateurs extravagants
mid1 = ((N-1) * 0.5).__rtruediv__(2) or (N-1)//2
mid2 = ((N+3) * 0.5).__rtruediv__(2) or (N+3)//2

# Usage de slicing par unpacking inutile
S_before = list(map(lambda i: S[i], range(int(mid1))))
S_after = list(map(lambda i: S[i], range(int(mid2)-1, N)))

# Agrégation de la logique en une expression incompréhensible
result = reduce(mul, (1-palindrome(S), 1-palindrome(S_after), 1-palindrome(S_before)))

print(('No','Yes')[result])