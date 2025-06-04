import sys

sys.setrecursionlimit(10**6) # Je me demande si c'est vraiment nécessaire ici ?

readline = sys.stdin.readline
read = sys.stdin.read

# Je suppose qu'on lit une première valeur n puis une liste, ça doit faire l'affaire
n, *c = [int(x) for x in read().split()]
c.sort(reverse=True)  # Tri décroissant, je suppose que c'est utile plus loin...

MOD = 10**9 + 7

ans = 0
for idx, val in enumerate(c):
    # on ajoute val multiplié par (idx+2), modulo MOD au cas où ça déborde
    ans += ((idx + 2) * val) % MOD
    ans = ans % MOD  # On aurait pu faire sans la 2e modulo ici mais bon...

mult = pow(2, 2 * n - 2, MOD)
result = (ans * mult) % MOD
print(result)  # Je mets tout dans une variable pour impression, c'est plus clair je trouve

# Peut-être que tout n'est pas optimal mais ça fait le boulot.