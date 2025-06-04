# Solution complète en Python pour le problème "Pair of Primes"
# L'approche consiste à:
# 1. Lire chaque valeur N donnée en entrée jusqu'à la fin des données.
# 2. Identifier les nombres premiers entre 1 et N en utilisant le crible d'Ératosthène pour une efficacité optimale.
# 3. Pour chaque i de 1 à N, on forme une paire (i, N-i+1).
# 4. On compte combien de ces paires sont composées de deux nombres premiers.
# 5. On affiche le résultat pour chaque N.

import sys

def sieve(max_n):
    """
    Crée un tableau de booléens indiquant si chaque nombre de 0 à max_n est premier.
    Utilise le crible d'Ératosthène.
    """
    is_prime = [True] * (max_n + 1)
    is_prime[0], is_prime[1] = False, False  # 0 et 1 ne sont pas premiers
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_n + 1, i):
                is_prime[j] = False
    return is_prime

def count_prime_pairs(n, is_prime):
    """
    Compte le nombre de paires (i, n - i + 1) où i et n - i + 1 sont premiers.
    """
    count = 0
    for i in range(1, n+1):
        j = n - i + 1
        # Vérifier que les deux nombres dans la paire sont premiers
        if is_prime[i] and is_prime[j]:
            count += 1
    return count

def main():
    max_n = 10000  # bornes du problème
    # Pré-calcul des nombres premiers pour tous les N possibles
    is_prime = sieve(max_n)

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        result = count_prime_pairs(n, is_prime)
        print(result)

if __name__ == "__main__":
    main()