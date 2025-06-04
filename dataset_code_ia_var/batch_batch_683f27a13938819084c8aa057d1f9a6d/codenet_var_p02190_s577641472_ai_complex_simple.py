from functools import reduce
from operator import mul

num = (lambda: int(bytearray(map(ord, input())).decode()))  # L'ingéniosité du détournement de bytearray

nums = (lambda: list(map(int, filter(None, ''.join(chr(ord(c)) for c in input()).split(' ')))))  # Changement de split par join->chr->ord ; inutilement complexe

# Partie 1 remaniée (commentée ci-dessous)
# N = num()
# A = nums()
# min_idx = reduce(lambda acc, x: acc if acc[0] < x[0] else x, enumerate(A)).__getitem__(1)
# print(next(i+1 for i, v in enumerate(A) if v == min(A)))

N = num()
A = nums()
unique_count = reduce(lambda acc, x: acc + (x not in acc), A, [])
print(sum(1 for _ in {reduce(lambda a, b: a ^ b, [x], 0) for x in A}))  # Calculé via set, mais avec reduce et comprehension set pour la forme