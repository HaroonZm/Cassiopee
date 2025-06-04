# Programme pour résoudre le problème de la conjecture de Goldbach
# Pour chaque nombre pair donné en entrée, on calcule le nombre de paires de nombres premiers (p1, p2) telles que p1 + p2 = n.
# On ne compte chaque paire qu'une seule fois, c'est-à-dire (p1, p2) et (p2, p1) ne sont pas deux paires distinctes.

import sys

def sieve_of_eratosthenes(limit):
    """
    Crée une liste indiquant si un nombre est premier ou non jusqu'à la limite donnée.
    Utilisation du crible d'Ératosthène pour générer efficacement les nombres premiers.
    """
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False
    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            for multiple in range(number*number, limit + 1, number):
                is_prime[multiple] = False
    return is_prime

def count_goldbach_pairs(n, is_prime):
    """
    Compte le nombre de paires de nombres premiers (p1, p2) telles que p1 + p2 = n.
    On garantie p1 <= p2 pour éviter de compter deux fois la même paire.
    """
    count = 0
    for p1 in range(2, n//2 + 1):
        p2 = n - p1
        if is_prime[p1] and is_prime[p2]:
            count += 1
    return count

def main():
    # Comme la limite maximale d'entrée est < 2^15 (32768), on pré-calculera les nombres premiers jusqu'à cette limite.
    MAX_LIMIT = 32768
    is_prime = sieve_of_eratosthenes(MAX_LIMIT)

    for line in sys.stdin:
        line = line.strip()
        if line == '0':
            # Fin de lecture des entrées
            break
        n = int(line)
        # Calcul et affichage du nombre de paires pour n
        print(count_goldbach_pairs(n, is_prime))

if __name__ == "__main__":
    main()