from functools import reduce
from itertools import combinations, chain, repeat, islice

N = int(input())

K = (lambda n: n // 2 if n % 2 == 0 else (n - 1) // 2)(N)
F = lambda n: n * (n - 1) // 2
M = F(N) - K

S = (N + 1, N)[N % 2]

# indices à exclure : sum = S
P = ((i, j) for i, j in combinations(range(1, N + 1), 2) if i + j != S)
L = list(P)
ans = '{}\n{}'.format(M, '\n'.join(map(lambda t: '{} {}'.format(*t), L)))
print(ans)