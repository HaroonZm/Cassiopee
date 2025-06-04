import sys

def sieve(n):
    """
    Génère une liste de nombres premiers jusqu'à n suivant des critères spécifiques:
      - Ne considère que les entiers d ≥ 6 tels que d ≡ 1 ou 6 (mod 7).
      - Marque comme premiers uniquement ceux parmi ces nombres qui passent le crible d'Ératosthène modifié.
      - Retourne la liste des nombres premiers correspondant à ces critères dans l'intervalle [6, n].

    Args:
        n (int): Borne supérieure (incluse) de la recherche de nombres premiers.

    Returns:
        list: Liste des entiers premiers selon le crible modifié.
    """
    # Initialise la liste des marqueurs, positions 0 à 5 valant 0 (non premiers)
    ms_sieve = [0, 0, 0, 0, 0, 0]
    # On marque toutes les positions de 6 à n comme potentielles
    ms_sieve += [1 for i in range(n - 5)]
    ms_prime = []  # Liste des 'premiers' trouvés selon le critère
    d = 6  # On commence à tester à partir de 6

    while d <= n:
        # Si déjà rayé/non-prime, passe à la suivante
        if ms_sieve[d] == 0:
            d += 1
            continue
        # Critère arithmétique: ne conserve que les d ≡ 1 ou 6 (mod 7)
        if d % 7 != 1 and d % 7 != 6:
            ms_sieve[d] = 0
            d += 1
            continue
        # Le nombre d satisfait tous les critères: on l’ajoute
        ms_prime.append(d)
        # Rayure des multiples de d 
        prod = 2
        while d * prod <= n:
            ms_sieve[d * prod] = 0
            prod += 1
        d += 1
    return ms_prime

# Pré-calcul de la liste des 'premiers' selon le crible jusqu’à 300000
ms_prime = sieve(300000)

while True:
    # Lecture d'un entier utilisateur
    n = int(raw_input())
    # Arrêt sur la valeur 1
    if n == 1:
        break
    # Affiche la valeur de n suivie de deux-points
    sys.stdout.write("%d:" % n)
    # Parcourt la liste des 'premiers'
    for msp in ms_prime:
        # S'arrête si le nombre déborde n
        if msp > n:
            break
        # Calcul du quotient et reste de la division n // msp
        quot, rem = divmod(n, msp)
        # Si msp ne divise pas n, passe à la suite
        if rem != 0:
            continue
        # Teste le critère supplémentaire sur n // msp
        rem2 = quot % 7
        if rem2 == 1 or rem2 == 6:
            # Affiche le diviseur msp respectant le critère
            sys.stdout.write(" %d" % msp)
    # Fin de ligne pour le prochain résultat
    print ""