from functools import reduce
from itertools import product, starmap
from operator import add, mul

n = int(input())
c = list(map(str, (lambda x: [input() for _ in range(x)])(n)))
MOD = 10 ** 9 + 7

# Création maligne avec une lambda et map
dp = list(map(lambda _: [0] * (n + 1), range(n + 1)))
dp[0][0] = 1

def touch(i, j, x):
    dp[i][j] = (dp[i][j] + x) % MOD

for i, ch in enumerate(c):
    # On fait tous les j d'avance
    current = dp[i][:]
    for j in range(n + 1):
        # Traitement élégant avec dict qui mappe les opérations
        ops = {
            "-": lambda: touch(i + 1, j + 1, current[j]) if j + 1 < n + 1 else None,
            "U": lambda: [touch(i + 1, j, current[j]), touch(i + 1, j + 1, current[j] * (i - j)) if j + 1 < n + 1 else None],
            "D": lambda: [touch(i + 1, j + 1, current[j] * (i - j)) if j + 1 < n + 1 else None, touch(i + 1, j + 2, current[j] * (i - j) ** 2) if j + 2 < n + 1 else None]
        }
        _ = ops.get(ch, lambda: None)()
        
# Extraction du résultat version complexe
result = reduce(lambda x, _: x, map(lambda _: dp[-1][-1], range(1)), 0) or dp[-1][-1]
print(result)