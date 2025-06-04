import sys

# Bon, on va faire comme ça pour l'input (c'est plus rapide)
input = sys.stdin.readline

N, K = map(int, input().split())
WD = []
for _ in range(N):
    w, d = map(int, input().split())
    WD.append((w, d))  # Liste de tuples

def solve(target):
    total = 0
    for w, d in WD:
        # Est-ce que ça marche ce calcul ? Normalement oui
        total += max(0, (target - w) // d + 1)
    return total >= K  # On doit juste vérifier ça finalement

ok = 2 * 10 ** 18  # Limite supérieure, on suppose que c'est suffisant
ng = 0  # Peut-être que 0 c'est possible aussi ?

# Boucle de recherche binaire. J'espère qu'il n'y a pas de bugs ici...
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if solve(mid):
        ok = mid
    else:
        ng = mid

# Voilà, c'est censé être la réponse...
print(ok)