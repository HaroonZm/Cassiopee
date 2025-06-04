# Solution Python complète pour vérifier le théorème de Chebyshev
# Le programme lit des entiers n jusqu'à ce qu'il rencontre un zéro,
# puis pour chaque n, il compte le nombre de nombres premiers p
# tels que n < p <= 2n, et affiche ce nombre.

import sys

def sieve(max_limit):
    """
    Génère une liste de booléens indiquant si un nombre est premier jusqu'à max_limit inclus.
    Utilise le crible d'Ératosthène pour une efficacité optimale.
    """
    sieve = [True] * (max_limit + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(max_limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_limit + 1, i):
                sieve[j] = False
    return sieve

def main():
    # Pour répondre au problème, le maximum 2*n peut être jusqu'à 2*123456 = 246912
    MAX_N = 246912

    # Pré-calcul des nombres premiers jusqu'à 2*123456 avec le crible d'Ératosthène
    primes = sieve(MAX_N)

    for line in sys.stdin:
        n = line.strip()
        if n == '0':
            # Fin de la lecture de données
            break
        n = int(n)
        # Compter le nombre de premiers p tels que n < p <= 2n
        count = 0
        for p in range(n+1, 2*n + 1):
            if primes[p]:
                count += 1
        print(count)

if __name__ == "__main__":
    main()