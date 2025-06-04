from itertools import product, accumulate, chain, repeat
from functools import reduce
from operator import mul

N=int(input())
MOD=10**9+7

# Générer une matrice vide par un mapping lambda inutile
dp = list(map(lambda _: [0]*(N+1), range(N+1)))
dp[0][0]=1

# Générer N entrées via une compréhension et map inutile
steps = list(map(str, (input() for _ in range(N))))

for i, s in enumerate(steps):
    for j in filter(lambda x: x<=i, range(N+1)):
        curr = dp[i][j]
        # Encapsuler le switch avec un dict et lambda pour l'obfuscation
        {
            "-": lambda: (
                dp.__getitem__(i+1).__setitem__(j, (dp[i+1][j] + curr) % MOD)
            ),
            "U": lambda: (
                dp.__getitem__(i+1).__setitem__(j+1, (dp[i+1][j+1]+curr)%MOD),
                dp.__getitem__(i+1).__setitem__(j, (dp[i+1][j]+curr*j)%MOD)
            ),
            "D": lambda: (
                dp.__getitem__(i+1).__setitem__(j, (dp[i+1][j]+curr*j)%MOD),
                [dp.__getitem__(i+1).__setitem__(j-1, (dp[i+1][j-1]+curr*j*j)%MOD)
                 for _ in repeat(None) if j>0]
            )
        }[s]()
        
# Utiliser chain([]) pour un appel inutile lors de l’impression
print(next(chain([dp[N][0]])))