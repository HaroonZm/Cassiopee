import sys
import math

def sieve(n):
    """
    Crée une liste booléenne indiquant la primalité des entiers de 0 à n.
    True signifie que l'indice est un nombre premier, False sinon.
    Utilisation du crible d'Ératosthène pour une efficacité optimale.
    """
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    limit = int(math.sqrt(n)) + 1
    for i in range(2, limit):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes

def precompute_twin_quadruples(max_n):
    """
    Pré-calculer pour chaque possible n (jusqu'à max_n) la valeur maximale de la
    taille d'une quadruple de nombres premiers (a, a+2, a+6, a+8) dont la taille
    est <= n.
    Retourne une liste max_size où max_size[x] correspond à la plus grande taille
    d'une quadruple jusqu'à x (ou 0 si aucune).
    """
    primes = sieve(max_n)
    max_size = [0] * (max_n + 1)
    current_max = 0
    # On parcourt tous les nombres jusqu'à max_n pour détecter les quadruples
    for a in range(2, max_n - 8 + 1):
        # Vérification de la condition quadruple de nombres premiers
        if primes[a] and primes[a + 2] and primes[a + 6] and primes[a + 8]:
            size = a + 8
            if size > current_max:
                current_max = size
        max_size[a] = current_max
    # Compléter max_size pour les indices restants (de max_n-7 à max_n)
    for x in range(max_n - 7 + 1, max_n + 1):
        max_size[x] = current_max
    return max_size

def main():
    input_numbers = []
    max_input = 0
    for line in sys.stdin:
        n = int(line.strip())
        if n == 0:
            break
        input_numbers.append(n)
        if n > max_input:
            max_input = n
    # Pré-calculer pour tous les n jusqu'au maximum d'entrée
    max_size = precompute_twin_quadruples(max_input)
    # Pour chaque entrée, afficher la plus grande taille <= n
    for n in input_numbers:
        print(max_size[n])

if __name__ == "__main__":
    main()