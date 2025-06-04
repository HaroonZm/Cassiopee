def sieve_of_eratosthenes(limit):
    """
    Génère la liste des nombres premiers jusqu'à 'limit' exclus.

    Args:
        limit (int): La borne supérieure (exclue) pour la recherche des nombres premiers.

    Returns:
        list: Une liste de nombres premiers inférieurs à 'limit'.
    """
    # Initialisation: tous les nombres >=2 sont présumés premiers
    is_prime = [1] * limit
    is_prime[0] = is_prime[1] = 0  # 0 et 1 ne sont pas premiers

    # Itération jusqu'à racine carrée de limit pour marquer les composites
    for i in range(int(limit ** 0.5)):
        if is_prime[i]:
            # Marquer tous les multiples de 'i' (à partir de 2*i) comme non premiers
            is_prime[2 * i :: i] = [0 for _ in range(2 * i, limit, i)]
    
    # Extraire les indices correspondant aux nombres premiers
    primes = []
    for i in range(limit):
        if is_prime[i]:
            primes.append(i)
    return primes

def count_prime_partitions(n_max, k_max, primes):
    """
    Remplit un tableau dp où dp[k][n] est le nombre de façons d'écrire n comme somme de k nombres premiers distincts.

    Args:
        n_max (int): Somme maximale à considérer.
        k_max (int): Nombre maximal de termes premiers.
        primes (list): Liste de nombres premiers disponibles.

    Returns:
        list: Tableau 2D dp tel que dp[k][n] = nombre de décompositions de n avec k premiers distincts.
    """
    # dp[k][n] = nombre de façons d'écrire n comme somme de k premiers distincts
    dp = [[0] * n_max for _ in range(k_max)]
    dp[0][0] = 1  # Il y a 1 façon de faire la somme 0 avec 0 termes (somme vide)

    # Remplissage du tableau dynamique
    for i in range(len(primes)):
        # On considère d'abord le cas où on prend exactement k premiers (jusqu'à k_max-1)
        for k in range(min(i + 1, k_max - 1), 0, -1):
            # Parcourir les sommes possibles en ajoutant le premier courant
            for j in range(primes[i], n_max):
                dp[k][j] += dp[k - 1][j - primes[i]]
    return dp

def main():
    """
    Fonction principale: lit des entrées jusqu'à (0, *_), puis affiche le nombre de façons d'écrire n comme somme de k premiers distincts.

    Entrées:
        Sur chaque ligne: deux entiers n et k (avec 0 <= n < 1121, 0 <= k < 15)
        S'arrête si n == 0.

    Sortie:
        Pour chaque requête, affiche dp[k][n].
    """
    import sys

    r = 1121    # Borne supérieure pour n (exclus)
    k_max = 15  # Nombre maximal de termes premiers

    # Génération de la liste des nombres premiers inférieurs à r
    primes = sieve_of_eratosthenes(r)
    # Pré-calcul des partitions de n en k premiers distincts
    dp = count_prime_partitions(r, k_max, primes)

    # Boucle principale de lecture et affichage des résultats
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            n_k = line.strip().split()
            if not n_k:
                continue
            n, k = map(int, n_k)
            if n == 0:
                break
            print(dp[k][n])
        except Exception:
            break

if __name__ == "__main__":
    main()