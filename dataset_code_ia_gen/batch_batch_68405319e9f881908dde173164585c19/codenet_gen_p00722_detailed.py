import sys

# On sait que le plus grand nombre à tester est < 1 000 000 selon l'énoncé
MAX_LIMIT = 10**6

def sieve_of_eratosthenes(limit):
    """
    Génère une liste booléenne 'is_prime' où is_prime[i] est True si i est premier, False sinon,
    pour tous les i de 0 à limit (inclus).
    Utilisation du crible d'Ératosthène pour une efficacité optimale.
    """
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return is_prime

def find_nth_prime_in_arithmetic_sequence(a, d, n, is_prime):
    """
    Trouve le nième nombre premier dans la progression arithmétique commençant par a
    et avec un pas d, en utilisant la liste booléenne de primalité déjà calculée.
    """
    count = 0
    current = a
    while current <= MAX_LIMIT:
        if is_prime[current]:
            count += 1
            if count == n:
                return current
        current += d
    # Théoriquement, on ne devrait jamais arriver ici selon l'énoncé
    return -1

def main():
    # Pré-calculer tous les nombres premiers jusqu'à 1 000 000 inclus
    is_prime = sieve_of_eratosthenes(MAX_LIMIT)

    for line in sys.stdin:
        line = line.strip()
        if line == "0 0 0":
            break
        a, d, n = map(int, line.split())
        # a et d sont premiers entre eux (donné), on peut directement chercher
        result = find_nth_prime_in_arithmetic_sequence(a, d, n, is_prime)
        print(result)

if __name__ == "__main__":
    main()