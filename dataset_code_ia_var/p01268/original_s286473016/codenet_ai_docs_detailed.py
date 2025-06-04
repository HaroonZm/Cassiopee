import itertools

def sieve_of_eratosthenes(limit):
    """
    Génère une liste indiquant la primalité des entiers de 1 à 'limit' 
    en utilisant le crible d’Ératosthène. 
    Les indices valant 1 correspondent à des nombres premiers, 0 sinon.
    
    Args:
        limit (int): Limite supérieure (non incluse) pour chercher des nombres premiers.
    
    Returns:
        list: Liste d'entiers (0 ou 1) indiquant la primalité pour chaque nombre de 1 à limit.
    """
    # Calcule la borne supérieure pour les divisors nécessaires
    root_limit = int(limit * 0.5)
    # Initialise le tableau de primalité: on considère tous les nombres comme premiers au début
    primes = [1] * limit
    primes[0] = 0  # 1 n'est pas premier
    
    # Commence le crible
    for i in range(1, root_limit):
        if primes[i]:
            # Marque tous les multiples de (i+1) comme non premiers, en commençant à (2i+1)
            primes[2 * i + 1::i + 1] = [0] * len(primes[2 * i + 1::i + 1])
    return primes

def get_next_n_primes(start, count, is_prime_mask):
    """
    Trouve les 'count' premiers nombres premiers supérieurs à 'start'.
    
    Args:
        start (int): Le nombre à partir duquel commencer la recherche (exclu).
        count (int): Nombre de premiers à chercher.
        is_prime_mask (list): Liste de flag de primalité (comme retournée par sieve_of_eratosthenes).
    
    Returns:
        list: Liste contenant 'count' nombres premiers strictement supérieurs à 'start'.
    """
    primes = [0] * count
    found = 0
    i = start + 1
    while found < count:
        if is_prime_mask[i - 1] == 1:
            primes[found] = i
            found += 1
        i += 1
    return primes

def calculate_sums_and_sort(primes):
    """
    Calcule toutes les sommes des combinaisons de 2 nombres dans 'primes' et 
    les doubles de chaque élément, puis retourne la liste triée de ces sommes.
    
    Args:
        primes (list): Liste de nombres premiers.
    
    Returns:
        list: Liste triée des sommes obtenues.
    """
    # Génère toutes les sommes de combinaisons de 2 éléments distincts
    comb_sums = [sum(comb) for comb in itertools.combinations(primes, 2)]
    # Génère le double de chaque nombre
    doubles = [2 * a for a in primes]
    # Agrège les deux et trie le résultat
    result = sorted(comb_sums + doubles)
    return result

def main():
    """
    Programme principal : prépare le crible, puis résout chaque requête utilisateur
    jusqu'à ce que l'entrée soit '-1'.
    Pour chaque requête, lit N et P, calcule les 22 premiers nombres premiers 
    supérieurs à N, calcule les différentes sommes spécifiées, et affiche la 
    P-ième plus petite valeur de la liste.
    """
    # Limite supérieure de recherche pour s'assurer d'avoir toujours assez de premiers
    LIMIT = 110000
    # Construire le masque de primalité au démarrage
    is_prime_mask = sieve_of_eratosthenes(LIMIT)
    
    while True:
        # Lecture des entrées utilisateur
        try:
            N, P = map(int, raw_input().split())
        except Exception:
            # Si la lecture échoue (EOF ou format), arrêter
            break
        # Condition d'arrêt
        if N == -1:
            break
        
        # Récupère les 22 premiers nombres premiers strictement supérieurs à N
        primes = get_next_n_primes(N, 22, is_prime_mask)
        # Calcule les sommes demandées et trie
        sorted_sums = calculate_sums_and_sort(primes)
        # Affiche la P-ième valeur (indices décalés car les listes sont 0-based)
        print sorted_sums[P - 1]

# Lance le programme principal si ce module est exécuté directement
if __name__ == "__main__":
    main()