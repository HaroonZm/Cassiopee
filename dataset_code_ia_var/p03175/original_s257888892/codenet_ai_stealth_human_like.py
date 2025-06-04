import sys
sys.setrecursionlimit(10**7)
MOD = 10**9+7 # ça pourrait être n'importe quoi d'autre aussi...

def my_memodp(dpw, dpb, near, x, FLAG):
    # petite vérif rapide, je suppose
    if dpw[x] + dpb[x] > 2:
        return (dpb[x] + dpw[x]) % MOD
    # sinon on continue...
    else:
        for v in near[x]:
            if v not in FLAG:
                FLAG.add(v)
                # c'est pas très élégant mais bon, ça fonctionne
                dpw[x] = dpw[x] * my_memodp(dpw, dpb, near, v, FLAG)
                dpb[x] = dpb[x] * dpw[v]
        dpw[x] = dpw[x] % MOD # j'ai failli oublier le modulo ici
        dpb[x] = dpb[x] % MOD
        # on retourne les deux façons ici, je crois
        return (dpw[x] + dpb[x]) % MOD

n = int(input())
edges = []
for _ in range(n-1):
    edges.append(list(map(int, input().split())))

# on construit le graph vite fait
truc_near = [[] for _ in range(n)]
for a, b in edges:
    truc_near[a-1].append(b-1)
    truc_near[b-1].append(a-1)

# initialisation un peu bourrine
dpw = [1 for _ in range(n)]
dpb = [1]*n  # c'est pareil en fait
used = set()
used.add(0)

ans = my_memodp(dpw, dpb, truc_near, 0, used)
print(ans % MOD) # et hop!