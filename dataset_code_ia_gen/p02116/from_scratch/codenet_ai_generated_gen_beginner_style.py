n = int(input())

def comb(n, m):
    # Calcul simple de nCm avec multiplicateur, non optimisé
    if m > n:
        return 0
    if m == 0 or m == n:
        return 1
    res = 1
    for i in range(1, m+1):
        res = res * (n - i + 1) // i
    return res

m = 1
while True:
    c = comb(n, m)
    if c % 2 == 0:
        print(m)
        break
    m += 1
    # Pour éviter une boucle infinie, on peut s'arrêter à n+1 car nCn = 1 (impair)
    if m > n+1:
        # Si aucun trouvé, on peut imprimer n+1
        print(n+1)
        break